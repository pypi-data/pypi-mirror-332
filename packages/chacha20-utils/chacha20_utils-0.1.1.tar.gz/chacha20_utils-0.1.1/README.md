# ChaCha20 Utils

*A simple ChaCha20 encryption/decryption utility for Python.*

[![PyPI](https://img.shields.io/pypi/v/chacha20-utils.svg)](https://pypi.org/project/chacha20-utils/)
[![Python Version](https://img.shields.io/pypi/pyversions/chacha20-utils.svg)](https://pypi.org/project/chacha20-utils/)
[![License](https://img.shields.io/github/license/SAKIB-SALIM/chacha20_utils)](https://github.com/SAKIB-SALIM/chacha20_utils/blob/main/LICENSE)

---

## Features

✔ Simple API for encryption and decryption  
✔ Uses **ChaCha20** for fast, secure encryption  
✔ **Automatic nonce handling** (prepended to ciphertext)  
✔ Requires a **32-byte key** for security  

---

## Installation

Install the package using pip:

```sh
pip install chacha20-utils
```

---

## Usage

```python
from chacha20_utils import ChaCha20Cipher

# Use a 32-byte secret key
key = b'your_32_byte_secret_key_________________'

cipher = ChaCha20Cipher(key)

# Encrypt
plaintext = b"Hello, ChaCha20!"
encrypted = cipher.encrypt(plaintext)
print("Encrypted:", encrypted)

# Decrypt
decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted)
```

---

## Notes

- **The key must be exactly 32 bytes** (256 bits).  
- The **nonce is randomly generated** and prepended to the ciphertext for decryption.  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

Developed by **Sakib Salim**  
GitHub: [sakib-salim](https://github.com/SAKIB-SALIM)
