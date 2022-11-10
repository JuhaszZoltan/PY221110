# \\pdc\Diakkaptar\Juhász Zoltán\GYAKORLO FELADATOK

# létrehozunk egy listát, és elhelyezünk benne 5 nevet:
nevek = ['Adél', 'Béla', 'Cecil', 'Dezső', 'Erika']

# kiírjuk a neveket, egymás alá
# for nev in nevek: print(f'{nev}')

# létrehozunk egy üres listát a magasságoknak
magassagok = []
# csinálunk egy ciklust, ami annyiszor fut le, ahány név van a korábbi listában
# a ciklusmagváltozó (az <i>) felveszi a nevek lista indexeinek értékeit (0, 1, ... 4)
for i in range(len(nevek)):
    # hozzáadunk a magasságokhoz egy számot, amit a billentyűzetről kérünk be a felhasználótól
    # minden szám tárolása előtt kiírjuk a nevek listájának azonos indexű elemét
    magassagok.append(int(input(f'{nevek[i]} magassága: ')))

ossz_magassag = 0
for magassag in magassagok:
    ossz_magassag += magassag
print(f'átlagmagasság: {ossz_magassag/len(magassagok)}')

# nem, ezt MÉG nem kell "tudni":
for i in range(len(magassagok) - 1):
    for j in range(i + 1, len(magassagok)):
        if magassagok[i] > magassagok[j]:
            ms = magassagok[i]
            ns = nevek[i]
            magassagok[i] = magassagok[j]
            nevek[i] = nevek[j]
            magassagok[j] = ms
            nevek[j] = ns
for i in range(len(nevek)):
    print(f'{nevek[i]}: {magassagok[i]}')