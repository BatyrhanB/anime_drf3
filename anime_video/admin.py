from django.contrib import admin

class VideoCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug']

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} 
    date_hierarchy = 'publish_date'
    list_display = ['title', 'slug', 'publish_date', 'is_public',
        'allow_comments', 'author']
    list_filter = ['created_date', 'publish_date', 'modified_date',
        'is_public', 'allow_comments']
    search_fields = ['title', 'description', 'tags']
    fieldsets = (
        ('Video Details', {'fields': [
            'title', 'slug', 'description', 'tags', 'categories', 'is_public',
            'allow_comments', 'publish_date', 'author',
        ]}),
    )
