def positie_laagste_ascii(woord):
    ascii = 10000000000000000000000
    for i in range(0, len(woord)):
        if ord(woord[i]) < ascii:
            ascii = ord(woord[i])
    p = chr(ascii)
    antwoord = woord.find(p)
    return antwoord

def sorteer(woord):
    nieuw_woord = ''
    for i in range(0, len(woord)):
        ascii = 10000000000000000000000
        for i in range(0, len(woord)):
            if ord(woord[i]) < ascii:
                ascii = ord(woord[i])
        k = chr(ascii)
        nieuw_woord += k
        z = woord.find(k)
        woord = woord[0:z] + woord[z + 1:]
    return nieuw_woord

def is_alfabetisch(woord):
    k = sorteer(woord)
    if k == woord:
        return True
    else:
        return False
