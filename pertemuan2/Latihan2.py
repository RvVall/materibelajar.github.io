


# Program untuk mengonversi nilai angka menjadi nilai huruf

def konversi_nilai(nilai_angka):
    if 80 <= nilai_angka <= 100:
        return 'A'
    elif 70 <= nilai_angka <= 79:
        return 'B'
    elif 50 <= nilai_angka <= 69:
        return 'C'
    elif 30 <= nilai_angka <= 49:
        return 'D'
    elif 0 <= nilai_angka <= 29:
        return 'E'
    else:
        return 'Nilai tidak valid'

#Sebagai Perulangan meminta Input dari user
while True:
    try:
        # Input dari pengguna
        nilai_angka = int(input("Masukkan nilai angka: "))
        
        # Mengonversi dan menampilkan nilai huruf
        nilai_huruf = konversi_nilai(nilai_angka)
        print("Nilai huruf:", nilai_huruf)
        
        # Menanyakan apakah ingin memasukkan nilai lagi
        ulang = input("Apakah Anda ingin memasukkan nilai lagi? (y/n): ").lower()
        if ulang != 'y':
            print("Program selesai.")
            break
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka yang benar.")
