import sains.matematika
from sains import fisika
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1,7,8,3)
print(f"hasil tambah darai package adalah = {hasil_tambah}")

gaya = fisika.gaya(70,5)
print(f"gaya adalah = {gaya}")

gaya = force(70,5)
print(f"gaya adalah = {gaya}")
