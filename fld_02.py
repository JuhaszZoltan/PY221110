# lista, 20db [50, 150] közötti rnd számmal
# rendezni (ezt majd mutatom)
# számok összege
# számok átlaga
# 0ra végződők száma

import random

szamok = []
for x in range(20):
    szamok.append(random.randint(50, 150))
print(f'eredeti:  {szamok}')
list.sort(szamok)
# ha csökkenőben kell, akkor még +: list.reverse(szamok)
print(f'rendezve: {szamok}')

osszeg = 0
nulla_db = 0
for szam in szamok:
    if szam % 10 == 0: nulla_db += 1
    osszeg += szam

print(f'számok összege: {osszeg}')
print(f'számok átlaga: {osszeg/len(szamok)}')
print(f'nullára végződők száma: {nulla_db}')