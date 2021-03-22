from django.urls import path
from . import views as neueapp_views

urlpatterns = [
    path('', neueapp_views.start, name='neueapp-start'),
]