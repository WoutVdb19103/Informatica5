#invoer
speler_1 = str(input('Welke vorm achter je rug (blad/steen/schaar, speler 1)? '))
speler_2 = str(input('Welke vorm achter je rug (blad/steen/schaar, speler 2)? '))

#bewerking
if speler_1 == speler_2:
    uitkomst = 'onbeslist'

elif speler_1 == 'blad' and speler_2 == 'steen' or speler_1 == 'steen' and speler_2 == 'schaar' or speler_1 == 'schaar' and speler_2 == 'blad':
    uitkomst = 'speler 1 wint'

else:
    uitkomst = 'speler 2 wint'



#uitvoer
print(uitkomst)