'''Fungsi dengan kembalian (return)'''

# Template
# def nama_fungsi(argument):
#     badan fungsi 
#     return output

def kuadrat(angka):
    kuadrat = angka**2
    return kuadrat

y = kuadrat(3)
print(y)

print(kuadrat(10))

z = 10 + kuadrat(17)
print(z)

def tambah(angka1,angka2):
    return angka1 + angka2

a = tambah(1,7)
print(a)

def operasi_matematika(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    bagi = angka1 / angka2
    kali = angka1 * angka2

    return tambah,kurang,bagi,kali

k,l,m,n, = operasi_matematika(2,7)
print(f"hasil tambah: {k}")
print(f"hasil kurang: {l}")
print(f"hasil bagi: {m}")
print(f"hasil kali: {n}")