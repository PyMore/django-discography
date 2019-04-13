from django.contrib import admin
from .models import ArtistGroup, Album
# Register your models here.

admin.site.register(Album)
admin.site.register(ArtistGroup)
