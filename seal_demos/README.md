# 🧠 Encrypted Age Verification with BFV (SEAL-Python)

This demo illustrates a privacy-preserving age verification check using the [SEAL-Python](https://github.com/Huelse/SEAL-Python) library, a Python wrapper for [Microsoft SEAL](https://github.com/microsoft/SEAL). It leverages the Brakerski/Fan-Vercauteren (BFV) scheme, which is designed for exact computations on encrypted **integers** — ideal for threshold logic like “is age ≥ 18?”

The idea: users encrypt their age locally and send it to a verifier, who homomorphically checks if the age meets a threshold — without ever seeing the actual value.

---

## 🧠 What It Demonstrates

- Trusted setup with key generation
- Integer encryption using BFV
- Homomorphic subtraction (`age - required_age`)
- Decryption and threshold comparison

---

## 🎯 Use Case: Private Age Check

Imagine a service that needs to verify whether a user is over 18 without ever seeing their actual age.

1. **User:** Encrypts their age (e.g., `25`) using a public key.
2. **Service:** Receives the encrypted age and homomorphically computes `(encrypted_age - 18)` — without decrypting or learning any values.
3. **User (or verifier):** Decrypts the result. If it’s **≥ 0**, the user meets the age requirement.

🧪 _In this demo, the decryption happens inside the script to showcase the full workflow. A real-world deployment would keep encrypted results opaque to the verifier._

---

## 🧾 Expected Output

```text
User's age: 25. Threshold: 18.
Server computes (age - 18) homomorphically...
Decrypted result: 7
✅ Age verification successful: True

User's age: 17. Threshold: 18.
Server computes (age - 18) homomorphically...
Decrypted result: -1
✅ Age verification successful: False
```

---

## 🚀 Getting Started

### Prerequisites

**Platform Compatibility:** These instructions have been verified on **macOS**. The `SEAL-Python` library requires compiling C++ code, which can be platform-specific. While the steps are similar for Linux and Windows, you may need to adapt them to your environment.

- Python 3.8+
- macOS or Linux (Windows supported with slight adjustments)
- C++ compiler (e.g. `clang`, `gcc`)
- [CMake](https://cmake.org/download/) ≥ 3.16


Install basic dependencies:
```bash
brew install cmake       # or use your OS package manager
```

---

### Installation Steps

1. **CD to `seal_demos` folder:**

2. **Create a Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Clone SEAL-Python:**
   ```bash
   git clone https://github.com/Huelse/SEAL-Python.git
   cd SEAL-Python
   ```

5. **Initialize submodules:**
   ```bash
   git submodule update --init --recursive
   ```

6. **Build Microsoft SEAL:**
   ```bash
   cd SEAL
   cmake -S . -B build -DSEAL_USE_MSGSL=OFF -DSEAL_USE_ZLIB=OFF -DSEAL_USE_ZSTD=OFF
   cmake --build build
   ```

7. **CD back to the directory `SEAL-Python`**
    ```bash 
    cd .. 
    ```

8. **Build Python bindings:**
   ```bash
   python setup.py build_ext -i
   ```

   This creates a file named `seal.<platform>.so` (or `.pyd` on Windows) in your current folder.

9. **Copy the `seal.*.so` file generated in step 8 up to the parent `seal_demos` folder** so it can be imported by the demo script.
   ```bash
   cp seal.*.so ../
  
---

## Running the Demo

1. **CD back to directory `seal_demos`**

2. **Run the demo:**
   ```bash
   python bfv_age_verification.py --age 25
   python bfv_age_verification.py --age 17
   ```

---


## 🧩 Notes on SEAL-Python Compatibility

SEAL-Python wraps Microsoft SEAL’s C++ library with a Pythonic interface. Key differences:

- Encoders like `IntegerEncoder` have been deprecated
- `SEALContext.Create()` replaced with `SEALContext(parms)`
- Operations return new objects instead of mutating inputs
- Use `create_public_key()` for key access
- Decrypted plaintexts must be interpreted as signed integers modulo `plain_modulus`


