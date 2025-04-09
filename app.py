import tkinter as tk
from tkinter import filedialog
from encryption_tool import generate_key, encrypt_file, decrypt_file

key = generate_key()

def encrypt_action():
    file_path = filedialog.askopenfilename()
    encrypt_file(file_path, key)
    status_label.config(text="✅ File Encrypted!")

def decrypt_action():
    file_path = filedialog.askopenfilename()
    decrypt_file(file_path, key)
    status_label.config(text="🔓 File Decrypted!")

# Set up the window
app = tk.Tk()
app.title("🔐 Advanced Encryption Tool")
app.geometry("300x200")

encrypt_button = tk.Button(app, text="Encrypt File", command=encrypt_action)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(app, text="Decrypt File", command=decrypt_action)
decrypt_button.pack(pady=10)

status_label = tk.Label(app, text="")
status_label.pack(pady=20)

app.mainloop()
