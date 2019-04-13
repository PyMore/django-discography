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
        fields ='__all__'

class ArtisAlbumSerializer(serializers.ModelSerializer):

    is_favorite = serializers.SerializerMethodField()

    def get_is_favorite(self, obj):
        albums= Album.objects.filter(artist__id=obj.id)
        print(albums)
        print(self.context['request'])
        return AlbumNotAritisSerializer(albums,self.context['request'],many=True).is_valid()

    class Meta:
        model = ArtistGroup
        fields ='__all__'
