# data yang dimasukan pasti string
#data = input("Masukan data: ")

#print("data = ",data,",type =",type(data))

# jika kita ingin mengambil int, maka
#angka = float(input("masukan angka: "))
#angka = int(input("masukan angka: "))

#print("data = ",angka,",type =",type(angka))



# bagaimana dengan boolean
#biner = bool(int(input("masukan nilai boolean: ")))

#casting ke int terlebih dahulu 

#print("data = ",biner,",type =",type(biner))

while True:
    try:
        angka = int(input("Masukkan angka: "))
        print("Data =", angka, ", type =", type(angka))
        
        ulang = input("Apakah Anda ingin memasukkan angka lagi? (y/n): ").lower()
        if ulang != 'y':
            print("Program selesai.")
            break
    except ValueError:
        print("Input tidak valid, masukkan angka yang benar.")
