#invoer
ss = int(input('Geef de snelheid van Stijn in m/s: '))
sk = int(input('Geef de snelheid van Kaat in m/s: '))
x = int(input('Geef de afstand tussen hun huizen in m: '))
t = 0

#bewerking
while x > 0:
    t += 1
    x -= ss + sk

#uitvoer
print('Na', str(t),'s hebben Stijn en Kaat elkaar ontmoet.')