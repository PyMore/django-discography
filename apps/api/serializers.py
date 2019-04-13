from rest_framework import serializers
from .models import Album,ArtistGroup


class AlbumSerializer(serializers.ModelSerializer):
    """ Album Serializer """

    class Meta:
        model = Album
        fields ='__all__'


class ArtistGroupSerializer(serializers.ModelSerializer):
    """  Serializer """

    class Meta:
        model = ArtistGroup
        fields ='__all__'
    