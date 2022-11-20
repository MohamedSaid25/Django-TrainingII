import pytest
from artists.models import Artist
from albums.models import Album
from datetime import datetime
from rest_framework import status
from authentication.tests.fixtures import api_client_auth


class TestAlbum:

    def test_if_authCanPost(self, django_user_model, api_client_auth):
        user = django_user_model.objects.create_user(
            username="task7", password="task7")
        client = api_client_auth(user)

        artist = Artist.objects.create(user=user, stageName='artist')
        album = {
            "name": "album",
            "release": datetime(12, 12, 2001),
            "cost": 100,
            "isApproved": True,
        }

        response = client.post('/albums/', album)

        assert response.status_code == status.HTTP_201_CREATED
