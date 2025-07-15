# Homomorphic Encryption Demos

## 💡 Why Homomorphic Encryption?

Homomorphic Encryption refers to a new type of encryption technology that allows computation to be directly on encrypted data, without requiring any decryption in the process.

Homomorphic encryption enables computation on encrypted data, unlocking new possibilities for privacy-preserving ML, identity verification, secure medical workflows, and federated finance — without revealing raw inputs.

This repository contains several homomorphic encryption demos built using:
- [TenSEAL](https://github.com/OpenMined/TenSEAL) — for CKKS-based encrypted vector math
- [SEAL-Python](https://github.com/Huelse/SEAL-Python) — a Python wrapper around Microsoft SEAL, supporting BFV and CKKS schemes

---
## 🔐 Projects

### `tenseal_demos/`
Demonstrates encrypted inference using CKKS. Floating-point operations and privacy-preserving ML workloads.

### `seal_demos/`
A discrete integer demo using BFV — built with SEAL-Python. It shows how a service can check if a user's age meets a threshold without ever seeing the actual age.

📌 _Note: This project intentionally uses BFV because TenSEAL does not support BFV-based integer logic for threshold comparisons._

---

## 🧪 How to Run

Each project is self-contained and has its own dependencies. Please follow the setup instructions in the `README.md` inside each sub-folder (`tenseal_demos/` and `seal_demos/`).

This separation ensures that the dependencies for one demo do not conflict with the other.

---
