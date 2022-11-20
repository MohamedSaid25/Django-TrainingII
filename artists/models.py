from django.db import models
from users.models import User
from django.db.models import Q, Count


class ArtistManager(models.Manager):
    def get_queryset(self):
        approved_albums_number = Count(
            'album', filter=Q(album__isApproved=True))
        return super().get_queryset().annotate(isApproved=approved_albums_number)


class Artist(models.Model):

    stageName = models.CharField(
        max_length=100, unique=True, blank=False, null=False
    )
    socialMediaProfile = models.URLField(
        max_length=200, blank=True, null=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    objects = ArtistManager()

    class Meta:
        ordering = ['stageName']

    def __str__(self):
        return self.stageName
