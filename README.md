# 🔐 Homomorphic Encryption Demos

## 💡 Why Homomorphic Encryption?

Homomorphic Encryption (HE) refers to a new type of cutting-edge encryption technology that allows computations to be performed directly on encrypted data—without ever exposing the raw inputs. This breakthrough enables secure workflows in areas like:

- Privacy-preserving machine learning  
- Federated finance and encrypted identity checks  
- Secure healthcare and biometric verification  

This repository showcases practical HE demos using two popular encryption schemes, **BFV** and **CKKS**, each tailored to specific use cases.

Built with:
- [TenSEAL](https://github.com/OpenMined/TenSEAL) — CKKS-based encrypted vector math library
- [SEAL-Python](https://github.com/Huelse/SEAL-Python) — Python wrapper for Microsoft SEAL, supporting both BFV and CKKS

## 🤔 Why BFV and CKKS?

This repository uses both **BFV** and **CKKS** encryption schemes because each is optimized for different types of computation:

| Scheme | Precision Type | Best Use | Example Demo |
|--------|----------------|-----------|---------------|
| **BFV** | Exact integers | Binary decisions, like age checks | `seal_demos/` |
| **CKKS** | Approximate floats | Encrypted ML inference and analytics | `tenseal_demos/` |

- 🧮 **BFV** is essential when precision matters—such as verifying whether a value meets a specific threshold.  
- 📊 **CKKS** is perfect for privacy-preserving machine learning and statistical workloads, where small rounding errors are acceptable.

📌 _Note: While TenSEAL includes BFV support, its main strength and tooling focus is on CKKS. For more robust integer logic, we rely on SEAL-Python._

This split ensures each demo showcases the encryption scheme in the context it performs best—without compromise.

## 🗂️ Project Structure

### `tenseal_demos/`
- Demonstrates encrypted ML inference and floating-point operations using CKKS.
- Ideal for showcasing privacy-preserving analytics.

### `seal_demos/`
- Implements discrete logic using BFV.
- Demonstrates secure age checks without revealing user data.

---

## 🧪 How to Run

Each project is self-contained with its own dependencies. To get started:

1. Navigate to the appropriate folder (`tenseal_demos/` or `seal_demos/`)
2. Follow setup instructions in the respective `README.md`

This modular setup ensures that library dependencies remain isolated and don’t conflict across projects.

---
