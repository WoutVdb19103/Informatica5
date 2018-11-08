#invoer
dv = float(input('Geef de verkeersdichtheid van het vrachtwagenverkeer: '))
vv = int(input('Geef de snelheid van het vrachtwagenverkeer: '))
da = float(input('Geef de verkeersdichtheid van het autoverkeer: '))
va = int(input('Geef de snelheid van het autoverkeer: '))

#extra gegevens
pv = min((vv * dv) / 40, 1)
pa = min((va * da) / 40, 1)

#bewerking
if min(pv, pa) > 0.7:
    code = 'zwart'
elif max(pv, pa) > 0.7 and abs(pa - pv) < 0.2:
    code = 'rood'
elif abs(pv - pa) > 0.7:
    code = 'geel'
else:
    code = 'groen'

#uitvoer
print(code)