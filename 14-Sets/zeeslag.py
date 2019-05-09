def boot_overlappend(c1, c2):
    return c1.intersection(c2) == 0

print(boot_overlappend({'B4', 'A4', 'C4'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))