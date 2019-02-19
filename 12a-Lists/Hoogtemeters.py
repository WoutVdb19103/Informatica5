def hoogtemeters(list):
    new_list = []

    for i in range(len(list) - 1):

        new_list.append(list[i + 1] - list[i])

    return new_list

def dalen_en_stijgen(list):
    negatief = 0
    positief = 0

    for h in list:

        if h < 0:

            negatief += -h

        else:

            positief += h
    new_list = (negatief, positief)

    return new_list

print(hoogtemeters([822, 61, 347, 234, 883, 336]))