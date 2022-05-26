from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Video
from . serializers import VideoSerializer
class VideoList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'video_list.html'

    def get(self, video):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response({'serializer': serializer, 'video': video})
