#invoer
x = int(input('Geef de windsnelheid: '))

#bewerking
if x <= 118:
    print('geen orkaan')

elif 119 <= x <= 153:
    print('categorie 1')

elif 154 <= x <= 177:
    print('categorie 2')

elif 178 <= x <= 209:
    print('categorie 3')

elif 210 <= x <= 249:
    print('categorie 4')

else:
     print('categorie 5')