from django.urls import path
from . import views as datenbank_views
from .views import DeleteNameView, UpdateNameView

urlpatterns = [
    path('', datenbank_views.start, name='datenbank-start'),
    path('loeschen/<int:pk>', DeleteNameView.as_view(), name='datenbank-loeschen'),
    path('bearbeiten/<int:pk>', UpdateNameView.as_view(), name='datenbank-bearbeiten')
]