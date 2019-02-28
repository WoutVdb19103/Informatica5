def beweeg(tuple, richting):
    a = tuple[0]
    b = tuple[1]

    if richting == '<':
        a -= 1

    elif richting == '>':
        a += 1

    elif richting == 'v':
        b -= 1

    else:
        b += 1

    return (a, b)


def teruggekeerd(list):
    return list[0] == '<' and list[1] == '>' or list[0] == '>' and list[1] == '<' or list[0] == 'v' and list[
        1] == '^' or list[0] == '^' and list[1] == 'v'


def laatste_levende_positie(list):
    a = 0
    c = (0, 0)
    k = 0

    for i in range(len(list) - 1):

        if i < len(list) - 1:

            c = beweeg(c, list[i])

        else:

            if teruggekeerd((list[i], list[i + 1])) is True:

                return (k, c[0], c[1])
        k += 1

    return (k, c[0], c[1])

print(beweeg((-6, -6), '<'))
print(teruggekeerd(['^', 'v']))
print(laatste_levende_positie(['v', '>', 'v', '<', '^', '^']))