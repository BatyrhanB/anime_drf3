from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('anime/', views.AnimeList.as_view(), name='category-list'),
    path('anime/<int:pk>/', views.AnimeDetail.as_view(), name='category-detail'),
    path('video/', views.VideoList.as_view(), name='video-list'),
    path('video/<int:pk>/', views.VideoDetail.as_view(), name='video-detail'),
    path('actors/', views.PersonageList.as_view(), name='personage-list'),
    path('actors/<int:pk>', views.PersonageDetail.as_view(), name='personage-detail'),
    path('genre/', views.GenreList.as_view(), name='genre-list'),
    path('genre/<int:pk>', views.GenreDetail.as_view(), name='genre-detail'),
]