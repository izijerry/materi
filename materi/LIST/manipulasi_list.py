#index    0(-3)   1(-2)    2(-1)
data = ['otong', 'ucup', 'dudung']

#mengambil data dari list 
data0 = data[0]
print(f'data pertama adalah: {data0}\n')

data_terakhir = data[-1]
print(f'data terakhir adalah: {data_terakhir}\n')


#mengambil data dari info list
panjangdata = len(data)
print(f"panjang data adalah: {panjangdata}")

## manipulasi data list

#menambahkan item pada list sesuai posisi
print(f'data sebelum ditambah: {data}')
            #posisi #item
data.insert(2,"bule")
print(f"data sesudah ditambah: \n{data}")

#menambah di akhir list
data.append("buleganteng")
print(f'data ditambah lagi: \n {data}')

#menambah list dengan list 
data_baru = ["ujang",'usep','dadang']
data.extend(data_baru)
print(f"data gabungan: \n {data}")

#merubah data
#ubah data 2 menjadi trevor
data[2] = "trevor"
print(f"data ubah = \n {data}")

#meremove data 
data.remove("ujang")
print(f"data remove = \n {data}")

#meremove data paling belakang
data.pop()
print(f"data akhir = \n {data}")
