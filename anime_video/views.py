from requests import request
from django_filters import rest_framework as filters
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import (
                     Video, 
                     Anime, 
                     Personage, 
                     Genre, 
                     VideoShots
                     )
from . serializers import (
                            VideoListSerializer, 
                            VideoDetailSerializer, 
                            PersonageSerializer, 
                            GenreSerializer, 
                            AnimeSerializer, 
                            AnimeDetailSerializer,
                            VideoShotsListSerializer
                          )

from config.mixins import RequestLogViewMixin


class VideoList(RequestLogViewMixin,
                ListAPIView
                ):
    queryset = Video.objects.all()
    serializer_class = VideoListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'genres', 'personages')
    # pagination_class = None


class VideoDetail(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer
    permission_classes = (AllowAny,)


class AnimeList(ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (AllowAny,)


class AnimeDetail(RetrieveAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeDetailSerializer
    permission_classes = (AllowAny,)


class PersonageDetail(RetrieveAPIView):
    queryset = Personage.objects.all()
    serializer_class = PersonageSerializer
    permission_classes = (AllowAny,)


class PersonageList(ListAPIView):
    queryset = Personage.objects.all()
    serializer_class = PersonageSerializer
    permission_classes = (AllowAny,)


class GenreDetail(RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AllowAny,)


class GenreList(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AllowAny,)

class VideoShotsList(ListAPIView):
    queryset = VideoShots.objects.all()
    serializer_class = VideoShotsListSerializer
    permission_classes = (AllowAny,)