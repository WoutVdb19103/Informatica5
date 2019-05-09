# bestaat_weg: de eerste parameter is de dictionary met de wegenkaart. De tweede en derde parameter zijn twee steden.
# Indien beide steden rechtstreeks verbonden zijn door een weg, dan geeft de functie True terug. In het andere geval False.
#
# geen_dubbelburen: de eerste parameter is de dictionary met de wegenkaart. De tweede en derde parameter zijn twee steden.
# De functie geeft een set steden terug die rechtstreeks verbonden zijn met een van de twee gegeven steden maar niet met alle twee.
#
# bereikbaarheid_meest_afgelegen_stad: berekent met hoeveel steden de meest onbereikbare stad of steden rechtstreeks verbonden zijn.
# De enige parameter is de dictionary met de wegenkaart.
#
# bestaat_route: de tweede parameter is de dictionary met de wegenkaart. De eerste parameter is een lijst van steden.
# De functie geeft True terug indien alle opeenvolgende steden in de lijst rechtstreeks verbonden zijn met een weg. In het andere geval laat je False teruggeven.
kaart = {'Brugge': {'Gent', 'Antwerpen'}, 'Kortrijk': {'Gent'}, 'Gent': {'Antwerpen', 'Kortrijk', 'Brugge'}, 'Antwerpen': {'Gent', 'Brussel', 'Brugge'}, 'Brussel': {'Hasselt', 'Antwerpen'}, 'Hasselt': {'Brussel'}}


def bestaat_weg(stad1, stad2, kaart):
    return stad1 in kaart[stad2] and stad2 in kaart[stad1]


def geen_dubbelburen(stad1, stad2, kaart):
    buren = set()

    for stad in kaart:
        if stad1 in kaart[stad] and stad2 not in kaart[stad] or stad2 in kaart[stad] and stad1 not in kaart[stad]:
            buren.add(stad)

    if stad1 in buren or stad2 in buren:
        buren.remove(stad1)
        buren.remove(stad2)

    return buren


def bereikbaarheid_meest_afgelegen_stad(kaart):
    steden = set()

    for value in kaart.values():
        steden.add(len(value))

    afgelegen = min(steden)

    return afgelegen


def bestaat_route(steden, kaart):
    ja = 0
    for i in range(0, len(steden) - 1):
        if steden[i + 1] in kaart[steden[i]]:
            ja += 1

    return ja == len(steden) - 1

