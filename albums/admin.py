from django.contrib import admin
from .models import Album
# Register your models here.


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('creationTime',)
    #list_display = ['artistName', 'name']


admin.site.register(Album, AlbumAdmin)
