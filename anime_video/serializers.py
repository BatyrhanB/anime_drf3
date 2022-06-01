from rest_framework import serializers as s

from .models import Video, VideoCategory, Personage, Genre

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

class PersonageSerializer(s.ModelSerializer):
    class Meta:
        model = Personage                           
        fields = '__all__'


class GenreSerializer(s.ModelSerializer):
    class Meta:
        model = Genre                           
        fields = '__all__'
