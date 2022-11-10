nevek = []
for x in range(10):
    nev = input(f'{x + 1}. név: ')
    if nev == '': break
    else: nevek.append(nev)

########################################
# index = 0                            #
# nev = '-'                            #
# while index < 3 and nev != '':       #
#     nev = input('nev: ')             #
#     if nev != '': nevek.append(nev)  #
#     index += 1                       #
########################################

list.sort(nevek)
print(nevek)