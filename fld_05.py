import random

szamok = []
for x in range(50):
    szamok.append(random.randint(5, 49) * 2 + 1)
    # szamok.append(random.randrange(11, 100, 2))
print(szamok)

i = 0
while i < len(szamok) and szamok[i] != 13: i += 1
if i < len(szamok): print('van benne 13')
else: print('nincs benne 13')