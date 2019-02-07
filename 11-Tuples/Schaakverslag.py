def geldige_zet(zet):
    mes = False

    #controleren of index 0 in K,L...
    if len(zet) == 3 and zet[0] in 'KDTLP' and zet[1] in 'abcdefgh' and zet[2] in '12345678':
        mes = True

    elif len(zet) == 2 and zet[0] in 'abcdefgh' and zet[1] in '12345678':
        mes = True

    return mes


def geldige_zetten(zetten):

    i = 0

    while i < len(zetten) and geldige_zet(zetten[i]):
        i += 1

    return i >= len(zetten)


print(geldige_zetten(('Df6', 'Tf2', 'Db6', 'b1', 'g7', 'Pb6', 'e2', 'g6')))
