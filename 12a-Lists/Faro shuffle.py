def nieuw_kaartspel(kleuren, waarden):
    kaartspel = []
    a = 0
    b = 0
    while a < len(kleuren):
        while b < len(waarden):
            kaartspel.append(kleuren[a] + waarden[b])

            b += 1
        a += 1
        b = 0

    return kaartspel


def splits_kaartspel(kaarten):
    return (kaarten[0:len(kaarten) // 2], kaarten[len(kaarten) // 2:])


def faro_shuffle(k1, k2):
    shuffle = []
    a = 0
    if len(k1) == len(k2):
        while a < len(k1):
            shuffle.append(k1[a])
            shuffle.append(k2[a])
            a += 1
    else:
        while a < len(k1):
            shuffle.append(k1[a])
            shuffle.append(k2[a])
            a += 1
        shuffle.append(k2[a])

    return shuffle
