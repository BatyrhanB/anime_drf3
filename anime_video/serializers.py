from rest_framework import serializers as s

from .models import Video

class VideoSerializer(s.ModelSerializer):
    class Meta:
        model = Video                           
        fields = ('title', 'description', 'image', 'file')
