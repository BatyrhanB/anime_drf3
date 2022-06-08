from rest_framework import serializers as s

from .models import (Video, 
                     Anime, 
                     Personage, 
                     Genre, 
                     VideoShots)


class VideoListSerializer(s.ModelSerializer):
    class Meta:
        model = Video                           
        fields = ('title',
                  'description',
                  'image', 
                  'file'
                  )


class PersonageSerializer(s.ModelSerializer):
    class Meta:
        model = Personage                           
        fields = '__all__'


class PersonageInnerSerializer(s.ModelSerializer):
    class Meta:
        model = Personage                           
        fields = ('name', 
                  'description'
                 )


class GenreSerializer(s.ModelSerializer):
    class Meta:
        model = Genre                           
        fields = '__all__'


class GenreInnerSerializer(s.ModelSerializer):
    class Meta:
        model = Genre                           
        fields = ('id',
                  'title'
                  )


class VideoDetailSerializer(s.ModelSerializer):

    category = s.CharField(source='category.title')
    # genre = s.CharField(source='genres.title')
    genres = GenreInnerSerializer(many=True)
    personages = PersonageInnerSerializer(many=True)

    class Meta:
        model = Video                           
        fields = ('title', 
                  'description', 
                  'slug', 
                  'image', 
                  'file', 
                  'video_type', 
                  'category', 
                  'genres', 
                  'personages',
                  'allow_comments', 
                  'is_public', 
                  'create_at', 
                  'modified_date', 
                  'publish_date'
                 )


class AnimeSerializer(s.ModelSerializer):
    class Meta:
        model = Anime                           
        fields = '__all__'



class AnimeDetailSerializer(s.ModelSerializer):
    videos = VideoListSerializer(many=True)
    class Meta:
        model = Anime                           
        fields = ('title', 
                  'slug', 
                  'description', 
                  'videos'
                 )

class VideoShotsListSerializer(s.ModelSerializer):
    class Meta:
        model = VideoShots                           
        fields = '__all__'


