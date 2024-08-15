import mysql.connector

# If dan Else Statement

# 1. if nya
# 2. kondisinya
# 3. aksinya

nama = input("Siapa nama anda? ")

# program sebelumnya
# if kondisi: aksi
# program selanjutnya

# 1. program if inline
# if nama=="Rivaldy" : print("Kamu Yang Semangatt Yah Belajarnya!!!!")
# print(f"Terima kasih {nama}")

# 2. program if indentation

# if nama=="Rivaldy:
# 	print("Kamu Yang Semangatt Yah Belajarnya!")
# 	print("Semangat Terus!")
# print(f"Terima kasih {nama}")

# 3. Else Statement

if nama=="Rivaldy":
	print("hai Rivaldy, Semangatt Belajarnya!")
else:
	print("Kamu Bukan Rivaldy Kita Tidak Kenal :(")

print("\nakhir dari program")