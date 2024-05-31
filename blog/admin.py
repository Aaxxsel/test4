from django.contrib import admin

from blog.models import PostSite


@admin.register(PostSite)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'slug']
    list_display = ('id', 'title', 'text', 'date_db', 'slug')
    list_display_links = ('id', 'title')
    ordering = ('-date_db', 'title')
    list_per_page = 4
    search_fields = ['title']
    list_filter = ['date_db', 'slug']
