teman_teman = {
    'bul': 'bule',
    'tg':'otong',
    'cp':'ucup',
    'sep':'asep',
    'dung':'dudung'
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman['bul'] = "bule gantengg abiezzz"

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

#pop dictionary (berdasarkan key)
dataASEP = friends.pop("sep")
print(f"data asep: {dataASEP}\n")
print(f"data friends: {friends}\n")

#popitem  dictionary (yang terakhir aja)
dataTerakhir = friends.popitem()
print(f"data terakhir: {dataTerakhir}\n")
print(f"data friends: {friends}\n")