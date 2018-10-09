from math import sqrt

#invoer
a = float(input('Geef een getal a groter dan 0: '))
b = float(input('Geef een getal b groter dan 0: '))

#bewerking
c = float(sqrt((a ** 2) + (b ** 2)))

#uitvoer
print('In een rechthoekige driehoek met rechthoekszijden a = ' + str(round(a, 2)) + ' en b = ' + str(round(b, 2)) + ' is de schuine zijde ' + str(round(c, 2)))