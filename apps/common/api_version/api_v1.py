from .api_name import SerializersListApv1
from apps.api.serializers import *

class Apiv1:
    
    def get_serializer_class(name):

        if name == SerializersListApv1.ArtistGroupSerializer:
            return ArtisAlbumSerializer
        
        elif name == SerializersListApv1.AlbumSerializer:
            return AlbumSerializer

        elif name == SerializersListApv1.AlbumNotAritisSerializer:
            return AlbumNotAritisSerializer

        elif name == SerializersListApv1.ArtisAlbumSerializer:
            return ArtisAlbumSerializer
        
        else        
            return None 
     