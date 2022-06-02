from django.db import models
from datetime import datetime
from django.conf import settings
from django.urls import reverse
from django.core.validators import FileExtensionValidator


class Anime(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        help_text='Удобный URL-адрес для категории',
    )
    description = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('category-list', [self.slug])


class Genre(models.Model):
    title = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    slug = models.SlugField(unique=True,
        help_text='Удобный URL-адрес для жанра.')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('genre-detail', [self.slug])

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Personage(models.Model):
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to="actors/")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('personage-detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class Video(models.Model):
    OGG = 0
    WEBM = 1
    MP4 = 2
    FLASH = 3
    VIDEO_TYPE = (
        (OGG, 'video/ogg'),
        (WEBM, 'video/webm'),
        (MP4, 'video/mp4'),
        (FLASH, 'video/flv'),
    )
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True,
        help_text='Удобный URL-адрес для видеоклипа.')
    image = models.ImageField(upload_to='image/')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    video_type = models.IntegerField(
        choices=VIDEO_TYPE,
        default=WEBM,
        help_text='Тип видео'
    )
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    category = models.ForeignKey(
        Anime, verbose_name='Аниме', on_delete=models.SET_NULL, null=True, related_name='videos'
    )
    personages = models.ManyToManyField(Personage, verbose_name='Персонажи')
    allow_comments = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)    
    create_at = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        # ordering = ('-publish_date')
        get_latest_by = 'publish_date'


    def __str__(self):
        return self.title

    def __unicode__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('video-detail', (), { 
            'year': self.publish_date.strftime("%Y"),
            'month': self.publish_date.strftime("%b"),
            'day': self.publish_date.strftime("%d"), 
            'slug': self.slug 
        })

    def save(self, *args, **kwargs):
        self.modified_date = datetime.now()
        if self.publish_date == None and self.is_public:
            self.publish_date = datetime.now()
        super(Video, self).save(*args, **kwargs)


class VideoShots(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    slug = models.SlugField(unique=True,
        help_text='Удобный URL-адрес для видеокадров.')
    image = models.ImageField('Изображение', upload_to='video_shots/')
    video = models.ForeignKey(Video, verbose_name='Видео', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из видео'
        verbose_name_plural = 'Кадры из видео'
