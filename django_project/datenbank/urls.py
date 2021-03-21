from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as datenbank_views

urlpatterns = [
    path('', datenbank_views.start , name='datenbank-start')
]