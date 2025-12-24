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
```

## 📂 Project Structure

- **main.c** - Core implementation of the Toy Block Cipher (Alice & Bob logic).

- **rsa_key_wrapper.py** - Python script for generating RSA keys and wrapping/unwrapping the symmetric key.

- ***.txt** - The system generates several text files for keys, S-boxes, and encrypted outputs.

## ⚡ Usage Guide
The workflow simulates a secure communication channel between Alice (Sender) and Bob (Receiver).

### Phase 1: Setup & RSA Keys 🐍
Run the Python script to generate RSA keys for Bob.

```bash

python rsa_key_wrapper.py
```

# Select Option 1: Generate RSA Key Pair

### Phase 2: Alice Generates the Secret 💻
Compile and run the C program.

```bash

gcc main.c -o cipher
./cipher
```

# Select Option 1 to generate the Symmetric Key, S-Box, and Permutation.

# Output: key.txt, sbox.txt, perm.txt.

### Phase 3: Key Wrapping (The Bridge) 🐍
Alice uses Python to encrypt the Symmetric Key using Bob's Public Key.

```bash

python rsa_key_wrapper.
```

# Select Option 2: RSA Cipher
# Input: key.txt -> Output: encrypted_key.txt
Alice sends encrypted_key.txt and the sbox/perm files to Bob.

### Phase 4: Encryption (Alice) 💻
Alice uses the C program to encrypt her message file using the original key.txt.

``` bash

./cipher
```

# Select Option 2 (Alice Encrypt)
### Phase 5: Decryption (Bob) 🔓
Bob recovers the Key: Bob uses his Private RSA Key in Python to decrypt encrypted_key.txt.

``` bash

python rsa_key_wrapper.py

```

# Select Option 3: RSA Decipher
# Output: recovered_key.txt
Bob decrypts the Message: Bob runs the C program using the recovered_key.txt.


``` bash

./cipher

```
# Select Option 3 (Bob Decrypt)
## 👥 Authors
- José Roberto López Reyes

- Alejandro Hernández Zamora

Computer Systems Engineering - ESCOM IPN Cryptography Course - Group 6CV4

Disclaimer: This is an educational project designed to demonstrate cryptographic principles. It is intended for academic use and not for securing sensitive production data.
