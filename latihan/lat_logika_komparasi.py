input_user = float(input('masukan angka kurang dari 3 atau lebih besar dari 10 = '))

kurangdari = (input_user < 3)
lebihdari  = (input_user > 10)
benar = kurangdari or lebihdari

print(benar)


input_user = float(input('masukan angka lebih besar dari 3 dan kurang dari 10 = '))

kurangdari = (input_user < 10)
lebihdari  = (input_user > 3)
benar = kurangdari and lebihdari

print(benar)


# ++++++0---------5+++++++8---------11+++++++
input_user = float(input(print('masukan angka kurang dari dari 0 dan lebih besar dari 5 dan kurang dari 8 dan lebih besar dari 11:  ')))
x = input_user < 0 or input_user > 5
y = input_user < 8 or input_user > 11
hasil = x and y
print(hasil)
