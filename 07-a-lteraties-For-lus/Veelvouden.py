#invoer
r = int(input('Geef een natuurlijk getal groter dan 0 en kleiner dan 100: '))
som_veelvouden = 0

#overloop alle veelvouden van r
for i in range(r, 101, r):
    som_veelvouden += i

#uitvoer
print(som_veelvouden)
