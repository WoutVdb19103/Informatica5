def kleur_toevoegen(list, kleur):
    if kleur == 'rood':
        list[0] += 1

    elif kleur == 'groen':
        list[1] += 1

    else:
        list[2] += 1

    return list

def is_wit(list):
    return list[0] == list[1] == list[2]

def verf_verzamelen(list):
    aantal = 0
    wit = 0
    r = 0
    g = 0
    b = 0
    for i in range(len(list)):
        while wit == 0:
            if r == g == b != 0:
                wit += i
            elif list[i] == 'rood' :
                r += 1
            elif list[i] == 'groen':
                g += 1
            elif list[i] == 'blauw':
                b += 1
            elif i == len(list) - 1 and wit == 0:
                return None
    return (wit, [r, g, b])





print(verf_verzamelen(['groen', 'groen', 'rood', 'groen', 'rood', 'groen', 'groen', 'rood', 'blauw', 'groen', 'groen', 'blauw', 'blauw', 'rood', 'rood', 'rood', 'blauw', 'rood']))
print(verf_verzamelen(['blauw', 'rood', 'groen', 'blauw', 'groen', 'rood', 'blauw', 'rood', 'blauw', 'rood', 'rood', 'blauw', 'blauw', 'rood', 'groen', 'rood', 'groen']))
