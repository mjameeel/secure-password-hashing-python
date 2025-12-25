# Secure Password Hashing Tool (Python)

## Overview
This repository demonstrates the implementation of a **simple password hashing tool** using Python. It is designed for educational purposes, helping learners understand **secure password storage**, the role of **salting**, and the practical differences between commonly used hashing approaches.

The project compares **bcrypt** and **SHA-256 (SHA-2 family)** to highlight why modern systems require adaptive, computationally expensive hashing algorithms for password storage.

---

## Why Password Hashing Matters
Storing passwords in plaintext or using weak hashing techniques exposes systems to serious security risks, including brute-force and rainbow table attacks. Password hashing ensures that even if a database is compromised, original passwords remain protected.

This project reinforces industry best practices recommended by **OWASP** and **NIST**, emphasizing secure handling of user credentials.

---

## bcrypt vs SHA-256 (Key Differences)

### SHA-256
- Part of the SHA-2 family of cryptographic hash functions
- Fast and deterministic
- Suitable for data integrity checks
- **Not ideal for password storage on its own** due to speed, which makes brute-force attacks feasible

### bcrypt
- Adaptive password hashing algorithm
- Automatically incorporates salting
- Computationally expensive by design
- Resistant to brute-force and rainbow table attacks
- Widely recommended for modern password storage

**Key Takeaway:**  
While SHA-256 is cryptographically strong, bcrypt is better suited for password hashing because it is intentionally slow and configurable.

---

## Features of the Tool
- Accepts plaintext password input
- Hashes passwords using:
  - bcrypt
  - SHA-256
- Applies salting to improve security
- Validates input (empty, long, non-ASCII passwords)
- Outputs hashed passwords to a file for inspection

---

## Simple Usage Example

### Requirements
- Python 3.x
- `bcrypt` library

Install dependencies:
```bash
pip install bcrypt
