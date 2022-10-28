from email.policy import default
from django.db import models
from datetime import datetime
from imagekit.models import ProcessedImageField
from artists.models import Artist
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=100, default='New Album', blank=True)
    artistName = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=False)
    creationTime = models.DateTimeField(auto_now_add=True)
    release = models.DateTimeField(
        default=datetime.now, null=False, blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    isApproved = models.BooleanField(
        default=False, help_text='Approve the album if its name is not explicit')
    # = models.IntegerField()

    def __str__(self):
        return self.name


class Song(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name='song_set')
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField()
    thumbnail = ProcessedImageField(format='JPEG')
    audio = models.FileField(
        validators=[FileExtensionValidator(['mp3', 'wav'])])

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Song)
def song_pre_save(sender, instance, **kwargs):
    if instance.name == "":
        my_album_name = Album.objects.get(pk=instance.album.id)
        instance.name = my_album_name.name
