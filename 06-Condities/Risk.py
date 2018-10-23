worp_1a = int(input('worp 1 aanvaller: '))
worp_2a = int(input('worp 2 aanvaller: '))
worp_3a = int(input('worp 3 aanvaller: '))
worp_4b = int(input('worp 1 verdediger: '))
worp_5b = int(input('worp 2 verdediger: '))

totaal_a = worp_1a + worp_2a + worp_3a
totaal_b = worp_4b + worp_5b

max_a = max(worp_1a, worp_2a, worp_3a)
max_b = max(worp_4b, worp_5b)
x = [worp_1a, worp_2a, worp_3a]
middel_a = sorted(x)[len(x) // 2]
middel_b = min(worp_4b, worp_5b)

if max_a == max_b and middel_a == middel_b:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')

elif max_a > max_b and middel_a > middel_b:
    print('aanvaller verliest 0 legers, verdediger verliest 2 legers')

elif max_a > max_b and middel_a < middel_b:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')

elif max_a < max_b and middel_a > middel_b:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')

elif max_a < max_b and middel_a < middel_b:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')

elif max_a == max_b and middel_a < middel_b:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')

elif max_a == max_b and middel_a > middel_b:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')

elif max_a < max_b and middel_a == middel_b:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')

elif max_a > max_b and middel_a == middel_b:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')