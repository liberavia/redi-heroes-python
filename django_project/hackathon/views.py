from django.shortcuts import render
from .models import Kommentar, Charakter


def startseite(request):
    liste_familienmitglieder = Charakter.objects.filter(familie=True)
    liste_sonstige = Charakter.objects.filter(familie=False)
    context = {
        'familienmitglieder': liste_familienmitglieder,
        'sonstige_charaktere': liste_sonstige,
    }

    return render(request, 'hackathon/startseite.html', context)


def speicher_kommentar(request):
    neuer_autor = request.POST.get('eingabeAutor')
    neuer_kommentartext = request.POST.get('eingabeKommentar')
    neuer_kommentar = Kommentar(autor=neuer_autor, kommentar=neuer_kommentartext)
    neuer_kommentar.save()


def ueberseite(request):
    if request.method == 'POST':
        speicher_kommentar(request)
    liste_kommentare = Kommentar.objects.all()

    context = {
        'kommentare': liste_kommentare
    }

    return render(request, 'hackathon/ueberseite.html', context)