# Meminta input nama dari pengguna
nama = input("Masukkan nama Anda: ")

# Meminta input umur dari pengguna
umur = int(input("Masukkan umur Anda: "))

# Menghitung tahun kelahiran
tahun_sekarang = 2024
tahun_lahir = tahun_sekarang - umur

# Mencetak pesan sapaan dan tahun kelahiran
print(f"Halo, {nama}! Anda lahir pada tahun {tahun_lahir}.")


print("Halo, "+ nama + "! Anda Lahir pada tahun " + str (tahun_lahir)+".")