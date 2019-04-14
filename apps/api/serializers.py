from builtins import object
from fnmatch import filter
from rest_framework import serializers
from .models import Album, ArtistGroup


class ArtistGroupSerializer(serializers.ModelSerializer):
    """  Serializer """

    class Meta:
        model = ArtistGroup
        fields ='__all__'


class AlbumSerializer(serializers.ModelSerializer):
    """ Album Serializer """
    artist = ArtistGroupSerializer(many=False)

    class Meta:
        model = Album
        fields ='__all__'


class AlbumNotAritisSerializer(serializers.ModelSerializer):
    """ Album Serializer """

    class Meta:
        model = Album
        exclude = ('artist',)


class ArtisAlbumSerializer(serializers.ModelSerializer):

    albums = serializers.SerializerMethodField()

    def get_albums(self, obj):
        album = Album.objects.filter(artist__id=obj.id)
        serializer = AlbumNotAritisSerializer(album,
            context=self.context['request'], many=True)
        return serializer.data    

    class Meta:
        model = ArtistGroup
        fields ='__all__'
