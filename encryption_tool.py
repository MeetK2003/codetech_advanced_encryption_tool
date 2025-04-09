from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# AES needs key to lock/unlock. We make a strong one:
def generate_key():
    return get_random_bytes(32)  # 256 bits = 32 bytes

# Make the file super secret (encrypt it!)
def encrypt_file(filename, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(filename, 'rb') as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    with open(filename + ".enc", 'wb') as f:
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)

# Open the file (decrypt it!)
def decrypt_file(filename, key):
    with open(filename, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    
    with open(filename.replace(".enc", ".dec"), 'wb') as f:
        f.write(data)
