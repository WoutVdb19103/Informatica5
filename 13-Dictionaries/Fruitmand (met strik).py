def fruitmand_maken(mand):
    mandje = {}

    for i in mand:

            mandje[len(i)] = i

    return mandje

def fruitmand_inpakken(dictionary):
    mandje = []

    for value in dictionary.values():
        mandje.append(value)



    return mandje


print(fruitmand_inpakken({6: 'banaan', 7: 'aardbei', 4: 'peer', 5: 'appel', 3: 'bes', 11: 'sinaasappel', 8: 'framboos'}))
