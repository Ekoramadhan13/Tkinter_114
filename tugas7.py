import sqlite3
import tkinter as tk
from tkinter import messagebox

# Membuat ke database SQLite
conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

# Buat tabel nilai_siswa 
cursor.execute('''
CREATE TABLE IF NOT EXISTS nilai_siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_siswa TEXT NOT NULL,
    biologi INTEGER,
    fisika INTEGER,
    inggris INTEGER,
    prediksi_fakultas TEXT
)
''')
conn.commit()

# Berfungsi untuk menentukan prediksi fakultas dan menyimpan data ke database
def submit_nilai():
    # Mengambil nilai dari entry input
    nama = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())

    # Menentukan prediksi fakultas berdasarkan skor tertinggi
    if biologi > fisika and biologi > inggris:
        prediksi = "Kedokteran"  # Prediksi jika nilai Biologi paling tinggi
    elif fisika > biologi and fisika > inggris:
        prediksi = "Teknik"  # Prediksi jika nilai Fisika paling tinggi
    elif inggris > biologi and inggris > fisika:
        prediksi = "Bahasa"  # Prediksi jika nilai Inggris paling tinggi
    else:
        prediksi = "Tidak dapat ditentukan"  # Prediksi jika ada nilai sama tinggi

    # Masukkan data ke dalam tabel SQLite
    cursor.execute('''
    INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
    VALUES (?, ?, ?, ?, ?)
    ''', (nama, biologi, fisika, inggris, prediksi))
    conn.commit()  # Simpan perubahan ke database

    # Tampilkan pesan informasi
    messagebox.showinfo("Info", f"Data berhasil disimpan! Prediksi fakultas: {prediksi}")

    # Kosongkan kolom entri
    entry_nama.delete(0, tk.END)  # Menghapus input di kolom nama
    entry_biologi.delete(0, tk.END)  # Menghapus input di kolom biologi
    entry_fisika.delete(0, tk.END)  # Menghapus input di kolom fisika
    entry_inggris.delete(0, tk.END)  # Menghapus input di kolom inggris

# Berfungsi untuk menampilkan seluruh data dari tabel
def show_all_data():
    cursor.execute('SELECT * FROM nilai_siswa')  # Perintah SELECT untuk mengambil semua data
    rows = cursor.fetchall()  # Mengambil semua hasil query
    print("Data dalam tabel nilai_siswa:")
    for row in rows:
        print(row)  # Menampilkan setiap baris data

# Membuat jendela utama
root = tk.Tk()
root.title("Input Nilai Siswa")  # Judul window utama

# Membuat dan menempatkan widget
label_nama = tk.Label(root, text="Nama Siswa")  # Label untuk input nama siswa
label_nama.grid(row=0, column=0)
entry_nama = tk.Entry(root)  # Entry field untuk nama siswa
entry_nama.grid(row=0, column=1)

label_biologi = tk.Label(root, text="Nilai Biologi")  # Label untuk input nilai Biologi
label_biologi.grid(row=1, column=0)
entry_biologi = tk.Entry(root)  # Entry field untuk nilai Biologi
entry_biologi.grid(row=1, column=1)

label_fisika = tk.Label(root, text="Nilai Fisika")  # Label untuk input nilai Fisika
label_fisika.grid(row=2, column=0)
entry_fisika = tk.Entry(root)  # Entry field untuk nilai Fisika
entry_fisika.grid(row=2, column=1)

label_inggris = tk.Label(root, text="Nilai Inggris")  # Label untuk input nilai Inggris
label_inggris.grid(row=3, column=0)
entry_inggris = tk.Entry(root)  # Entry field untuk nilai Inggris
entry_inggris.grid(row=3, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_nilai)  # Tombol untuk submit data
submit_button.grid(row=4, column=0, columnspan=2)

# Tombol untuk menampilkan semua data
show_button = tk.Button(root, text="Show All Data", command=show_all_data)  # Tombol untuk menampilkan data
show_button.grid(row=5, column=0, columnspan=2)

# Jalankan perulangan Tkinter
root.mainloop()

# Tutup koneksi database setelah selesai
conn.close()  # Tutup koneksi ke database