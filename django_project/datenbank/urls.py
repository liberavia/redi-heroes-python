from django.urls import path
from . import views as datenbank_views
from .views import DeleteNameView

urlpatterns = [
    path('', datenbank_views.start, name='datenbank-start'),
    path('delete/<int:pk>', DeleteNameView.as_view(), name='datenbank-loeschen')
]