from django.contrib import admin
from anime_video.models import *

class HTML5VideoInline(admin.TabularInline):
    model = HTML5Video

class VideoCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug']

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} 
    date_hierarchy = 'publish_date'
    list_display = ['title', 'slug', 'publish_date', 'is_public',
        'allow_comments']
    list_filter = ['publish_date', 'modified_date',
        'is_public', 'allow_comments']
    search_fields = ['title', 'description', 'tags']
    fieldsets = (
        ('Video Details', {'fields': [
            'title', 'slug', 'description', 'is_public',
            'allow_comments', 'publish_date'    
        ]}),
    )


class FlashVideoAdmin(VideoAdmin):
    list_display = VideoAdmin.list_display + ['encode']
    list_filter = VideoAdmin.list_filter + ['encode']
    fieldsets = VideoAdmin.fieldsets + (
        ('Video Source', {'fields': [
            'original_file',
            'flv_file',
            'thumbnail', 
            'encode'
        ]}),
    )

class EmbedVideoAdmin(VideoAdmin):
    list_display = VideoAdmin.list_display + ['video_url']
    fieldsets = VideoAdmin.fieldsets + (
        ('Video Source', {'fields': [
            'video_url',
            'video_code',
        ]}),
    )

class PersonageAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)} 
    search_fields = ['title', 'description']

class BasicVideoAdmin(VideoAdmin):
    inlines = [HTML5VideoInline]


admin.site.register(VideoCategory, VideoCategoryAdmin)
admin.site.register(FlashVideo, FlashVideoAdmin)
admin.site.register(EmbedVideo, EmbedVideoAdmin)
admin.site.register(BasicVideo, BasicVideoAdmin)
admin.site.register(Personage, PersonageAdmin)
admin.site.register(Genre, GenreAdmin)