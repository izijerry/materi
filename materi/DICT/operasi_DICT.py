data_dict = {
    'bul': 'bule',
    'tg':'otong',
    'cp':'ucup',
}

#panjang dict
LENDICT = len(data_dict)

#mengecek key exist atau tidak 
KEY = "cp"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

#mengakeses value(read) dengan get 
print(data_dict.get("cp"))
print(data_dict.get("kiss", "key tidak ditemukan"))

#mengupdate data 
data_dict['cp'] = "ucup jelek"
print(data_dict)

data_dict.update({"adm":"admiral"})#kalau ga ada di add
print(data_dict)

#mendelete data pada dict 
del data_dict["adm"]
print(data_dict)