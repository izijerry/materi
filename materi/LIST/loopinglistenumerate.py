#looping dari list 

#for loop
print('for loop')
kumupulanAngka = [1,4,2,3,6,7,5,8,9]

for angka in kumupulanAngka:
    print(f"angka: {angka}")

print("\n")
peserta = ["ucup","bule","dadang","diding"]

for nama in peserta:
    print(f"nama: {nama}")

#for loop dan range
print('\nfor loop dan range')
kumpulanangka = [1,4,3,2,7,5,9,10]

panjang = len(kumpulanangka)

for i in range(panjang):
    print(f'angka= {kumpulanangka[i]}')

#while
print('\nwhile loop')
kumpulanangka = [1,4,3,2,7,5,9,10]

panjang = len(kumpulanangka)
i = 0 

while i < panjang:
    print(f"angka = {kumpulanangka[i]}")
    i += 1

#list comprehension
print("\nlist comprehension")
data = ["ucup",1,2,3,"otong"]

[print(f"data = {i}") for i in data] 

#enumerate
print('\nenumerate')
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")