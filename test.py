from encryption_tool import generate_key, encrypt_file, decrypt_file

key = generate_key()  # Make the secret key

# Lock the file
encrypt_file('my_secret.txt', key)

# Unlock the file
decrypt_file('my_secret.txt.enc', key)
