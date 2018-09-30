#gegeven
bedrag = int(input('Geef het bedrag: '))
r1 = bedrag // 100
r2 = (bedrag - (r1 * 100)) // 50
r3 = (bedrag - (r2 * 50) - (r1 * 100)) // 20
r4 = (bedrag - (r3 * 20) - (r2 * 50) - (r1 * 100)) // 10
r5 = (bedrag - (r4 * 10) - (r3 * 20) - (r2 * 50) - (r1 * 100)) // 5
r6 = (bedrag - (r5 * 5) - (r4 * 10) - (r3 * 20) - (r2 * 50) - (r1 * 100)) // 2
r7 = (bedrag - (r6 * 2) - (r5 * 5) - (r4 * 10) - (r3 * 20) - (r2 * 50) - (r1 * 100)) // 1

#berekening
resultaat = int(r1 + r2 + r3 + r4 + r5 + r6 + r7)

print(str(bedrag) + ' cent kan je omwisselen in ' + str(resultaat) + ' muntstukken')
