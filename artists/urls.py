from django.urls import path
from . import views

urlpatterns = [
    path('create', views.ArtistForm.as_view(), name="create"),
    path('', views.ArtistList.as_view()),

]
