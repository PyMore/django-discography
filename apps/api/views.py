
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


class AlbumDetailView(APIView):
    """ Album List View """

    def get(self, request,id):
        album = get_object_or_none(Album,pk=id)

        if not album:
            return Response (data={'Album': 'Album does not exist'},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = AlbumSerializer(album,
            context={'request':request}, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get(self, request,id):
        album = get_object_or_none(Album,pk=id)

        if not album:
            return Response (data={'Album': 'Album does not exist'},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = AlbumSerializer(album,
            context={'request':request}, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, id):
        album = get_object_or_none(Album,pk=id)

        if not album:
            return Response (data={'Album': 'Album does not exist'},
                status=status.HTTP_400_BAD_REQUEST)


        serializer = AlbumSerializer(
            album,
            data=request.data,
            partial=True)

        if not serializer.is_valid():
            return Response(data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        serializer = AlbumSerializer(album,
            context={'request':request}, many=False)
            
        return Response(data={}, status=status.HTTP_200_OK)



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
                            
            print(filter)
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
            return Response (data={'ArtistGroup': 'ArtistGroup does not exist'},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = ArtistGroupSerializer(artists,
            context={'request':request}, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def put(self,request,id):
        artists = get_object_or_none(ArtistGroup, pk=id)
        if not artists:
            return Response (data={'ArtistGroup': 'ArtistGroup does not exist'},
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


"""
    xml 
"""