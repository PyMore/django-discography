from django.contrib import admin
from django.urls import path,include
from .views import AlbumListView

urlpatterns = [
    path('albums', AlbumListView.as_view(), name='albums-list'),
]
