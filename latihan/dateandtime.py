import datetime as dt
print("masukan tanggal lahir anda!!!\n")
tanggal = int(input("masukan tanggal: "))
bulan = int(input("masukan bulan: "))
tahun = int(input("masukan tahun: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(tanggal_lahir)
print(f"\nharinya adalah: {tanggal_lahir:%A}")


hariIni = dt.date.today()
print(f"hari ini adalah: {hariIni}")

umur_hari = hariIni - tanggal_lahir  
umur_tahun = umur_hari.days // 365
bulan_sisa = (umur_hari.days % 365) // 30
print(f"umur anda adalah: {umur_tahun} tahun, {bulan_sisa} bulan")
