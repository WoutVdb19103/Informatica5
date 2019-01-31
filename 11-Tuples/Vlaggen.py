def vlag(richting, kleuren):
    patroon = ''

    for kleur in kleuren:

        if richting == 'verticaal':

            if kleur == kleuren[-1]:

                patroon += kleur

            else:
                patroon += kleur + ' | '

        else:
            if kleur == kleuren[-1]:
                patroon += kleur

            else:
                patroon += kleur + '\n-\n'



    return patroon

print(vlag('verticaal', ('zwart', 'geel', 'rood')))