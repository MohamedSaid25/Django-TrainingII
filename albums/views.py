from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateAlbum
from .models import Album
# Create your views here.


def createAlbum(request):
    if request.method == 'POST':

        newAlbum = CreateAlbum(request.POST)
        if newAlbum.is_valid():
            newAlbum.save()

    return render(request, 'albums/createAlbum.html', {'createAlbum': CreateAlbum})
