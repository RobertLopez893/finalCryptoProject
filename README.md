# 🛡️ Hybrid Cryptosystem: Toy Block Cipher & RSA Key Wrapping

![Language](https://img.shields.io/badge/Language-C-00599C?style=for-the-badge&logo=c&logoColor=white)
![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A robust academic implementation of a **Hybrid Cryptosystem**. This project combines a custom **Symmetric Toy Block Cipher** (SP-Network) implemented in **C** with an **RSA Key Wrapping** mechanism implemented in **Python** to securely exchange keys.

---

## 🚀 Features

### 🔐 Symmetric Encryption (C)
- **Custom SP-Network:** Implements Substitution-Permutation Network architecture.
- **CTR Mode:** Uses Counter Mode for stream-like encryption, allowing random access and no padding.
- **Dynamic Components:** Generates and utilizes custom S-Boxes and Permutation Tables.
- **File Handling:** Encrypts and decrypts files using **Base64** encoding for safe transport.

### 🔑 Asymmetric Key Wrapping (Python)
- **RSA Implementation:** Generates 128-bit RSA key pairs (using 64-bit primes).
- **Key Wrapping:** Encrypts the 32-bit Symmetric Key using Alice's Public Key.
- **Hex/Int Conversion:** Seamlessly bridges the gap between C (Hex files) and Python (Integer math).

---

## 🛠️ Prerequisites

To run this project, you need:

1.  **GCC Compiler** (for the C code).
2.  **Python 3.x**.
3.  **PyCryptodome** library.

```bash
pip install pycryptodome
