from operator import itemgetter
def bereken_prijs(lijst):
    prijs = 0

    for i in lijst:

            prijs += i[1]

    return prijs

def winkelbriefje(lijst):
    briefje = []

    for i in lijst:

        briefje.append(i[0])

    return briefje

def sorteer(lijst):
    lijst.sort(key = itemgetter(1))

    return lijst



print(winkelbriefje([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))