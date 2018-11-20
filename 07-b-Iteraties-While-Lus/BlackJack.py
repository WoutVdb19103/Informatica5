#invoer
kaart = int(input('Geef kaart: (1-11): '))
totaal = 0

#bewerking
while kaart > 0 and kaart + totaal < 21:
    totaal += kaart
    kaart = int(input('Geef een nieuwe kaart: '))
if kaart + totaal == 21:
    uitkomst = 'Gewonnen!'
elif kaart + totaal < 21:
    uitkomst = 'Voorzichtig gespeeld ({})'.format(totaal + kaart)
else:
    uitkomst = 'Verbrand ({})'.format(totaal + kaart)

#uitvoer
print(uitkomst)