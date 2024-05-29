# user bisa bayar hutang jika saldo dia cukup atau lebih utk membayar 
# user tdk akan bisa membayar jika saldo kurang 

saldo_awal = 5000 #int  
deposit = int(input('berapa mau depositnya: ')) #str
hutang = 50000

saldo_total = int(saldo_awal) + int(deposit)

hasil = int(saldo_total) - int(hutang)

if deposit >= 50000:
    print('hutang anda lunas, saldo anda sisa: ' + str(hasil))
else:
    print('saldo anda sebanyak ' + str(saldo_total))




