from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateArtist
from .models import Artist
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
