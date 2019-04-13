from django.contrib import admin
from django.urls import path,include
from .views import (
    AlbumListView,
    ArtistGroupListVIew,
    ArtistView,
    ArtistAlbumView,
    TimeLineView,
    AlbumDetailView
)

urlpatterns = [
    path('albums', AlbumListView.as_view(), name='albums-list'),
    path('albums/<int:id>', AlbumDetailView.as_view(), name='albums-detailt'),

    path('artists', ArtistGroupListVIew.as_view(), name='artists-list'),
    path('artist/<int:id>', ArtistView.as_view(), name='artist-detailt'),
    path('artist/<int:id>/albums', ArtistAlbumView.as_view(), name='artist-albums-list'),
    path('time-line', TimeLineView.as_view(), name='time-lineView-list'),
]