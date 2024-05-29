# continue, pass, dan break     

# pass -> berfungsi sebagai dummy, tdk akan di eksekusi 

angka = 0 
 

while angka > 5:
    angka += 1
    if angka == 3:
        pass #ini tdk akan di eksekusi
    print(angka)



# continue 

angka = 0 

while angka < 5:
    angka += 1
    print(f"angka sekarang adalah: {angka}")    #aksi 1 

    if angka == 3:
        print("halo")
        continue #akan membuat loop meloncat ke step selanjutnya

    print("heyy")   #aksi 2
   

print("finish")



#break

data_int  = int(input("masukan angka sampaian: "))

angka = 0

while True:
    angka += 1
    print(angka)

    if angka == data_int:
        break

print("finish!!!")