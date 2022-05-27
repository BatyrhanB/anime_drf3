from rest_framework import serializers as s

from .models import Video, VideoCategory

class VideoSerializer(s.ModelSerializer):
    class Meta:
        model = Video                           
        fields = ('title', 'description', 'image', 'file')

class CategorySerializer(s.ModelSerializer):
    class Meta:
        model = VideoCategory                           
        fields = ('title', 'description')
