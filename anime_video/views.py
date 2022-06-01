from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Video, VideoCategory
from . serializers import VideoListSerializer, VideoDetailSerializer, CategorySerializer


class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoListSerializer


class VideoDetail(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer


class CategoryList(ListAPIView):
    queryset = VideoCategory.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveAPIView):
    queryset = VideoCategory.objects.all()
    serializer_class = CategorySerializer

