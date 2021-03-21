from django.shortcuts import render
from .models import Namensliste
from django.views.generic import DeleteView


def start(request):
    if request.method == 'POST':
        save_name(request)
    liste_namen = Namensliste.objects.all()

    context = {
        'namensliste': liste_namen
    }

    return render(request, 'datenbank/content.html', context)


def save_name(request):
    neuer_name = request.POST.get('eingabeName')
    neuer_eintrag = Namensliste(name=neuer_name)
    neuer_eintrag.save()


class DeleteNameView(DeleteView):
    model = Namensliste
    success_url = '/datenbank/'
