from time import sleep  

def penambahan():
        while True:
                x = int(input('masukan angka pertama: '))
                y = int(input('masukan angka kedua: '))
                hasil = x + y
                print(hasil)
                exit = input('kembali ke menu utama [y/n]? ')
                if exit == 'y':
                       menu()
                if exit == 'n':
                       penambahan()
                else:
                       print('pilihan tdk tersedia!!!')
        

def pengurangan():
         while True:
                x = int(input('masukan angka pertama: '))
                y = int(input('masukan angka kedua: '))
                hasil = x - y
                print(hasil)
                exit = input('kembali ke menu utama [y/n]? ')
                if exit == 'y':
                       menu()
                if exit == 'n':
                       pengurangan()
                else:
                       print('pilihan tdk tersedia!!!')
def perkalian():
        while True:
                x = int(input('masukan angka pertama: '))
                y = int(input('masukan angka kedua: '))
                hasil = x * y
                print(hasil)
                exit = input('kembali ke menu utama [y/n]? ')
                if exit == 'y':
                       menu()
                if exit == 'n':
                       perkalian()
                else:
                       print('pilihan tdk tersedia!!!')
def pembagian():
        while True:
                x = int(input('masukan angka pertama: '))
                y = int(input('masukan angka kedua: '))
                hasil = x / y
                print(hasil)
                exit = input('kembali ke menu utama [y/n]? ')
                if exit == 'y':
                       menu()
                if exit == 'n':
                       pembagian()
                else:
                       print('pilihan tdk tersedia!!!')

def menu():        
    menu = int(input('menu\n1. penambahan\n2. pengurangan\n3. perkalian\n4. pembagian\n5. exit program\n\nsiliahkan pilih: '))
    if menu == 1:
           penambahan()
    elif menu == 2:
           pengurangan()
    elif menu == 3:
           perkalian()
    elif menu == 4:
           pembagian()
    elif menu == 5:
           exit()
    else:
           print('silahkan pilih menu yg tersedia')    

        

def exit():
       print('program akan dihentikan')
       sleep(1)
       print('3...')
       sleep(1)
       print('2...')
       sleep(1)
       print('1...')
       sleep(1)
       print('program berhasil dihentikan')
       
def welcome_massage():
       title = 'KALKULATOR'
       style = "=" * (len(title) + 6 )
       print(style)
       print(f"== {title} ==")
       print(style)    

def program():
       welcome_massage()
       menu()

program()


