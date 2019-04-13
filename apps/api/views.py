
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response as RfResponse
from rest_framework.views import APIView
from apps.common.response import Response
from apps.common.utils import requestJson,get_object_or_none
from .models import Album, ArtistGroup
from .serializers import (
    AlbumSerializer, 
    ArtisAlbumSerializer,
    ArtistGroupSerializer
)
import json

class AlbumListView(APIView):
    """ Album List View """

    def get(self, request):

        if not request.GET:
            album = Album.objects.all()
        else: 
            filter = {}

            if request.GET.has_key('id'):
                filter['pk'] = album
            
            print(filter)
            album = Album.object.filter(**filter)

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
        print(request.data)
        serializer = ArtistGroupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"filtered_error": 'fail'},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)



class ArtistView(APIView):
    "Artis View"

    def get(self, request,id):
        artists = ArtistGroup.objects.get(pk=id)

        if not artists:
            return Response (data={'ArtistGroup': [_('ArtistGroup does not exist')]},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = ArtistGroupSerializer(artists,
            context={'request':request}, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def put(self,request,id):
        artists = get_object_or_none(ArtistGroup, pk=id)
        if not artists:
            return Response (data={'ArtistGroup': [_('ArtistGroup does not exist')]},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = ArtistGroupSerializer(artists, data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data='update', status=status.HTTP_200_OK)
        




class ArtistAlbumView(APIView):
    "Artisr List Album View"

    def get(self, request,id):
        artists = ArtistGroup.objects.get(pk=id)
        serializer = ArtisAlbumSerializer(artists,
            context={'request':request}, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



"""
    Case https://gturnquist-quoters.cfapps.io/api/random
"""


class TimeLineView(APIView):
    def get(self, request):
        data =requestJson('https://gturnquist-quoters.cfapps.io/api/random')        
        return Response(data=json.loads(data), status=status.HTTP_200_OK)
