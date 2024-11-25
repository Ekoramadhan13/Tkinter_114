import tkinter as tk  # Mengimpor modul tkinter untuk membuat GUI
from tkinter import messagebox  # Mengimpor messagebox untuk menampilkan pesan kesalahan

# Fungsi untuk melakukan prediksi berdasarkan nilai input
def hasil_prediksi():
    try:
        # Mengambil nilai dari setiap entry dan mengonversinya menjadi float
        nilai = [float(entry.get()) for entry in nilai_entries]
        
        # Jika semua input valid, tampilkan hasil prediksi
        hasil_label.config(text="Prodi Pilihan: Teknologi Informasi")
    except ValueError:
        # Jika ada input yang tidak valid, tampilkan pesan kesalahan
        messagebox.showerror("Input Error", "Silakan masukkan nilai yang valid (angka) di semua kolom.")

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Menetapkan judul jendela
root.geometry("400x600")  # Mengatur ukuran jendela (lebar x tinggi)

# Membuat label untuk judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.pack(pady=10)  # Menempatkan label di jendela dengan padding vertikal

# Membuat daftar untuk menyimpan widget Entry
nilai_entries = []
for i in range(10):
    entry = tk.Entry(root)  # Membuat widget Entry untuk input nilai
    entry.pack(pady=5)  # Menempatkan entry di jendela dengan padding vertikal
    nilai_entries.append(entry)  # Menambahkan entry ke daftar nilai_entries

# Membuat tombol untuk menghasilkan prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.pack(pady=20)  # Menempatkan tombol di jendela dengan padding vertikal

# Membuat label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14))
hasil_label.pack(pady=10)  # Menempatkan label di jendela dengan padding vertikal

# Menjalankan loop utama aplikasi
root.mainloop()
