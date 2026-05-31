"""
Demonstrates basic symmetric encryption and decryption using Fernet from the
cryptography library. Fernet uses a randomly generated secret key to encrypt a
plaintext message into ciphertext, then uses the same key to decrypt it back.

Install the required library with:
    pip install cryptography
"""

# Import Fernet, a high-level symmetric encryption tool from the cryptography library.
from cryptography.fernet import Fernet

# Generate a random symmetric key; this same key is required for both encryption and decryption.
key = Fernet.generate_key()

# Create a Fernet object using the generated key so we can encrypt and decrypt data.
cipher = Fernet(key)

# Define the original plaintext message as a string so it is easy for humans to read.
plaintext_message = "This is a secret message for the cybersecurity internship project."

# Convert the plaintext string into bytes because Fernet encrypts byte data, not regular strings.
plaintext_bytes = plaintext_message.encode()

# Encrypt the plaintext bytes with the symmetric key, producing unreadable ciphertext bytes.
encrypted_message = cipher.encrypt(plaintext_bytes)

# Print the original readable message so we can compare it with the encrypted and decrypted versions.
print("Original message:", plaintext_message)

# Print the encrypted ciphertext; it appears unreadable because the data is protected.
print("Encrypted (ciphertext):", encrypted_message)

# Decrypt the ciphertext using the same symmetric key to recover the original plaintext bytes.
decrypted_bytes = cipher.decrypt(encrypted_message)

# Decode the decrypted bytes back into a normal string and print the recovered message.
print("Decrypted message:", decrypted_bytes.decode())
