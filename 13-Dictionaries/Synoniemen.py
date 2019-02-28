def synoniemen(zin, woordenboek):

    zin = zin.split()

    for i in range(len(zin)):

        if zin[i] in woordenboek:
            zin[i] = woordenboek[zin[i]]

    return ' '.join(zin)



print(synoniemen('knoeien levert stoute leerlingen een straf op',{'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent', 'school': 'troep', 'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}))