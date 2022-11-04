from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateArtist
from .models import Artist
from .serializers import ArtistSerializer
from artists import serializers
from django.http import JsonResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics

# Create your views here.


class ArtistForm(LoginRequiredMixin, FormView):
    form_class = CreateArtist
    template_name = 'artists/addArtist.html'
    success_url = 'create'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ArtistApiview(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
