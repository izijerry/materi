#merubah semua ke upper
nama = "bule"
nama = nama.upper()
print('nama saya = ' + nama )

#merubah semua ke lower
nama = "BULE"
nama = nama.lower()
print('nama saya = ' + nama )

# pengecekan dengan isX method 

# contoh pengecekan lower case
nama = "bule"
cek = nama.islower()
print(str(cek))

# contoh pengeceupper case
nama = "bule"
cek = nama.isupper()
print(str(cek))

# isalpha()  utk mengecek semua huruf 
# isalnum()  huruf dan angka
# isdecimal() angka saja
# isspace()  spasi, tabv, newline \n
# istitle()  semua kata dimulai dari huruf besar

# alokasi karakter rjust(), ljust() center()

kanan = "kanan".rjust(10)
print(kanan)

kiri = "kiri".ljust(10)
print(kiri)

tengah = "tengah".center(10,"#")
print(tengah)
# menghilangkan
tengah = tengah.strip("#")
print(tengah)

#kasih koma
angka = 2000000
format_str = (f'jutaan = {angka:,}')
print(format_str)

#tampilin +-
angkaminus = -10 
angkaplus = 10
format_minus = f"minus = {angkaminus:+d}"
format_plus = f"minus = {angkaplus:+d}"

print(format_minus, format_plus)

#persen
persen = 0.123
format_persen = f"persen = {persen:%}"
print(format_persen)

# melakukan operasi matematika dalam placeholder
harga = 750999
barang = 25

format_string = f"harga total: Rp{barang*harga:,}"
print(format_string)

#format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadecimal = f"hexadecimal = {hex(angka)}"

print(format_binary, format_hexadecimal, format_octal)