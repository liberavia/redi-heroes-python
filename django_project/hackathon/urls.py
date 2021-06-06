from django.urls import path
from . import views as hackathon_views


urlpatterns = [
    path('', hackathon_views.startseite, name='hackathon-start'),
    path('ueber/', hackathon_views.ueberseite, name='hackathon-ueber')
]