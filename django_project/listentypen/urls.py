from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as listentypen_views

urlpatterns = [
    path('', listentypen_views.start , name='listentypen-start')
]