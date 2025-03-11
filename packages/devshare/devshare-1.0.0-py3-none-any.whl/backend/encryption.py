from Crypto.Cipher import AES
import os
import bcrypt
from config import AES_KEY_SIZE, BCRYPT_SALT_ROUNDS

# Generate a secure AES-256 key
AES_KEY = os.urandom(AES_KEY_SIZE)

def encrypt_chunk(chunk):
    """ Encrypt a chunk using AES-256-GCM """
    cipher = AES.new(AES_KEY, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(chunk)
    return cipher.nonce + tag + ciphertext  # Attach nonce + tag for decryption

def decrypt_chunk(encrypted_chunk):
    """ Decrypt an AES-GCM encrypted chunk """
    nonce = encrypted_chunk[:16]
    tag = encrypted_chunk[16:32]
    ciphertext = encrypted_chunk[32:]

    cipher = AES.new(AES_KEY, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

def hash_password(password):
    """ Hash a password using bcrypt """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(BCRYPT_SALT_ROUNDS))

def verify_password(password, hashed_password):
    """ Verify password using bcrypt """
    return bcrypt.checkpw(password.encode(), hashed_password)
