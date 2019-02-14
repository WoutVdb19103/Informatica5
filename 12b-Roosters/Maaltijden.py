def dagprijs(lijst):
    prijs = 0

    for i in lijst:

        if i == 'middagmaal':

            prijs += 5.3 * lijst[lijst.index(i) + 1]

        elif i == 'vieruurtje':

            prijs += 2.3 * lijst[lijst.index(i) + 1]

        elif i == 'soep':

            prijs += 1.7 * lijst[lijst.index(i) + 1]

    return prijs

def weekprijs(lijst):
    prijs = 0

    for i in lijst:

        prijs += dagprijs(i)

    return prijs

print(weekprijs((('middagmaal', 2, 'soep', 2, 'vieruurtje', 2), ('middagmaal', 1, 'soep', 1), ('soep', 3, 'vieruurtje', 3), ('middagmaal', 3, 'soep', 1), ('middagmaal', 3, 'soep', 3, 'vieruurtje', 1))))
