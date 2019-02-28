def verlaat_ploeg(naam, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(naam)

    if len(inschrijvingen[ploeg]) == 0:
        inschrijvingen.pop(ploeg)

    return inschrijvingen

def vervoegt_ploeg(naam, ploeg, ploegen):
    if ploeg in ploegen:
        ploegen[ploeg] += [naam]

    else:
        ploegen[ploeg] = [naam]

    return ploegen

print(vervoegt_ploeg('Els','Sinbox',{'Sinbox': ['An', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']})
)