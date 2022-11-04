from django.urls import path
from . import views

urlpatterns = [
    path('create', views.ArtistForm.as_view(), name="create"),
    path('', views.ArtistApiview.as_view(), name="artistsApi"),

]
