#invoer
hendel_trekken = str(input('Trek aan de hendel van de wissel? (ja/nee): '))
man_op_spoor_duwen = str(input('Duw de man op het spoor? (ja/nee): '))

#vragen
if hendel_trekken == 'ja':
    if man_op_spoor_duwen == 'ja':
        doden = '2'
    else:
        doden = '1'

else:
    if man_op_spoor_duwen == 'ja':
        doden = '1'
    else:
        doden = '5'

#uitvoer
print(doden)
