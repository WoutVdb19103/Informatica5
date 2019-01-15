def is_palindroom(woord):
    kaas = True

    if len(woord) == 1:
        kaas = True
    else:
        for i in range(len(woord) // 2):

            if woord[i] == woord[-i - 1] and kaas != False:
                kaas = True

            else:
                kaas = False

    return kaas

