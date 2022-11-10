import random

kulonbozo_szamok = []

i = 0
lfsz = 0
while i < 50:
    lfsz += 1
    szam = random.randint(10, 99)
    if szam not in kulonbozo_szamok:
        kulonbozo_szamok.append(szam)
        i += 1
list.sort(kulonbozo_szamok)
print(kulonbozo_szamok)
print(f'számok száma: {len(kulonbozo_szamok)}')
print(f'lefutások száma: {lfsz}')