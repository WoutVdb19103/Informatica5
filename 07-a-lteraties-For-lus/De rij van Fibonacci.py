#invoer
n = int(input('Hoeveelste getal van Fibonacci: '))

vorige, huidige = 1, 1

#bewerking
for i in range(n - 2):
    vorige, huidige = huidige, huidige + vorige

#invoer
print(huidige)
