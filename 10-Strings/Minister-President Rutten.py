#spelen met code niet per se efficient
def tel_woorden_dov(zin):
    return len(zin) - len(zin.replace(' ', '')) + 1

#opl Meneer
def tel_woorden(zin):
    lengte = len(zin)
    lengte_z_spaties = len(zin.replace(' ', ''))
    return lengte - lengte_z_spaties + 1


def tel_woorden(zin):

    aantal_spaties = 1

    for letter in zin:
        if letter == ' ':
            aantal_spaties += 1

    return aantal_spaties


print(tel_woorden_dov('Ze weet al welke ze wil.'))