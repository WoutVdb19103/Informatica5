def ik_heb_gemoord(list, moordenaar):
    if len(list) == 1:
        x = list[0]
    elif list.index(moordenaar) + 1 >= len(list):
        x = list[1]
        list.pop(0)
    elif list.index(moordenaar) + 2 >= len(list):
        x = list[0]
        list.pop(list.index(moordenaar) + 1)
    else:
        x = list[list.index(moordenaar) + 2]
        list.pop(list.index(moordenaar) + 1)

    return (x, list)

def ik_ben_vermoord(list, naam):
    if len(list) == 1:
        x = list[0]
    elif list.index(naam) == 0:
        x = list[1]
        list.pop(list.index(naam))
    elif list.index(naam) + 1 >= len(list):
        x = list[0]
        list.pop(list.index(naam))
    else:
        x = list[list.index(naam) + 1]
        list.pop(list.index(naam))
    return (x, list)