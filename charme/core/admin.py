from django.contrib import admin
from .models import PostsHome, PostsBlog, Author, Contato, Videos, ImagensSlideshow


class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


class PostHomeModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'brief_body', 'created_date')
    search_fields = ('title', 'brief_body')
    list_filter = ('created_date',)


class PostBlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'brief_body', 'created_date')
    search_fields = ('title', 'author', 'brief_body')
    list_filter = ('created_date',)


class ContatoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'mensagem')
    search_fields = ('nome', 'telefone', 'email', 'mensagem')
    list_filter = ('nome',)


class VideosModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link', 'video_destaque')
    search_fields = ('titulo', 'video_destaque')
    list_filter = ('video_destaque',)

admin.site.register(PostsHome, PostHomeModelAdmin)
admin.site.register(PostsBlog, PostBlogModelAdmin)
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Contato, ContatoModelAdmin)
admin.site.register(Videos, VideosModelAdmin)
admin.site.register(ImagensSlideshow)
