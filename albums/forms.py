from dataclasses import fields
from django import forms
from .models import Album


class CreateAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'artistName', 'release', 'cost']

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name")
        if name == "New Album":
            raise forms.ValidationError("Please Enter Your Album Name")
        else:
            return name

    def clean_cost(self, *args, **kwargs):
        cost = self.cleaned_data.get("cost")
        if cost <= 0:
            raise forms.ValidationError(
                "Please Enter Valid Price can't be zero or Negative")
        else:
            return cost
