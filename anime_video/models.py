from django.db import models
from datetime import datetime
from django.conf import settings
from django.urls import reverse
from django.core.validators import FileExtensionValidator


class VideoCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        help_text='Удобный URL-адрес для категории',
    )
    description = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

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
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True,
        help_text='Удобный URL-адрес для видеоклипа.')
    image = models.ImageField(upload_to='image/')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
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
    image = models.ImageField("Изображение", upload_to='video_shots/')
    video = models.ForeignKey(Video, verbose_name='Видео', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из видео'
        verbose_name_plural = 'Кадры из видео'

class BasicVideo(Video):
    pass

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'   


class HTML5Video(models.Model):
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

    video_type = models.IntegerField(
        choices=VIDEO_TYPE,
        default=WEBM,
        help_text='Тип видео'
    )
    video_file = models.FileField(
        upload_to='videos/html5/',
        help_text='Файл, который вы хотите загрузить. Убедитесь, что это правильный формат.',
    )

    basic_video = models.ForeignKey(BasicVideo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Html 5 видео'
        verbose_name_plural = 'Html 5 видео'

class EmbedVideo(Video):
    video_url = models.URLField(null=True, blank=True)
    video_code = models.TextField(
        null=True,
        blank=True,
        help_text='Используйте код для встраивания видео вместо URL-адреса, если ваш интерфейс не поддерживает встраивание только с помощью URL-адреса.'
    )
    class Meta:
        verbose_name = 'Встроенное видео'
        verbose_name_plural = 'Встроенное видео'


class FlashVideo(Video):
    original_file = models.FileField(
        upload_to="videos/flash/source/",
        null=True,
        blank=True,
        help_text='Убедитесь, что видео, которое вы загружаете, имеет битрейт аудио не менее 16. Кодирование не будет работать при более низком битрейте звука.'
    )

    flv_file = models.FileField(
        upload_to='videos/flash/flv/',
        null=True,
        blank=True,
        help_text='Если у вас уже есть закодированное флэш-видео, загрузите его здесь (кодирование не требуется).'
    )

    thumbnail = models.ImageField(
        blank=True,
        null=True, 
        upload_to='videos/flash/thumbnails/',
        help_text='Если вы загрузили клип flv, который уже был закодирован, вам также нужно будет загрузить миниатюру. Если вы планируете использовать django-video для кодирования, вам не нужно загружать миниатюру, так как django-video создаст ее для вас'
    )

    encode = models.BooleanField(
        default=False,
        help_text='Закодируйте или перекодируйте клип. Если вы только хотели изменить некоторую информацию об элементе и не хотите повторно кодировать клип, убедитесь, что этот параметр не выбран.'
    )

    class Meta:
        verbose_name = "Флэш-Видео"
        verbose_name_plural = "Флэш-Видео"

    def get_player_size(self):
        size = getattr(settings, 'VIDEOSTREAM_SIZE', '320x240').split('x')
        return "width: %spx; height: %spx;" % (size[0], size[1])