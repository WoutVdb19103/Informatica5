def gift_inschrijven(klas, giften):
    if klas[0] in giften:
        giften[klas[0]] += klas[1]

    else:
        giften[klas[0]] = klas[1]

    return giften


print(gift_inschrijven(('5IN', 73.81),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 232.48}))