import random

tippek = []

db = 0
while db < 7:
    tipp = int(input(f'{db + 1}. tipp: '))
    if tipp < 1 or tipp > 35:
        print('érvénytelen tipp!')
    elif tipp not in tippek:
        tippek.append(tipp)
        db += 1
    else: print('ez már volt!')

kezi_huzas = []
db = 0
while db < 7:
    szam = random.randint(1, 35)
    if szam not in kezi_huzas:
        kezi_huzas.append(szam)
        db += 1

gepi_huzas = []
db = 0
while db < 7:
    szam = random.randint(1, 35)
    if szam not in gepi_huzas:
        gepi_huzas.append(szam)
        db += 1

list.sort(tippek)
list.sort(kezi_huzas)
list.sort(gepi_huzas)

print(f'tippek: {tippek}')
print(f'kézi húzás számai: {kezi_huzas}')
print(f'gépi húzás számai: {gepi_huzas}')

kezi_talalat = 0
gepi_talalat = 0

for tipp in tippek:
    if tipp in kezi_huzas: kezi_talalat += 1
    if tipp in gepi_huzas: gepi_talalat += 1

print(f'kézi találatok száma: {kezi_talalat}')
print(f'gépi találatok száma: {gepi_talalat}')
