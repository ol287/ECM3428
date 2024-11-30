from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

# Plaintext to be encrypted
plaintext = b'0123456'  # Note: plaintext should be in bytes

# Step 1: Generate the private key
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Common public exponent
    key_size=2048,          # Key size in bits
    backend=default_backend()
)

# Step 2: Obtain the public key from the private key
public_key = private_key.public_key()

# Step 3: Encrypt the plaintext using the public key
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask generation function
        algorithm=hashes.SHA256(),                   # Hash algorithm
        label=None
    )
)

# Step 4: Decrypt the ciphertext using the private key
decodedtext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask generation function
        algorithm=hashes.SHA256(),                   # Hash algorithm
        label=None
    )
)

# Step 5: Print the texts
print("Plaintext: %s" % plaintext.decode('utf-8'))  # Decode bytes to string
print("Ciphertext: %s" % ciphertext.hex())          # Represent ciphertext as hex
print("Decodedtext: %s" % decodedtext.decode('utf-8'))  # Decode bytes to string
