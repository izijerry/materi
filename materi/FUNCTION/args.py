'''*args'''

#memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("bule",170,65)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["ucup",100,100])

#menggunakan args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("bule",170,70)

#studi kasus 

def tambah(*data):
    output= 0 
    for angka in data:
        output += angka 

    return output

hasil = tambah(1,2,3,4,5)
print(f"hasil {hasil}")

hasil = tambah(6,10,3,6,8)
print(f"hasil {hasil}")
