#def ontdubbelen(woord):
#    nieuw_woord = ''
#
#    for letter in woord:
#        if letter == woord[woord.find(letter) + 1]:
#           woord = woord[:woord.find(letter) - 1] + woord[woord.find(letter) + 1:]
#
#    return woord
#
#print(ontdubbelen('kaass'))


def ontdubbelen(woord):
    nieuw_woord = woord[0]

    for i in range(1, len(woord)):

        if woord[i] != woord[i - 1]:
            nieuw_woord += woord[i]

    return nieuw_woord

print(ontdubbelen('kaassseeennn'))