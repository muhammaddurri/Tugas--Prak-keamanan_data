from stegano import lsb
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def get_image_path():
   
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
    return file_path

def save_image_path():
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    return file_path

def hide_message():
    
    img_path = get_image_path()
    if not img_path:
        messagebox.showwarning("Peringatan", "Tidak ada file gambar yang dipilih.")
        return

    message = entry_message.get()
    if not message:
        messagebox.showwarning("Peringatan", "Pesan rahasia tidak boleh kosong.")
        return

    save_path = save_image_path()
    if not save_path:
        messagebox.showwarning("Peringatan", "Lokasi penyimpanan tidak dipilih.")
        return

    try:
        secret = lsb.hide(img_path, message)
        secret.save(save_path)
        messagebox.showinfo("Berhasil", f"Pesan berhasil disembunyikan dalam gambar. Gambar disimpan di: {save_path}")
    except Exception as e:
        messagebox.showerror("Gagal", f"Gagal menyimpan gambar: {e}")

def show_message():
    
    img_path = get_image_path()
    if not img_path:
        messagebox.showwarning("Peringatan", "Tidak ada file gambar yang dipilih.")
        return

    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            messagebox.showinfo("Pesan Tersembunyi", f"Pesan: {clear_message}")
        else:
            messagebox.showinfo("Tidak Ada Pesan", "Tidak ada pesan tersembunyi dalam gambar ini.")
    except Exception as e:
        messagebox.showerror("Gagal", f"Gagal menampilkan pesan dari gambar: {e}")

def main():
    
    # Membuat jendela utama
    root = tk.Tk()
    root.title("Steganography Tool")
    root.geometry("400x300")

    # Label judul
    tk.Label(root, text="Steganography Tool", font=("Arial", 16)).pack(pady=10)

    # Input pesan
    global entry_message
    tk.Label(root, text="Pesan Rahasia:").pack(pady=5)
    entry_message = tk.Entry(root, width=50)
    entry_message.pack(pady=5)

    # Tombol untuk sembunyikan pesan
    btn_hide = tk.Button(root, text="Sembunyikan Pesan", command=hide_message)
    btn_hide.pack(pady=10)

    # Tombol untuk tampilkan pesan
    btn_show = tk.Button(root, text="Tampilkan Pesan", command=show_message)
    btn_show.pack(pady=10)

    # Tombol keluar
    btn_exit = tk.Button(root, text="Keluar", command=root.quit)
    btn_exit.pack(pady=20)

    # Menjalankan aplikasi
    root.mainloop()

if __name__ == "__main__":
    main()
