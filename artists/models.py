from django.db import models

# Create your models here.
from django.db import models
#from albums.models import Album
# Create your models here.


class Artist(models.Model):

    stageName = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    socialMediaProfile = models.URLField(
        max_length=200, blank=True, null=False)

    class Meta:
        ordering = ['stageName']

    # def approved_albums(self):
    #   return 0  # obj.album_set.filter(is_approved=True).count()

    def __str__(self):
        return self.stageName
