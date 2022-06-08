# from django.contrib.auth.models import User
from turtle import title
from usermodel.models import User
from django.core.management.base import BaseCommand

from anime_video.models import (
                                 Anime,
                                 Genre,
                                 Personage,
                                 Video,
                                 VideoShots
                                )


class Command(BaseCommand):
    help = 'Populates the database with some testing data.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Started database population process...'))

        if User.objects.filter(email="example@gmail.com").exists():
            self.stdout.write(self.style.SUCCESS('Database has already been populated. Cancelling the operation.'))
            return


#USER
    #1
        mike = User.objects.create_user(email="example@gmail.com", password='really_strong_password123')
        mike.first_name = 'Mike'
        mike.last_name = 'Smith'
        mike.save()
    #2
        jess = User.objects.create_user(email="jess@gmail.com", password='really_strong_password123')
        jess.first_name = 'Jess'
        jess.last_name = 'Brown'
        jess.save()
    #3
        johnny = User.objects.create_user(email="johnny@gmail.com", password='really_strong_password123')
        johnny.first_name = 'Johnny'
        johnny.last_name = 'Davis'
        johnny.save()


#ANIME
        naruto = Anime.objects.create(title='Naruto', slug="naruto")
        bleach = Anime.objects.create(title='Bleach', slug="bleache")
        one_piece = Anime.objects.create(title='One piece', slug="one-piece")


#GENRE
    #1
        fant_genre = Genre.objects.create(
            title='Fantastic',
            slug='fantastic'
        )
    #2
        romance = Genre.objects.create(
            title='Romance',
            slug='romance '
        )
    #3 
        comedy = Genre.objects.create(
            title='Comedy',
            slug='comedy '
        ) 


#PERSONAGES
    #1
        sasuke_actor = Personage.objects.create(
            name='Sasuke',
            description='Naruto personage Sasuke from UCHIHA clan',
            slug='sasuke '
        )
    #2     
        ichigo_actor = Personage.objects.create(
            name='Ichigo',
            description='Bleach personage HALF_SHINIGAMI',
            slug='ichigo '
        )
    #3     
        luffy_actor = Personage.objects.create(
            name='Luffy',
            description='One piece personage PIRATE',
            slug='luffy '
        ) 

#VIDOE
    #1
        naruto_video = Video.objects.create(
            title='Naruto 1 ser',
            description='Example test description',
            slug="naruto 1 ser", 
            allow_comments=True,
            is_public=False,
        )
        naruto_video.save()
        naruto_video.category.add(naruto)
        naruto_video.genres.add(fant_genre)
        naruto_video.personages.add(sasuke_actor)

    #2
        bleache_video = Video.objects.create(
            title='Bleache 1 ser',
            description='Example test description',
            slug="bleache 1 ser", 
            allow_comments=True,
            is_public=True,
        )
        bleache_video.save()
        bleache_video.category.add(bleach)
        naruto_video.genres.add(romance)
        naruto_video.personages.add(ichigo_actor)

    #3
        onepiece_video = Video.objects.create(
            title='One piece 1 ser',
            description='Example test description',
            slug="one piece 1 ser", 
            allow_comments=True,
            is_public=True,
        )
        onepiece_video.save()
        onepiece_video.category.add(one_piece)
        naruto_video.genres.add(comedy)
        naruto_video.personages.add(luffy_actor)


#VIDOE SHOTS 
    #1
        naruto_shots = VideoShots.objects.create(
            title='Naruto video shot',
            description="Shot for anime NARUTO",
            slug='naruto-shot',
            )
        naruto_shots.save()
        naruto_shots.video.add(naruto_video)

    #2
        bleach_shots = VideoShots.objects.create(
            title='Bleach video shot',
            description="Shot for anime BLEACH",
            slug='bleach-shot',
            )
        bleach_shots.save()
        bleach_shots.video.add(bleache_video)

    #3
        onepiece_shots = VideoShots.objects.create(
            title='One piece video shot',
            description="Shot for anime ONE PIECE",
            slug='onepiece-shot',
            )
        onepiece_shots.save()
        onepiece_shots.video.add(onepiece_video)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))