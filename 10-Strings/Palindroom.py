def palindroom(woord):

    return woord == woord[::-1]

    #i = 0

    #while woord[i] == woord[-i -1] and i < len(woord) // 2:
     #   i += 1

    #!!! belangrijk !!!
    #return i == (len(woord) // 2)

print(palindroom(10000000000 * 'a'))