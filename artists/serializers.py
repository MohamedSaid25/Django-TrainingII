from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'stageName', 'socialMediaProfile']
