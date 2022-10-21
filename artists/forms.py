from dataclasses import fields
from django import forms
from .models import Artist


class CreateArtist(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['stageName', 'socialMediaProfile']

    def clean_stageName(self, *args, **kwargs):

        stageName = self.cleaned_data.get("stageName")
        if Artist.objects.filter(stageName=stageName).exists():
            raise forms.ValidationError(
                "already Exist in database try another name")
        else:
            return stageName
