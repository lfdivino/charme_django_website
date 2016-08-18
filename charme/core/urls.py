from django.conf.urls import url
from .views import index, contato, about

urlpatterns = [
    url(r'^blog/', index, name='index'),
    url(r'^blog/contato/', contato, name='contato'),
    url(r'^blog/about/', about, name='about'),
]