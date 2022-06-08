import mock
from django.core.files import File
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from .models import (Anime,
                     Genre,
                     Personage, 
                     Video,
                     VideoShots
                        )

from .serializers import VideoDetailSerializer


class VideoTests(APITestCase):


    def setUp(self):
        self.one_genre = Genre.objects.create(title='First-genre', slug='genre')
        Genre.objects.create(title='Second-brand', slug='secons-brand')


        self.one_anime = Anime.objects.create(title='First-anime', slug="anime")
        Anime.objects.create(title='Second-anime', slug="sec-anime")


        self.one_personage = Personage.objects.create(name='First personage', slug='first-personage')
        Personage.objects.create(name='Second personage', slug='second-personage')


        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'photo.jpg'


        self.one_video = Video.objects.create(
            title='Video',
            description='Example test description',
            slug="video",
            # genres = self.one_genre,    
            category=self.one_anime,
            # personages=self.one_personage,
            allow_comments=True,
            is_public=False,
        )

        self.one_shot = VideoShots.objects.create(title='First shot', slug='first-shot', video=self.one_video)
        VideoShots.objects.create(title='Second shot', slug='second-shot', video=self.one_video)

    def test_genre_list(self):
        response = self.client.get(reverse('genre-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        # print(response.json().get('results'))
        self.assertTrue({'id': 1, 'title': 'First-genre', 'description': None,
                            'slug': 'genre'}, {'id': 2, 'title': 'Second-brand', 'description': None,
                            'slug': 'secons-brand'} in response.json().get('results'))

    def test_anime_list(self):
        response = self.client.get(reverse('anime-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        # print(response.json().get('results'))
        self.assertTrue({'id': 1, 'title': 'First-anime', 'slug': 'anime', 'description': None},
                        {'id': 2, 'title': 'Second-anime', 'slug': 'sec-anime', 'description': None} in response.json().get('results'))

    def test_personage_list(self):
        response = self.client.get(reverse('personage-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        # print(response.json().get('results'))
        self.assertTrue({'id': 5, 'name': 'First personage', 'description': '', 'image': None,
                            'slug': 'first-personage'}, 
                            {'id': 6, 'name': 'Second personage', 'description': '', 'image': None, 
                            'slug': 'second-personage'} in response.json().get('results'))


    def test_product_detail(self):
        response = self.client.get(reverse('video-detail', kwargs={'pk': self.one_video.id}))
        serializer_data = VideoDetailSerializer(self.one_video).data
        # print(f'HERE RES{response.data}')
        # print(f'HERE SER{serializer_data}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)


    def test_video_shots(self):
        response = self.client.get(reverse('shots-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        # print(response.json().get('results'))
        self.assertTrue({'id': 9, 'title': 'First shot', 'description': None, 
                            'slug': 'first-shot', 'image': None, 'video': 5}, 
                        {'id': 10, 'title': 'Second shot', 'description': None, 
                            'slug': 'second-shot', 'image': None, 'video': 5} in response.json().get('results'))
