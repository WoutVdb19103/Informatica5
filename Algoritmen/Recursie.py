def faculteit(n):
    if n == 1:
        return 1
    else:
        print('{} * faculteit{}'.format(n, n - 1))
        res = faculteit(n - 1)
        print('{} * {} = {}'.format(n, res, n * res))
        return n * res

print(faculteit(6))