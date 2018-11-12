#invoer
n = int(input('Hoeveel getallen? '))
max = 0
som = 0

for i in range(n):
    getal = int(input('Geef een geheel getal: '))
    if i == 0:
        max = getal
    elif getal > max:
        max = getal
    som += getal

#bewerking
gemiddelde = round((som / n ), 2)

#uitvoer
print('{} {:d} {} {:.2f}'.format('Het grootste getal is', max, 'en het gemiddelde is', gemiddelde))



