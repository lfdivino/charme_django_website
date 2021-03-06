"""charme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .core.views import home, index, contato, about,\
    novidades_page, men_page, loja, novidades_post, video

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^index/', index, name='index'),
    url(r'^novidades/$', novidades_page, name='novidades'),
    url(
        r'^novidades/post/(?P<novidade_id>[0-9]+)/$',
        novidades_post,
        name='novidade-post'
    ),
    url(r'men/$', men_page, name='men'),
    url(r'^contato/', contato, name='contato'),
    url(r'^loja/', loja, name='loja'),
    url(r'^about/', about, name='about'),
    url(r'^videos/(?P<category>[0-9]+)/$', video, name='video'),
    url(r'^videos/$', video, name='videos'),
    url(r'^admin/', admin.site.urls),
]
