#invoer
hendel_trekken = str(input('Trek aan de hendel van de wissel? (ja/nee): '))
man_op_spoor_duwen = str(input('Duw de man op het spoor? (ja/nee): '))

#vragen
if hendel_trekken == 'ja' and man_op_spoor_duwen == 'ja':
    doden = 2
elif hendel_trekken == 'nee' and man_op_spoor_duwen == 'nee':
    doden = 5
else:
    doden = 1

#uitvoer
print(doden)