from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response as RfResponse
from rest_framework.views import APIView
from apps.common.response import Response
from apps.common.utils import (
    requestJson,
    get_object_or_none,
    serializer_data,
    serializer_data_create
)
from .models import Album, ArtistGroup
from .serializers import (
    AlbumSerializer, 
    ArtisAlbumSerializer,
    ArtistGroupSerializer
)
import json


class AlbumDetailView(APIView):
    """ Album List View """


    def get(self, request,id):
        """ Get Album by id """
        return serializer_data(Album,id,AlbumSerializer,request,{
            'Album': 'Album does not exist'
            }
        )


    def patch(self, request, id):
        """ Update Album """
        return serializer_data_create(Album,id,
            AlbumSerializer,True,request,
            {
                'Album': 'Album does not exist'
            }
        )



class AlbumListView(APIView):
    """ Album List View """

    def get(self, request):

        if not request.GET:
            album = Album.objects.all()
        else: 
            filter = {}

            if request.GET.get('name'):
                filter['id'] = request.GET.get('name')
            if request.GET.get('songs'):
                filter['songs'] = request.GET.get('songs')
            if request.GET.get('artist'):
                filter['artist__id'] = request.GET.get('artist')
                            
            album = Album.objects.filter(**filter)

        serializer = AlbumSerializer(album,
            context={'request':request}, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ArtistGroupListVIew(APIView):

    def get(self, request):
        artists = ArtistGroup.objects.all()
        serializer = ArtistGroupSerializer(artists,
            context={'request':request}, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = ArtistGroupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"filtered_error": 'fail'},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)



class ArtistView(APIView):
    "Artis View"

    def get(self, request,id):
        return serializer_data(ArtistGroup,id,
            ArtistGroupSerializer,
            request,{
                'Album': 'Album does not exist'
            }
        )
        

    def put(self,request,id):
        return serializer_data_create(ArtistGroup,id,
            ArtistGroupSerializer,False,request,
            {
                'ArtistGroup': 'ArtistGroup does not exist'
            }
        )
                


class ArtistAlbumView(APIView):
    "Artisr List Album View"

    def get(self, request,id):
        return serializer_data(ArtistGroup,id,
            ArtisAlbumSerializer,
            request,{
            'Artis': 'Album does not exist'
            }
        )



"""
    Case https://gturnquist-quoters.cfapps.io/api/random
"""


class TimeLineView(APIView):
    def get(self, request):
        data =requestJson('https://gturnquist-quoters.cfapps.io/api/random')        
        return Response(data=json.loads(data), status=status.HTTP_200_OK)


"""
    xml 
"""