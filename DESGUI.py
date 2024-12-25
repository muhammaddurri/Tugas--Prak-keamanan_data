from tkinter import Tk, Label, Entry, Button, Text, END
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Fungsi Enkripsi
def encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

# Fungsi Dekripsi
def decrypt(encrypted_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = des.decrypt(decoded_encrypted_text).decode('utf-8')
    return decrypted_text.rstrip()

def handle_encrypt():
    plain_text = entry_plain_text.get()
    key_input = entry_key.get()

    if len(key_input) != 8:
        output_text.delete(1.0, END)
        output_text.insert(END, "Key harus memiliki panjang 8 karakter.")
        return

    key = key_input.encode('utf-8')
    encrypted = encrypt(plain_text, key)
    output_text.delete(1.0, END)
    output_text.insert(END, f"Encrypted Text:\n{encrypted}")

def handle_decrypt():
    encrypted_text = entry_encrypted_text.get()
    key_input = entry_key.get()

    if len(key_input) != 8:
        output_text.delete(1.0, END)
        output_text.insert(END, "Key harus memiliki panjang 8 karakter.")
        return

    key = key_input.encode('utf-8')
    try:
        decrypted = decrypt(encrypted_text, key)
        output_text.delete(1.0, END)
        output_text.insert(END, f"Decrypted Text:\n{decrypted}")
    except Exception as e:
        output_text.delete(1.0, END)
        output_text.insert(END, f"Error: {e}")

# Membuat GUI
root = Tk()
root.title("DES Encryption Tool")
root.geometry("500x400")

Label(root, text="Plain Text:").pack(pady=5)
entry_plain_text = Entry(root, width=50)
entry_plain_text.pack(pady=5)

Label(root, text="Key (8 Karakter):").pack(pady=5)
entry_key = Entry(root, width=50)
entry_key.pack(pady=5)

Label(root, text="Encrypted Text:").pack(pady=5)
entry_encrypted_text = Entry(root, width=50)
entry_encrypted_text.pack(pady=5)

Button(root, text="Encrypt", command=handle_encrypt).pack(pady=10)
Button(root, text="Decrypt", command=handle_decrypt).pack(pady=10)

Label(root, text="Output:").pack(pady=5)
output_text = Text(root, height=10, width=60)
output_text.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()
