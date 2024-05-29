# 1. menyambung string (concatenate)
namaDepan = "budi"
namaBelakang = "dermawan"
namaLengkap = namaDepan + " " + namaBelakang
print(namaLengkap)

# 2. menghitung panjang string
panjang = len(namaLengkap)
print(f"panjang nama: {panjang}")

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string 

b = "b"
status = b in namaLengkap
print(b + " ada di " + namaLengkap + " = " + str(status))

B = "B"
status = B in namaLengkap
print(B + " ada di " + namaLengkap + " = " + str(status))

b = "b"
status = b not in namaLengkap
print(b + " tdk ada di " + namaLengkap + " = " + str(status))

# mengulang string 
print("ha" * 10 )
print(10 * "ha")

# indexing 
print(f"index ke 0: {namaLengkap[0]}")
print(f"index ke 5: {namaLengkap[5]}")
print(f"index ke -1: {namaLengkap[-1]}")
print(f"index ke 0:8: {namaLengkap[0:8]}")
print(f"index ke 0,2,4,6,8,10: {namaLengkap[0:11:2]}")

# item paling kecil 
print("paling kecil: " + min(namaLengkap))
print("paling besar: " + max(namaLengkap))

ascii_code = ord("2")
print("ascii code untuk 2: " + str(ascii_code)   )
data = 120 
print("char code untuk 120: " + chr(data)   )


# 4. operator dalam bentuk method 
data = "cao ni ma leee lanciao "
jumlah = data.count("e")
print(f"jumlah e pada {data} = {jumlah}" )

