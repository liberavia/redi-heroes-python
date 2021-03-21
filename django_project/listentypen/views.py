from django.shortcuts import render


def start(request):
    eine_liste = [
        'Eintrag 1',
        'Eintrag 2',
        'Eintrag 3',
        'Eintrag 4',
        'Eintrag 5',
    ]

    ein_woerterbuch = {
        'wort_mit_k': 'Kaffee',
        'lieblingszahl': 8,
        'die_liste': eine_liste
    }

    # Später verwenden wir vor allem Listen von Dictionaries.
    # So sieht dann z. B. eine Personenliste aus:
    personen = [
        {
            'name': 'André',
            'alter': 42
        },
        {
            'name': 'Oliver',
            'alter': 17
        },
        {
            'name': 'Vanessa',
            'alter': 16
        },
        {
            'name': 'Rebecca',
            'alter': 9
        },
    ]

    context = {
        'die_liste': eine_liste,
        'das_woerterbuch': ein_woerterbuch,
        'die_personen': personen
    }

    return render(request, 'listentypen/listentypen.html', context)
