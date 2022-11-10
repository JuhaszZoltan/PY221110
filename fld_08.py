atutalasok = []

for x in range(12):
    atutalasok.append(int(input(f'{x + 1}. napi átutalások száma: ')))

sm = 0
for atutalas in atutalasok:
    sm += atutalas
avg = sm / len(atutalasok)
c = 0
for atutalas in atutalasok:
    if atutalas > avg: c += 1
print(f'átlagos átutalás-szám a 12 nap alatt: {round(avg, 2)}')
print(f'napok száma, ahol az átutalások száma meghaladta az átlagot: {c}')