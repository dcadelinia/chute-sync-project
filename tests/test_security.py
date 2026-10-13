import pytest
from src.security.encryption import TelemetryCryptor

def test_cryptographic_integrity():
    """ Verifies that data remains secure and uncorrupted during encryption loops. """
    cryptor = TelemetryCryptor()
    original_payload = b"TEAM_04_ARENA_TELEMETRY_STREAM_SECURE"
    
    # Process encryption loop
    encrypted_package = cryptor.encrypt_payload(original_payload)
    assert encrypted_package != original_payload, "Data packaging failed encryption masking check."
    
    # Process decryption verification
    decrypted_payload = cryptor.decrypt_payload(encrypted_package)
    assert decrypted_payload == original_payload, "Data stream suffered corruption during transport translation."
