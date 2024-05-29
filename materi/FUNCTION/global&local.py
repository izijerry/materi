# Global & locak scope

nama_global = 'bule' # ini variabel global 

#akses variabel global dalam fungsi 
def fungsi1():
    print(f"fungsi menampilkan {nama_global}")

fungsi1()

#akses variebel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

#percabangan 
if True:
    print(f"if menampilkan {nama_global}")


## Variabel local scope 

def fungsi2():
    nama_local = "ucup" #<-- variabel local scope 

fungsi2()
# print(nama_local) #tidak bisa dilakukan 

##contoh 1: penggunaan akses variabel 
def say_otong():
    print(f"hello {nama}")

nama = "otong"
say_otong()

#contoh 2: merubah variabel global 
angka = 0
name = "ucup"

def ubah(nilai_baru, nama_baru):
    global angka    #fungsi ini mendapat akses merubah angka
    global name
    name = nama_baru
    angka = nilai_baru


print(f"sebelum {angka,name}")
ubah(12,"bule")
print(f"sesudah {angka,name}")

#contoh 3: 
angka = 0 

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)