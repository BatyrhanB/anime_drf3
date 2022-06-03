from requests import request
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters import rest_framework as filters

from .models import Video, Anime, Personage, Genre
from . serializers import (
    VideoListSerializer, 
    VideoDetailSerializer, 
    PersonageSerializer, 
    GenreSerializer, 
    AnimeSerializer, 
    AnimeDetailSerializer
    )


class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'genres', 'personages')


class VideoDetail(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer


class AnimeList(ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class AnimeDetail(RetrieveAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeDetailSerializer


class PersonageDetail(RetrieveAPIView):
    queryset = Personage.objects.all()
    serializer_class = PersonageSerializer


class PersonageList(ListAPIView):
    queryset = Personage.objects.all()
    serializer_class = PersonageSerializer


class GenreDetail(RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreList(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
