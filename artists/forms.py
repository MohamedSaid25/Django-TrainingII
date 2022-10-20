from dataclasses import fields
from django import forms
from .models import Artist


class CreateArtist(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['stageName', 'socialMediaProfile']

        def clean_stageName(self):
            stageName = self.cleaned_data.get('stageName')
            print("SSSSSSSSSSS", stageName)
            if Artist.objects.filter(stageName=stageName).exists():
                raise forms.ValidationError('Already Exist')
            return stageName
