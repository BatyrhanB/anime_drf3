from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('anime/', cache_page(30)(views.AnimeList.as_view()), name='anime-list'),
    path('anime/<int:pk>/', views.AnimeDetail.as_view(), name='anime-detail'),
    path('video/', cache_page(30)(views.VideoList.as_view()), name='video-list'),
    path('video/<int:pk>/', views.VideoDetail.as_view(), name='video-detail'),
    path('actors/', views.PersonageList.as_view(), name='personage-list'),
    path('actors/<int:pk>/', views.PersonageDetail.as_view(), name='personage-detail'),
    path('genre/', views.GenreList.as_view(), name='genre-list'),
    path('genre/<int:pk>/', views.GenreDetail.as_view(), name='genre-detail'),
    path('shots/', views.VideoShotsList.as_view(), name='shots-list'),
]
