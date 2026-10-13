import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class TelemetryCryptor:
    """
    Enforces 'Reasonable Measures' of secrecy under TUTSA Sec. 134A.002(6).
    Encrypts proprietary EdgeAI skeletal tracking data before cloud routing.
    """
    def __init__(self):
        # In production, pull this strictly from a secure hardware HSM or vault
        self.secret_key = AESGCM.generate_key(bit_length=256)
        self.aad = b"ODYNEX_CHUTE_SYNC_PROPRIETARY"

    def encrypt_payload(self, raw_telemetry_bytes: bytes) -> bytes:
        nonce = os.urandom(12)
        aesgcm = AESGCM(self.secret_key)
        encrypted_data = aesgcm.encrypt(nonce, raw_telemetry_bytes, self.aad)
        return nonce + encrypted_data

    def decrypt_payload(self, encrypted_payload: bytes) -> bytes:
        nonce = encrypted_payload[:12]
        ciphertext = encrypted_payload[12:]
        aesgcm = AESGCM(self.secret_key)
        return aesgcm.decrypt(nonce, ciphertext, self.aad)
