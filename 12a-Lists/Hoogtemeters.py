def hoogtemeters(list):
    new_list = []
    for h in list:

        while list.index(h) + 2 != len(list):

            new_list += [list[h + 1]]

    return list


print(hoogtemeters([822, 61, 347, 234, 883, 336]))