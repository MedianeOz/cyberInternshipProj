"""
Demonstrates digital signatures with RSA using the cryptography library.

Part 1 shows the normal valid-signature flow: a private key signs a message,
and the matching public key verifies that the message was not changed.

Part 2 shows the tampered-message flow: the original signature is checked
against a modified message, causing verification to fail with InvalidSignature.

Install the required library with:
    pip install cryptography
"""

# Import base64 so the binary signature can be printed as readable text.
import base64

# Import InvalidSignature so we can catch the expected error for tampered data.
from cryptography.exceptions import InvalidSignature

# Import RSA key generation support so we can create a public/private key pair.
from cryptography.hazmat.primitives.asymmetric import rsa

# Import PSS and MGF1 padding, which are recommended for RSA signatures.
from cryptography.hazmat.primitives.asymmetric import padding

# Import SHA-256 so the signing and verification process uses a secure hash.
from cryptography.hazmat.primitives import hashes

# Generate a 2048-bit RSA private key; this private key is used to create signatures.
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Derive the public key from the private key; this public key is used to verify signatures.
public_key = private_key.public_key()

# Define the original plaintext message as a string so it is easy to read.
message = "Alice approves this cybersecurity internship document."

# Convert the message into bytes because cryptographic signing functions work with bytes.
message_bytes = message.encode()

# Sign the message bytes using the private key, RSA-PSS padding, and SHA-256 hashing.
signature = private_key.sign(
    message_bytes,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256(),
)

# Print the original message so we can see exactly what was signed.
print("Message:", message)

# Encode the binary signature as base64 so it can be displayed safely as text.
signature_base64 = base64.b64encode(signature).decode()

# Print the base64 version of the signature.
print("Signature (base64):", signature_base64)

# Verify the signature with the public key to confirm the message is authentic and unchanged.
public_key.verify(
    signature,
    message_bytes,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256(),
)

# If verification did not raise an exception, the signature is valid.
print("Signature valid: True")

# Modify the original message slightly to simulate tampering after the signature was created.
tampered_message = "Alice approves this cybersecurity internship documents."

# Convert the tampered message into bytes so it can be checked against the original signature.
tampered_message_bytes = tampered_message.encode()

# Try to verify the original signature against the tampered message.
try:
    # This should fail because the signature was created for the original message, not this modified one.
    public_key.verify(
        signature,
        tampered_message_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )

    # This line would only run if verification unexpectedly succeeded.
    print("Signature valid: True")
except InvalidSignature:
    # Catch the expected failure and explain that the message no longer matches the signature.
    print("Signature valid: False — message was tampered!")
