from math import sqrt

def binnen_of_buiten(m,c,p):
    #straal : afstand van m tot c
    r = sqrt(pow((m[0] - c[0]), 2) + pow((m[1] - c[1]), 2))

    #afstand van m tot p
    d_mp = sqrt(pow((m[0] - p[0]), 2) + pow((m[1] - p[1]), 2))

    #vergelijken
    if r == d_mp:
        uitk = 'op'

    elif r > d_mp:
        uitk = 'binnen'

    else:
        uitk = 'buiten'

    return uitk, round(d_mp, 4)

print(binnen_of_buiten((0, 0), (1, 1), (-1, -1)))


