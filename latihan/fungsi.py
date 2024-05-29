'''latihan fungsi'''

import os

def header():
    '''fungsi header'''
    os.system("cls")
    print(f"{"PROGRAM MENGHITUNG LUAS":^40}")
    print(f"{"DAN KELILING PANJANG":^40}")
    print(f"{"-"*40:^40}")

def input_user():
    '''fungsi input user'''
    lebar = int(input("masukan nilai lebar: "))
    panjang = int(input("masukan nilai panjang: "))
    return panjang,lebar

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)

def display(message,value):
    print(f"hasil perhitungan {message} = {value}")

def opsi():
    opsi = int(input("1. hitung luas\n2. hitung keliling\npilih 1,2? "))
    if opsi == 1:
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        display("luas",LUAS)
    elif opsi == 2:
        LEBAR,PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("keliling",KELILING)
    else:
        print("opsi tidak tersedia") 

while True:
    header()
    opsi()

    iscontinue = input("apakah mau lanjut (y/n)? ")
    if iscontinue == "y":
        continue
    elif iscontinue == "n":
        break
print("program selesai, terima kasih")