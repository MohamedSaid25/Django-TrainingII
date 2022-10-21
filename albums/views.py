from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateAlbum
from .models import Album
# Create your views here.


def createAlbum(request):

    form = CreateAlbum(request.POST or None)
    if form.is_valid():
        form.save()
        form = createAlbum()
    context = {
        'form': form
    }
    return render(request, 'albums/createAlbum.html', context)
