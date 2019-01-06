#invoer
n = int(input('Aantal basen? '))
m, aantal_verschillende, basea, baset, baseg, basec = '', 0, '', '', '', ''

#bewerking
for i in range(n):
    base = input('Welke base? ')

    if base not in m:
        m += base
        aantal_verschillende += 1

        if base == 'A':
            basea += 'A'
        elif base == 'T':
            baset += 'T'
        elif base == 'G':
            baseg += 'G'
        else:
            basec += 'C'

#uitvoer
if aantal_verschillende == 1:
    print('De DNA-keting bevat 1 soort base: ', base)

else:
    print('De DNA-keting bevat' + aantal_verschillende + 'verschillende soorten basen: {} {} {} {}'.format(basea, basec, baseg, baset))