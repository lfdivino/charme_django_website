from django.contrib import admin
from .models import PostsHome, PostsBlog, Author, Contato, Videos, ImagensSlideshow


class VideosModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link', 'video_destaque')

admin.site.register(PostsHome)
admin.site.register(PostsBlog)
admin.site.register(Author)
admin.site.register(Contato)
admin.site.register(Videos, VideosModelAdmin)
admin.site.register(ImagensSlideshow)
