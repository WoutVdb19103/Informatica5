def hint(gok, woord):
    output = ''

    while len(output) < len(gok):

        for i in range(0, len(woord)):

            if gok[i] in woord[i]:
                output += gok[i].upper()

            elif gok[i] in woord:
                output += gok[i]

            else:
                output += '.'

    return output