#def positie_laagste_ascii(woord):
#    ascii = 10000000000000000000000
#    for i in range(0, len(woord)):
#        if ord(woord[i]) < ascii:
#            ascii = ord(woord[i])
#    p = chr(ascii)
#    antwoord = woord.find(p)
#    return antwoord
#
#def sorteer(woord):
#    nieuw_woord = ''
#    for i in range(0, len(woord)):
#        ascii = 10000000000000000000000
#        for i in range(0, len(woord)):
#            if ord(woord[i]) < ascii:
#                ascii = ord(woord[i])
#        k = chr(ascii)
#        nieuw_woord += k
#        z = woord.find(k)
#        woord = woord[0:z] + woord[z + 1:]
#    return nieuw_woord
#
#def is_alfabetisch(woord):
#    k = sorteer(woord)
#    if k == woord:
#        return True
#    else:
#        return False

def positie_laagste_ascii(tekst):

    p_laagste = 0
    ord_laagste = ord(tekst[0])

    for i in range(1, len(tekst)):

        ord_huidige = ord(tekst[i])

        if(ord_huidige < ord_laagste):
            p_laagste = i
            ord_laagste = ord_huidige

    return p_laagste

def sorteer(tekst):
    s_tekst = ''

    while len(tekst) > 0:
        i = positie_laagste_ascii(tekst)
        s_tekst += tekst[i]
        tekst = tekst[:i] + tekst[i + 1:]

    return s_tekst

def is_alfabetisch(tekst):
    return tekst == sorteer(tekst)

print(is_alfabetisch('aaaaaaaah'))

