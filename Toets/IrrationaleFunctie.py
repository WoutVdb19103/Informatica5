#invoer
from math import sqrt
x = float(input('Geef een reëel getal x: '))

#bewerking
if x < 2:
    uitkomst = '{:.2f}'.format(x) + ' NOT AN ELEMENT OF dom(f)'
elif x == 2:
    uitkomst = '{:.2f}'.format(x) + ' is nulpunt van f'
else:
    uitkomst = 'f(' + '{:.2f}'.format(x) + ') = ' + str(round(sqrt(x - 2), 2))

#uitvoer
print(uitkomst)
