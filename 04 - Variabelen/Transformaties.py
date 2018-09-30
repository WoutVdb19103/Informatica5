#gegeven
a = float(input('Geef de waarde voor a: '))
b = float(input('Geef de waarde voor b: '))
x = 'x'
fx = '2(x-3)^2 + 4'


#berekening

gx = '2' + '(x - ' + str(int(3 + a)) + ')^2' + ' + ' + str(int(4 + b))

#uitvoer
print('f(x) = ' + fx)
resultaat = (gx)
print('g(x) = ' + str(resultaat))