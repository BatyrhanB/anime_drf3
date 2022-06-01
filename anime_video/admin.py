from django.contrib import admin
from anime_video.models import *

class VideoCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug']
class PersonageAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)} 
    search_fields = ['title', 'description']

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} 
    date_hierarchy = 'publish_date'
    list_display = ['title', 'slug', 'publish_date', 'category', 'is_public',
        'allow_comments']
    list_filter = ['publish_date', 'modified_date',
        'is_public', 'allow_comments']
    search_fields = ['title', 'description', 'tags']
    fieldsets = (
        ('Video Details', {'fields': [
            'title', 'slug', 'category', 'genres', 'personages', 'description', 'is_public',
            'allow_comments', 'publish_date'    
        ]}),
    )   

class ShotsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)} 
    search_fields = ['title', 'description']


admin.site.register(Video, VideoAdmin)
admin.site.register(VideoCategory, VideoCategoryAdmin)
admin.site.register(Personage, PersonageAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(VideoShots, ShotsAdmin)