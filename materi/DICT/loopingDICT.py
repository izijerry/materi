teman_teman = {
    "cup":"ucup",
    "tong":"otong",
    "sep":"asep",
    "dung":"dudung",

}


#looping first try (yg keluar adalah keynya)
for teman in teman_teman:
    print(teman)



#operator untuk mengambil item/iterables
print("=====KEY=====")
keys = teman_teman.keys()
print(f"{keys}\n")

for key in teman_teman.keys():
    print(teman_teman.get(key))

print("=====VALUES=====")
values = teman_teman.values()
print(f"{values}\n")


for value in teman_teman.values():
    print(f"{value}\n")

print("=====ITEM=====")
item = teman_teman.items()
print(f"{item}\n")

for item in teman_teman.items():
    print(f"{item}\n")

for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}\n")