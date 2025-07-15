# Homomorphic Encryption

Homomorphic encryption is a form of encryption that allows computations to be performed directly on encrypted data, so results remain accurate and meaningful after decryption, without ever exposing the underlying sensitive information.   

For example, in healthcare, sensitive patient information can be encrypted and shared with researchers without ever seeing any individual's private data. This enables statistical analysis, or even machine learning algorithms to be performed directly on the encrypted data.

### 🔐 How it works:
- **Encrypt patient data**: Lab results or diagnoses are encrypted before sharing
- **Compute securely**: Operations like averages, totals, or even machine learning models are run *without* decrypting the data
- **Decrypt the outcome**: Only the final results are decrypted—never the individual records

Result: Actionable insights are gained while keeping personal health information completely private.  

- [`healthcare.py`](ckks_healthcare.py) demonstrates secure aggregation of patient cholesterol levels from multiple clinics, computing the average without exposing any patient's actual value.
- [`votes.py`](ckks_votes.py) shows how to tally encrypted votes, so the final count is revealed but individual votes remain private.

## Installation

1. **CD to the directory `tenseal_demos`**

2. **Create a Python virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   
4. **Run the demos:**
   ```sh
   python ckks_healthcare.py
   python ckks_votes.py
   ```
