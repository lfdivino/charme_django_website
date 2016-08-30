from django.contrib import admin
from .models import PostsHome, PostsBlog, Author, Contato

admin.site.register(PostsHome)
admin.site.register(PostsBlog)
admin.site.register(Author)
admin.site.register(Contato)
