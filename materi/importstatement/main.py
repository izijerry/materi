#import 

#fungsi adalah untuk mengambil program dari external .py

#1. untuk menyambung program dari external 
import program_print
import program_hello
#2. import dengan data 
import ucup
import bule

#data ada di namespace variable
print(ucup.data)
print(bule.data)

#3. import dengan fungsi
import matematika

hasil = matematika.tambah(4,5)
print(hasil)


