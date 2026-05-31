"""
Demonstrates basic asymmetric encryption and decryption using RSA from the
cryptography library. The script generates an RSA private key, derives the
matching public key, encrypts a plaintext message with the public key using
OAEP padding and SHA-256, then decrypts it with the private key.

Install the required library with:
    pip install cryptography
"""

# Import base64 so the encrypted bytes can be printed in a readable text format.
import base64

# Import RSA key generation support so we can create a public/private key pair.
from cryptography.hazmat.primitives.asymmetric import rsa

# Import OAEP and MGF1 padding tools, which make RSA encryption secure in practice.
from cryptography.hazmat.primitives.asymmetric import padding

# Import SHA-256 so OAEP can use a modern secure hash function.
from cryptography.hazmat.primitives import hashes

# Generate a 2048-bit RSA private key; this private key must be kept secret.
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Derive the matching public key from the private key; this public key can be shared.
public_key = private_key.public_key()

# Define the original plaintext message as a string so it is easy to read.
plaintext_message = "This is a secret message encrypted with Bob's public RSA key."

# Convert the plaintext string into bytes because cryptographic functions work with bytes.
plaintext_bytes = plaintext_message.encode()

# Encrypt the plaintext bytes with the public key so only the private key can decrypt them.
ciphertext = public_key.encrypt(
    plaintext_bytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# Print the original readable message before encryption.
print("Original message:", plaintext_message)

# Encode the ciphertext with base64 so the encrypted bytes can be printed safely as text.
ciphertext_base64 = base64.b64encode(ciphertext).decode()

# Print the base64-encoded ciphertext; it should look unreadable compared with the plaintext.
print("Encrypted (base64):", ciphertext_base64)

# Decrypt the ciphertext with the private key using the same OAEP padding configuration.
decrypted_bytes = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# Decode the decrypted bytes back into a string and print the recovered plaintext message.
print("Decrypted message:", decrypted_bytes.decode())
