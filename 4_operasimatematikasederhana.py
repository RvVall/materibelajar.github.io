a = 10
b = 3
penjumlahan = a + b
pengurangan = a - b
perkalian = a * b
pembagian = a / b
pembagian_bulat = a // b
modulus = a % b
pangkat = a ** b

print("Penjumlahan:", penjumlahan)
print("Pengurangan:", pengurangan)
print("Perkalian:", perkalian)
print("Pembagian:", pembagian)
print("Pembagian Bulat:", pembagian_bulat)
print("Modulus:", modulus)
print("Pangkat:", pangkat)

# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

# prioritas operasi, operational precedence
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z 
print('(',x,'+',y,') *',z,'=',hasil)