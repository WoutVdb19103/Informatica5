#invoer
prijs = float('{:.2f}'.format(float(input('Geef de prijs: '))))
totaal = prijs

#bewerking
while prijs > 0:
    prijs = float('{:.2f}'.format(float(input('Geef de prijs: '))))
    totaal += prijs
#uitvoer
print('{} {:.2f}'.format('De totale prijs is €', totaal))



