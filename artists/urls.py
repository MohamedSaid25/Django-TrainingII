from django.urls import path
from . import views

urlpatterns = [
    path('create', views.addArtist, name='home')
]
