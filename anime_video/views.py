from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Video, VideoCategory
from . serializers import VideoSerializer, CategorySerializer
class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CategoryList(ListAPIView):
    queryset = VideoCategory.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(RetrieveAPIView):
    queryset = VideoCategory.objects.all()
    serializer_class = CategorySerializer

