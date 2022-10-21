from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateArtist
from .models import Artist
from albums.models import Album
# Create your views here.


def addArtist(request):

    form = CreateArtist(request.POST or None)

    if form.is_valid():
        form.save()
        form = CreateArtist()
    context = {

        'form': form
    }

    return render(request, 'artists/addArtist.html', context)


def artistInfo(request):

    allArtists = Artist.objects.all()

    context = {

        'Artists': allArtists
    }

    return render(request, 'artists/info.html', context)
