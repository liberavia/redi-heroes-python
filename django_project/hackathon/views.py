from django.shortcuts import render
from .models import Kommentar


def startseite(request):
    liste_kommentare = Kommentar.objects.all()

    context = {
        'kommentare': liste_kommentare
    }

    return render(request, 'hackathon/startseite.html', context)


def ueberseite(request):
    return render(request, 'hackathon/ueberseite.html')