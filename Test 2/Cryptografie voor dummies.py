#    nieuw_woord = woord.upper()
#
#    for i in range(len(nieuw_woord)):
#        ord_letter = ord(nieuw_woord[i]) + n
#        nieuw_woord = nieuw_woord.replace(nieuw_woord[i],chr(ord_letter))
#
#    return nieuw_woord
#
#def versleutel_zin(zin, n):
#    kaas = 0
#    while kaas < 1:
#        if ' ' in zin:
#            woord = zin[:zin.find(' ') + 1]
#            nieuw_woord_zin = versleutel_woord(woord, n) + '@'
#            zin = zin.replace(woord, nieuw_woord_zin)
#
#
#        else:
#            kaas += 1

#    return zin

#print(versleutel_zin('ik eet kaas', 6))

def versleutel_woord(woord, n):

    versleuteld_woord = ''

    woord = woord.upper()

    for letter in woord:

        versleutelde_letter = chr(ord(letter) + n)

        if versleutelde_letter == '@':
            versleutelde_letter = ' '

        versleuteld_woord += versleutelde_letter

    return versleuteld_woord

print(versleutel_woord('kaas', 1))