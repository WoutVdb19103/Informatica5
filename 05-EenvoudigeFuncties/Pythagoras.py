from math import sqrt
#invoer
a = round(float(input('Geef een getal a groter dan 0: ')), 2)
b = round(float(input('Geef een getal b groter dan 0: ')), 2)

#bewerking
c = '{:4.2f}'.format(sqrt((a ** 2) + (b ** 2)))

#uitvoer
print('In een rechthoekige driehoek met rechthoekszijden a = ' + str(a) + ' en b = ' + str(b) + ' is de schuine zijde ' + str(c))