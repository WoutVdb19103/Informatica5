#invoer
n = int(input('Hoeveelste getal van Fibonacci: '))

vorige = 1
huidige = 1
#bewerking
for i in range(n - 2):
    vorige, huidige = huidige, huidige + vorige
    #print(vorige, huidige)

print(huidige)
