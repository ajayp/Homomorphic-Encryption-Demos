import tenseal as ts
from functools import reduce

# STEP 1: Shared Encryption Context - distributed to all clinics
def create_shared_context():
    context = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[60, 40, 40, 60]
    )
    context.generate_galois_keys()
    context.global_scale = 2**40
    return context

def encrypt_clinic_data(context, clinic_data):
    """Encrypts cholesterol data for each clinic."""
    encrypted_data = {}
    for clinic_name, values in clinic_data.items():
        print(f"Clinic '{clinic_name}' encrypting {len(values)} patient values...")
        encrypted_data[clinic_name] = ts.ckks_vector(context, values)  # Encrypt as a single vector
    return encrypted_data

def aggregate_encrypted_data(encrypted_data):
    """Aggregates encrypted cholesterol data from all clinics."""
    # First, sum the values *within* each encrypted vector using the homomorphic .sum() method.
    # Then, add these partial sums together to get the grand total.
    clinic_sums = [vec.sum() for vec in encrypted_data.values()]
    return reduce(lambda x, y: x + y, clinic_sums)

def compute_encrypted_average(aggregated_data, total_patients):
    """Computes the encrypted average cholesterol level."""
    return aggregated_data * (1 / total_patients)


def compute_cholesterol_average(context, total_patients, encrypted_clinic_data ):
    """
    Securely computes the average cholesterol level across multiple clinics.
    """

    # STEP 1: Aggregate encrypted data
    aggregated_encrypted_data = aggregate_encrypted_data(encrypted_clinic_data)

    # STEP 2: Calculate the encrypted average
    average_encrypted = compute_encrypted_average(aggregated_encrypted_data, total_patients)

    # STEP 3: Research team decrypts final insight
    average_result = average_encrypted.decrypt()    
    return average_result
    
def main():
    # STEP 1: Create a shared encryption context
    shared_context = create_shared_context()

    # Sample data: cholesterol readings from different clinics
    # Each clinic has a different number of patients, and the values are in mg/dL
    print("🔐 Creating shared encryption context for clinics..."    )
    clinic_data = {
        "Clinic A": [190.0, 200.5], # 2 patients
        "Clinic B": [205.3, 199.8], # 2 patients
        "Clinic C": [202.1] # 1 patient
        # Add more clinics as needed
    }
    
    # STEP 2: Compute the total number of patients
    total_patients = sum(len(values) for values in clinic_data.values())
    print(f"Total patients across clinics: {total_patients}")

    # STEP 3: Encrypt cholesterol data from each clinic
    print("🔐 Encrypted data from clinics")
    encrypted_clinic_data = encrypt_clinic_data(shared_context, clinic_data)

    clinic_data = {} # Reset clinic_data to avoid confusion in the next steps
    
    # STEP 4: Compute the average cholesterol level from encrypted data
    print("🔐 Compute the average cholesterol level using encrypted cholesterol data...")
    average_result = compute_cholesterol_average(shared_context, total_patients, encrypted_clinic_data)
    print("🔐 Securely computed average cholesterol level:", round(average_result[0], 2), "mg/dL")  # RESULT is 199.54 mg/d L()

if __name__ == "__main__":
    main()