def dubbels(list):
    list2 = []

    for item in list:

        if list.count(item) > 1 and item not in list2:

            list2.append(item)

    return list2

