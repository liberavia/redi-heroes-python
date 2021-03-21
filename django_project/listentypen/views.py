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

    context = {
        'die_liste': eine_liste,
        'das_woerterbuch': ein_woerterbuch,
    }

    return render(request, 'listentypen/listentypen.html', context)
