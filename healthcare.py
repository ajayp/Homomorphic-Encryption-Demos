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

context = create_shared_context()

# STEP 2: Each clinic encrypts its own patient data locally
# Let's simulate 3 clinics with different cholesterol readings
clinic_data = {
    "Clinic A": [190.0, 200.5],
    "Clinic B": [205.3, 199.8],
    "Clinic C": [202.1]
}
patient_count = sum(len(v) for v in clinic_data.values())

# STEP 3: Encrypt each patient’s data at their respective clinic
encrypted_all = []
for clinic_name, values in clinic_data.items():
    for val in values:
        enc = ts.ckks_vector(context, [val])
        encrypted_all.append(enc)

# STEP 4: Secure aggregation on the central server
total_encrypted = reduce(lambda x, y: x + y, encrypted_all)

# STEP 5: Compute average (still encrypted)
average_encrypted = total_encrypted * (1 / patient_count)

# STEP 6: Research team decrypts final insight
average_result = average_encrypted.decrypt()
print("🔐 Securely computed average cholesterol level:", round(average_result[0], 2), "mg/dL") # RESULT is 199.54 mg/dL
