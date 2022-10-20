from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateArtist
from .models import Artist
# Create your views here.


def addArtist(request):

    if request.method == 'POST':

        newArtist = CreateArtist(request.POST)
        if newArtist.is_valid():
            newArtist.save()

    return render(request, 'artists/addArtist.html', {'addArtist': CreateArtist})
