#invoer
n = int(input('Hoeveel getallen? '))
max = int(input('getal: '))
som = max

for i in range(n - 1):
    getal = int(input('Geef een geheel getal: '))
    if i == 0:
        max = getal
    elif getal > max:
        max = getal
    som += getal

#bewerking
gemiddelde = round((som / n ), 2)

#uitvoer
print('Het grootste getal is {} en het gemiddelde is {:.2f}'.format(max, gemiddelde))