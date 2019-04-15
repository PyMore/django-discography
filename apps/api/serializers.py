from rest_framework import serializers
from .models import Album, ArtistGroup
from apps.common.serializer import ApiVersionSerializer
import datetime

class ArtistGroupSerializer(serializers.ModelSerializer):
    """  Serializer """

    class Meta:
        model = ArtistGroup
        exclude = (
            'enable',
        )
    

class AlbumSerializer(serializers.ModelSerializer):
    """ Album Serializer """

    artist = ArtistGroupSerializer(many=False)
    year = serializers.DateTimeField()

    class Meta:
        model = Album
        fields = '__all__'

    def validate(self, data):
        """
        Check that date is corret.
        """

        print(data.get('year'))
        return data
 
    
    def update(self, instance, validated_data):
        return instance    



class AlbumNotAritisSerializer(serializers.ModelSerializer):
    """ Album Serializer """

    class Meta:
        model = Album
        exclude = (
            'artist',
            'enable',
            'created',
            'modified',
        )


class ArtisAlbumSerializer(serializers.ModelSerializer):

    albums = serializers.SerializerMethodField()

    def get_albums(self, obj):
        album = Album.objects.filter(artist__id=obj.id,enable=True)
        serializer = AlbumNotAritisSerializer(album,
            context=self.context['request'], many=True)
        return serializer.data    

    class Meta:
        model = ArtistGroup
        exclude = (
            'enable',
        )
