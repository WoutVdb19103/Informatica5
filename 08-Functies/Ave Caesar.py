#invoer
def is_letter(n):
    if n in 'abcdefghijklmnopqrstuvwxyz' or n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        waarheid = True
    else:
        waarheid = False
    return waarheid


def roteer_letter(n, k):
    if is_letter(n) == True:
        if n in 'abcdefghijklmnopqrstuvwxyz':
            if ord(n) + k > 122:
                return chr((ord(n) + k) - 26)
            else:
                return chr(ord(n) + k)

        elif n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if ord(n) + k > 90:
                return chr((ord(n) + k) - 26)
            else:
                return chr(ord(n)+k)
    else:
        return n


def versleutel(z, k):
    zin = ''
    for letter in z:
        zin += roteer_letter(letter, k)
    return zin