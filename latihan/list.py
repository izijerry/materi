#program list buku
list_buku = []
while True:
    judul = input("judul buku: ")
    penulis = input("penulis buku: ")

    bukuBaru = [judul,penulis]
    list_buku.append(bukuBaru)
    
    print("\n\n","="*10,"data buku","="*10)
    for index,buku in enumerate(list_buku):

        print(f"{index+1}. | {buku[0]} | {buku[1]}")
    print("\n\n","="*20)
    lanjut = input("apakah mau lanjut?(y/n): ")

    if lanjut == "n":
        break

print("PROGRAM SELSAI")


