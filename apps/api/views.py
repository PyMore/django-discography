
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response as RfResponse
from apps.common.response import Response
from .models import Album,ArtistGroup
from .serializers import (
    AlbumSerializer,
    ArtistGroupSerializer
)


class AlbumListView(APIView):

    def get(self, request):
        artists = ArtistGroup.objects.all()
        serializer = ArtistGroupSerializer(artists,
            context={'request':request}, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)