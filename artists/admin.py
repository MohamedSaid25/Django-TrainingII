from django.contrib import admin
from .models import Artist
from albums.models import Album
# Register your models here.


class AlbumInstanceInline(admin.TabularInline):
    model = Album


class ArtistAdmin(admin.ModelAdmin):

    def approvedAlbumsCountPerArtist(self, obj):
        return obj.album_set.filter(isApproved=True).count()

    approvedAlbumsCountPerArtist.short_description = 'Approved_Albums'

    list_display = ['stageName', 'approvedAlbumsCountPerArtist']

    inlines = [AlbumInstanceInline]


admin.site.register(Artist, ArtistAdmin)
