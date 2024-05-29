'''fungsi dengan argumen (input)'''

# Template
# def nama_fungsi(argument):
#     badan fungsi

def helloWorld(nama):
    '''fungsi hello world menerima input dengan variable nama'''
    print(f"selamat datang {nama}")


helloWorld("ucup")


#program tambah
def tambah(angka_1,angka_2):
    '''Fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(3,8)


def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")

anggota = ['ucup','otong','asep','bule']

say_hi(anggota)
