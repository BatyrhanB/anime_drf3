from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Video
from . serializers import VideoSerializer
class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

