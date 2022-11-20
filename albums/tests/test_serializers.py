import pytest
from ..models import Album
from ..serializers import AlbumSerializer
from artists.models import Artist
from users.models import User
from datetime import datetime


@pytest.mark.django_db
def test_AlbumSerializer_validData():
    # create user
    user = User.objects.create(
        username='task8', password='sadboy2022')
    # create artist
    addArtist = Artist.objects.create(
        stageName='uzumakiMeta', socialMediaProfile='https://www.bldai.com/', user=user)
    # create album
    addAlbum = Album.objects.create(
        name='Dead at nigth suffer at moring', artistName=addArtist, release=datetime(2001, 5, 5), cost=100.00)

    serializer = AlbumSerializer(addAlbum)

    assert addAlbum.artistName.id == serializer.data['artistName']['id']
    assert addAlbum.name == serializer.data['name']
    assert str(addAlbum.release)[:1] == str(serializer.data['release'])[:1]
    assert addAlbum.cost == float(serializer.data['cost'])


@pytest.mark.django_db
def test_AlbumSerializer_WrongCostdata():

    # create user
    user = User.objects.create(
        username='task8', password='sadboy2022')
    # create artist
    addArtist = Artist.objects.create(
        stageName='uzumakiMeta', socialMediaProfile='https://www.bldai.com/', user=user)
    # create album

    serializer = AlbumSerializer(data={
        "name": "Roma",
        "release": datetime(2002, 7, 7),
        "cost": "badData",
        "artistName": addArtist
    })

    serializer.is_valid(raise_exception=False)
    assert serializer.errors
    assert serializer.errors.keys() == set(['cost'])
