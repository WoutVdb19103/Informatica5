kaart = {'Brugge': {'Gent', 'Antwerpen'}, 'Kortrijk': {'Gent'}, 'Gent': {'Antwerpen', 'Kortrijk', 'Brugge'}, 'Antwerpen': {'Gent', 'Brussel', 'Brugge'}, 'Brussel': {'Hasselt', 'Antwerpen'}, 'Hasselt': {'Brussel'}}

def bestaat_weg(stad1, stad2, kaart):
    return stad1 in kaart[stad2] and stad2 in kaart[stad1]


def geen_dubbelburen(stad1, stad2, kaart):
    buren = set()

    #allemaal gekke union dingen en difference
    for stad in kaart[stad1] or stad in kaart[stad2]:
        buren.add(stad)

    if stad1 in buren or stad2 in buren:
        buren.remove(stad1)
        buren.remove(stad2)

    if stad in kaart[stad1] and stad in kaart[stad2]:
        buren.remove(stad)

    return buren


def bereikbaarheid_meest_afgelegen_stad(kaart):
    steden = set()

    for value in kaart.values():
        steden.add(len(value))

    afgelegen = min(steden)

    return afgelegen


def bestaat_route(steden, kaart):
    ja = 0
    # best while lus hier
    for i in range(0, len(steden) - 1):
        if steden[i + 1] in kaart[steden[i]]:
            ja += 1

    return ja == len(steden) - 1

print(geen_dubbelburen('Antwerpen', 'Kortrijk', kaart))