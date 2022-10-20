from dataclasses import fields
from django import forms
from .models import Album


class CreateAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
