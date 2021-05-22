from django.shortcuts import render


def start(request):
    kung_fu_helden = [
        'Bruce Lee',
        'Jet Li',
        'Kung-Fu Panda',
        'Jackie Chan'
    ]

    ein_woerterbuch = {
        'wort_mit_k': 'Kreis',
        'lieblingszahl': 10,
        'die_liste': kung_fu_helden
    }

    eine_einkaufsliste = [
        'Milch',
        'Salz',
        'Butter',
        'Popcornmais'
    ]

    context = {
        'die_liste': eine_einkaufsliste,
        'das_woerterbuch': ein_woerterbuch
    }

    return render(request, 'listentypen/listentypen.html', context)
