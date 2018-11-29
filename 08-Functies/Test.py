from math import sqrt, floor
aantal_gevraagd = int(input('aantal gevraagd: '))
som, aantal, n = 0, 0, 2

while aantal < aantal_gevraagd:
    i = 2

    while i <= floor(sqrt(n)) and n % i != 0:
        i += 1

    if i == floor(sqrt(n)) + 1:
        som, aantal = som + n, aantal + 1
    n += 1

print(som)