# Homomorphic Encryption Demos

Homomorphic encryption is a form of encryption that allows computations to be performed directly on encrypted data, so results remain accurate and meaningful after decryption, without ever exposing the underlying sensitive information. For example, in healthcare, patient data can be encrypted and securely shared for statistical analysis or trend detection—researchers can compute averages or other insights without ever seeing any individual's private data.

- [`healthcare.py`](healthcare.py) demonstrates secure aggregation of patient cholesterol levels from multiple clinics, computing the average without exposing any patient's actual value.
- [`votes.py`](votes.py) shows how to tally encrypted votes, so the final count is revealed but individual votes remain private.

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

 2. **Create a Python virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   
4. Run the demos:
   ```sh
   python healthcare.py
   python votes.py
   ```