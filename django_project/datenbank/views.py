from django.shortcuts import render
from .models import Namensliste
from django.views.generic import DeleteView, UpdateView


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
    punkte = request.POST.get('eingabePunkte')
    neuer_eintrag = Namensliste.objects.filter(name=neuer_name).first()
    if neuer_eintrag:
        neuer_eintrag.punkte += int(punkte)
    else:
        neuer_eintrag = Namensliste(name=neuer_name, punkte=int(punkte))
    neuer_eintrag.save()


class DeleteNameView(DeleteView):
    model = Namensliste
    success_url = '/datenbank/'


class UpdateNameView(UpdateView):
    model = Namensliste
    fields = ['name', 'punkte']
    success_url = '/datenbank/'

