#invoer
x = float(input('Geef x: '))
y = float(input('Geef y: '))

#gegevens
linkerlid = abs(abs(x) - abs(y))
rechterlid = abs(x - y)

#oplossing
print('{:.4f} \N{LESS-THAN OR EQUAL TO} {:.4f}'.format(linkerlid, rechterlid))

