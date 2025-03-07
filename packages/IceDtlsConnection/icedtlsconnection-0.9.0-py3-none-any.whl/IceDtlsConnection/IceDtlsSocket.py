#!/usr/bin/env python3
import aioice

from OpenSSL.SSL import Context, Connection, DTLS_METHOD, WantReadError, VERIFY_PEER, VERIFY_FAIL_IF_NO_PEER_CERT, OP_NO_QUERY_MTU
from OpenSSL import crypto
from pylibsrtp import Policy, Session
from random import randbytes, randrange
from socket import gethostname

SRTP_KEY_LEN = 16
SRTP_SALT_LEN = 14

def get_srtp_key_salt(src, idx):
    key_start = idx * SRTP_KEY_LEN
    salt_start = 2 * SRTP_KEY_LEN + idx * SRTP_SALT_LEN
    return (
        src[key_start:key_start + SRTP_KEY_LEN] +
        src[salt_start:salt_start + SRTP_SALT_LEN]
    )

def _gen_openssl():
    '''
    Returns (cert, key) as ASCII PEM strings
    '''

    pkey = crypto.PKey()
    pkey.generate_key(crypto.TYPE_RSA, 2048)

    x509 = crypto.X509()
    subject = x509.get_subject()
    subject.commonName = gethostname()
    x509.set_issuer(subject)
    x509.gmtime_adj_notBefore(0)
    x509.gmtime_adj_notAfter(5*365*24*60*60)
    x509.set_pubkey(pkey)
    x509.set_serial_number(randrange(100000))
    x509.set_version(2)
    x509.add_extensions([
        crypto.X509Extension(b'subjectAltName', False,
            ','.join([
                'DNS:%s' % gethostname(),
                'DNS:*.%s' % gethostname(),
                'DNS:localhost',
                'DNS:*.localhost']).encode()),
        crypto.X509Extension(b"basicConstraints", True, b"CA:false")])

    x509.sign(pkey, 'SHA256')

    return (crypto.dump_certificate(crypto.FILETYPE_PEM, x509),
        crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey))


class DtlsContext:
    def __init__(self, cert_pem = None, key_pem = None, remote_fingerprint = None):
        self.ctx = Context(DTLS_METHOD)
        self.ctx.set_verify(VERIFY_PEER | VERIFY_FAIL_IF_NO_PEER_CERT, self.verify_callback)
        if key_pem != None:
            self.ctx.use_privatekey(crypto.load_privatekey(crypto.FILETYPE_PEM, key_pem))
        if cert_pem != None:
            self.ctx.use_certificate(crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem))
        self.cookie = None
        self.remote_fingerprint = remote_fingerprint
        self.ctx.set_cipher_list(b'HIGH:!CAMELLIA:!aNULL')
        self.ctx.set_tlsext_use_srtp(b'SRTP_AES128_CM_SHA1_80')
        self.ctx.set_options(OP_NO_QUERY_MTU)
        self.ctx.set_cookie_generate_callback(self.generate_cookie)
        self.ctx.set_cookie_verify_callback(self.verify_cookie)

    def generate_cookie(self, ssl):
        self.cookie = randbytes(5)
        return self.cookie

    def verify_cookie(self, ssl, cookie):
        return cookie == self.cookie

    def verify_callback(self, connection, cert, error_number, error_depth, ok):
        if cert != None:
            remote_fingerprint = cert.digest("SHA256").decode('ascii')
            if remote_fingerprint != self.remote_fingerprint.upper():
                raise Exception('DTLS fingerprint does not match')
                return 0
            else:
                return 1
        return 1


class IceDtlsConnection(aioice.Connection):
    LARGE_BUFFER = 65536

    def __init__(self, ice_controlling=True, stun_server=("stun.l.google.com", 19302)):
        aioice.Connection.__init__(self, ice_controlling=ice_controlling, components=1, stun_server=stun_server)
        self.local_ssl_cert, self.local_ssl_key = _gen_openssl()
        self.encrypted = False
    
    @property
    def local_fingerprint(self):
        return crypto.load_certificate(crypto.FILETYPE_PEM, self.local_ssl_cert).digest('SHA256').decode('ascii')

    async def connect(self, is_server, remote_fingerprint):
        await super(IceDtlsConnection, self).connect()
        context = DtlsContext(self.local_ssl_cert, self.local_ssl_key, remote_fingerprint = remote_fingerprint) 
        self.conn = Connection(context.ctx)

        if is_server:
            self.conn.set_accept_state()
            self.conn.set_ciphertext_mtu(1500)
            latest_client_hello = None
            s_listening = True
            s_handshaking = False
            while s_listening or s_handshaking:
                chunk = await super(IceDtlsConnection, self).recv()
                self.conn.bio_write(chunk)
                try:
                    if chunk[0] == 22 and chunk[13] == 1:
                        latest_client_hello = chunk
                except IndexError:  # pragma: no cover
                    pass
                if s_listening:
                    try:
                        self.conn.DTLSv1_listen()
                    except WantReadError:
                        pass
                    else:
                        s_listening = False
                        s_handshaking = True
                        # Write the duplicate ClientHello.
                        self.conn.bio_write(latest_client_hello)
                if s_handshaking:
                    try:
                        self.conn.do_handshake()
                    except WantReadError:
                        pass
                    else:
                        s_handshaking = False
                try:
                    chunk = self.conn.bio_read(self.LARGE_BUFFER)
                except WantReadError:
                    pass
                else:
                    if chunk:  # pragma: no cover
                        await super(IceDtlsConnection, self).send(chunk)
            material = self.conn.export_keying_material(b'EXTRACTOR-dtls_srtp', 2 * (SRTP_KEY_LEN + SRTP_SALT_LEN))
            if material is None:
                raise Exception('DTLS could not extract SRTP keying material')
            self.srtp_tx_key = get_srtp_key_salt(material, 1) # SRTP key for transmiting
            self.srtp_rx_key = get_srtp_key_salt(material, 0) # SRTP key for receiving
            tx_policy = Policy(key=self.srtp_tx_key, ssrc_type=Policy.SSRC_ANY_OUTBOUND)
            self.tx_session = Session(policy=tx_policy)
            rx_policy = Policy(key=self.srtp_rx_key, ssrc_type=Policy.SSRC_ANY_INBOUND)
            self.rx_session = Session(policy=rx_policy)
            self.encrypted = True
        else:
            self.conn.set_connect_state()
            self.conn.set_ciphertext_mtu(1500)
            while True:
                try:
                    self.conn.do_handshake()
                except WantReadError:
                    pass
                else:
                    break
                try:
                    chunk = self.conn.bio_read(self.LARGE_BUFFER)
                    if chunk:  # pragma: no cover
                        await super(IceDtlsConnection, self).send(chunk)
                        chunk = await super(IceDtlsConnection, self).recv()
                        self.conn.bio_write(chunk)
                except WantReadError:
                    break
            material = self.conn.export_keying_material(b'EXTRACTOR-dtls_srtp', 2 * (SRTP_KEY_LEN + SRTP_SALT_LEN))
            if material is None:
                raise Exception('DTLS could not extract SRTP keying material')
            self.srtp_tx_key = get_srtp_key_salt(material, 0) # SRTP key for transmiting
            self.srtp_rx_key = get_srtp_key_salt(material, 1) # SRTP key for receiving
            tx_policy = Policy(key=self.srtp_tx_key, ssrc_type=Policy.SSRC_ANY_OUTBOUND)
            self.tx_session = Session(policy=tx_policy)
            rx_policy = Policy(key=self.srtp_rx_key, ssrc_type=Policy.SSRC_ANY_INBOUND)
            self.rx_session = Session(policy=rx_policy)
            self.encrypted = True

    async def send(self, rtp, encrypted=True):
        if encrypted:
            assert self.encrypted
            srtp = self.tx_session.protect(rtp)
            await super(IceDtlsConnection, self).send(srtp)
        else:
            await super(IceDtlsConnection, self).send(rtp)

    async def recv(self, encrypted=True):
        if encrypted:
            assert self.encrypted
            srtp = await super(IceDtlsConnection, self).recv()
            return self.rx_session.unprotect(srtp)
        else:
            return await super(IceDtlsConnection, self).recv()

    @property
    def srtp_tx(self):
        return self.srtp_tx_key

    @property
    def srtp_rx(self):
        return self.srtp_rx_key
