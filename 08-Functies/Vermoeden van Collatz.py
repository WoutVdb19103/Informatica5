#invoer
n = int(input('Geef een willekeurig natuurlijk getal zonder nul: '))

#bewerking
def volgend_collatz_getal(n):
    while n != 1:
        if (n / 2) = (n // 2):
            n = n / 2
        else:
            n = 3 * n + 1
        return n


