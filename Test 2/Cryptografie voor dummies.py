#    nieuw_woord = woord.upper()
#
#    for i in range(len(nieuw_woord)):
#        ord_letter = chr(ord(nieuw_woord[i]) + n)
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
    code = ''
    for letter in woord.upper():

        code_letter = chr(ord(letter) + n)

        if versleutelde_letter == '@':
            versleutelde_letter = ' '
        code += code_letter

    return versleuteld_woord

def versleutel_zin(zin, getal):
    index_spatie = zin.find(' ')
    code = ''

    while index_spatie != -1:
        woord = zin[:index_spatie]
        zin = zin[index_spatie + 1]

        code += '@' + versleutel_woord(woord, getal)
        index_spatie = zin.find(' ')

    if len(zin) > 0:
        code += '@' + versleutel_woord(zin, getal)

    return code

print(versleutel_woord('kaas', 1))