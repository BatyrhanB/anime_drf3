from rest_framework import serializers as s

from .models import Video, VideoCategory

class VideoListSerializer(s.ModelSerializer):
    class Meta:
        model = Video                           
        fields = ('title', 'description', 'image', 'file')

class VideoDetailSerializer(s.ModelSerializer):
    class Meta:
        model = Video                           
        fields = '__all__'

class CategorySerializer(s.ModelSerializer):
    class Meta:
        model = VideoCategory                           
        fields = '__all__'
