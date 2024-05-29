'''Default argument'''

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):

#contoh 1
def say_hello(nama = "ganteng"):
    '''fungsi dengan default argument'''
    print(f"halo {nama}")

say_hello("bule")
say_hello()

#contoh 2
def sapa_dia(nama,pesan = "apa kabar?"):
    '''fungsi dengan satu input biasa, dan satu default'''
    print(f"halo {nama}, {pesan}")

sapa_dia("ucup","jelek")
sapa_dia("bule")

#contoh 3 
def hitung_pangkat(angka,pangkat=2):
    hasil = angka**pangkat
    return hasil

hasil = hitung_pangkat(angka=5, pangkat=3)
print(hasil)

#contoh 4
def fungsi(input1=1,input2=2,input3=3,input4=4,input5=5):
    hasil = input1 + input2 + input3 + input4 + input5
    return hasil

print(fungsi())
print(fungsi(input2=6))
