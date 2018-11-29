from random import randint
aantal_experimenten = int(input('Aantal experimenten: '))
kop, munt, succes = 0, 0, 0

for i in range(aantal_experimenten):
    kop, munt = 0, 0

    for j in range(3):
        worp = randint(0,2)

        if(not worp):
            kop += 1

    else:
        munt += 1

    if kop == 3:
        succes += 1

print('P(K|K|K) = {:.5f}'.format(succes / aantal_experimenten))