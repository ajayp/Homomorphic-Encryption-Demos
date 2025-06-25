import tenseal as ts
from functools import reduce

# Step 1: Setup TenSEAL CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.generate_galois_keys()
context.global_scale = 2**40

# Step 2: Simulated encrypted votes
# Let's say 5 voters: 1 = voted for Alice, 0 = voted for Bob
voter_choices = [1, 0, 1, 1, 0]

# Encrypt each vote individually
encrypted_votes = [ts.ckks_vector(context, [vote]) for vote in voter_choices]

# Step 3: Securely tally encrypted votes without decryption
total_encrypted = reduce(lambda a, b: a + b, encrypted_votes)

# Step 4: Decrypt only the final result
final_tally = total_encrypted.decrypt()
print("🧮 Decrypted tally (votes for Alice):", round(final_tally[0])) # RESULT is 3 votes
