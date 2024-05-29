#conditional + input + str


usia = input('masukan umur anda: ')
# == sama dengan
# >  lebih dari
# <  kurang dari 
# !=  tdk sama dengan
# >= lebih dari sama dengan 
# <= kurang dari sama dengan 

#if usia == 20: 
#    print('bener')
#else:
#    print('salah')

if usia >= str(13) and usia <= str(18):
    print('remaja')
elif usia >= str(1) and usia <= str(12):
    print('bocil')
else: 
    print('tua')
