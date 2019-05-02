def vergeten_woorden(tekst, verplicht):
    verzameling = set(tekst.split())

    gebruikte_woorden = len(verzameling.intersection(verplicht))

    return len(verplicht), len(verplicht) - gebruikte_woorden, gebruikte_woorden


verplicht = {'python', 'world', 'hello', 'java'}
tekst = 'hello world world world'
print(vergeten_woorden(tekst, verplicht))