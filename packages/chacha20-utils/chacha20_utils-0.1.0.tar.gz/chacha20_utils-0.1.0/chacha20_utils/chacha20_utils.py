import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class ChaCha20Cipher:
    def __init__(self, key: bytes):
        """Initialize the cipher with a strict 32-byte key requirement."""
        if len(key) != 32:
            raise ValueError("Key must be exactly 32 bytes (256 bits)")
        self.key = key

    def encrypt(self, plaintext: bytes) -> bytes:
        """Encrypt plaintext using ChaCha20 and prepend the nonce."""
        nonce = os.urandom(16)  # Generate a 16-byte nonce
        cipher = Cipher(algorithms.ChaCha20(self.key, nonce), mode=None, backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext)
        return nonce + ciphertext  # Prepend nonce to ciphertext

    def decrypt(self, data: bytes) -> bytes:
        """Decrypt ciphertext by extracting the nonce first."""
        if len(data) < 16:
            raise ValueError("Ciphertext is too short to contain a nonce")
        nonce, ciphertext = data[:16], data[16:]
        cipher = Cipher(algorithms.ChaCha20(self.key, nonce), mode=None, backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext)

# Example Usage:
if __name__ == "__main__":
    key = os.urandom(32)  # Generate a random 32-byte key
    cipher = ChaCha20Cipher(key)

    plaintext = b"Hello, ChaCha20!"
    encrypted = cipher.encrypt(plaintext)
    print("Encrypted:", encrypted)

    decrypted = cipher.decrypt(encrypted)
    print("Decrypted:", decrypted)
