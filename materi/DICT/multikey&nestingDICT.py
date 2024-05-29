import datetime

mahasiswa1 = {
    'nama' : 'bule',
    'nim' : '0123123',
    'sks_lulus' : '130',
    'beasiswa' : False,
    'lahir' : datetime.datetime(2001,3,13)

}


mahasiswa2 = {
    'nama' : 'ucup',
    'nim' : '0123125',
    'sks_lulus' : '140',
    'beasiswa' : True,
    'lahir' : datetime.datetime(2004,2,20)

}


mahasiswa3 = {
    'nama' : 'otong',
    'nim' : '0123127',
    'sks_lulus' : '100',
    'beasiswa' : False,
    'lahir' : datetime.datetime(1996,6,26)

}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}

print(f"{'KEY':<6} {'NAMA':<17}{'SKS':<5}{'BEASISWA':<9}{'LAHIR':<10}")
print('-'*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')
    print(f"{KEY:<6} {NAMA:<17}{SKS:<5}{BEASISWA:^9}{LAHIR:<10}")