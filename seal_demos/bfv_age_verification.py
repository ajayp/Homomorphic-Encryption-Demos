from seal import *
import argparse

# --- Configuration and Key Generation (Trusted Setup) ---
def create_bfv_context():
    poly_modulus_degree = 8192
    parms = EncryptionParameters(scheme_type.bfv)
    parms.set_poly_modulus_degree(poly_modulus_degree)
    parms.set_coeff_modulus(CoeffModulus.BFVDefault(poly_modulus_degree))
    parms.set_plain_modulus(PlainModulus.Batching(poly_modulus_degree, 20))

    context = SEALContext(parms)
    keygen = KeyGenerator(context)
    
    public_key = keygen.create_public_key()
    secret_key = keygen.secret_key()

    return context, public_key, secret_key

# --- User's Actions ---
def user_encrypts_age(context, public_key, age):
    encryptor = Encryptor(context, public_key)
    plain_age = Plaintext(str(age))
    encrypted_age = encryptor.encrypt(plain_age)
    return encrypted_age

def user_decrypts_result(context, secret_key, encrypted_result):
    decryptor = Decryptor(context, secret_key)

    plain_modulus = PlainModulus.Batching(8192, 20).value()
    decrypted = decryptor.decrypt(encrypted_result)
    result = decode_signed(decrypted, plain_modulus)
    # print("Decrypted hex:", decrypted.to_string())
    # print("Decrypted int:", int(decrypted.to_string(), 16))
    return result

def decode_signed(decrypted, plain_modulus):
    value = int(decrypted.to_string(), 16)
    if value > plain_modulus // 2:
        value -= plain_modulus
    return value


# --- Service's Actions ---
def service_verifies_age(context, encrypted_age, required_age):
    evaluator = Evaluator(context)
    plain_required = Plaintext(str(required_age))
    encrypted_diff = evaluator.sub_plain(encrypted_age, plain_required)
    return encrypted_diff


# --- Main Execution Flow ---
def main():
    parser = argparse.ArgumentParser(description="Homomorphic age verification demo using the BFV scheme.")
    parser.add_argument("--age", type=int, default=25, help="The user's age to check.")
    args = parser.parse_args()

    user_age = args.age
    required_age = 18
    print(f"User's age: {user_age}. Threshold: {required_age}.")

    context, public_key, secret_key = create_bfv_context()
    encrypted_age = user_encrypts_age(context, public_key, user_age)

    print(f"Server computes (age - {required_age}) homomorphically...")
    encrypted_result = service_verifies_age(context, encrypted_age, required_age)
    decrypted_diff = user_decrypts_result(context, secret_key, encrypted_result)

    print(f"Decrypted result: {decrypted_diff} - (this will be >= 0 if age >= 18)") 
    print(f"✅ Age verification successful: {decrypted_diff >= 0}")

if __name__ == "__main__":
    main()
