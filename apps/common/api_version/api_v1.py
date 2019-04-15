from .api_name import SerializersListApv1
from apps.api.serializers import *

class Apiv1:
    
    def get_serializer_class(self,name):
        if name == SerializersListApv1.ArtistGroupSerializer.name:
            return ArtisAlbumSerializer
        
        elif name == SerializersListApv1.AlbumSerializer.name:
            return AlbumSerializer

        elif name == SerializersListApv1.AlbumNotAritisSerializer.name:
            return AlbumNotAritisSerializer

        elif name == SerializersListApv1.ArtisAlbumSerializer.name:
            return ArtisAlbumSerializer
        
        else:        
            return None 
     