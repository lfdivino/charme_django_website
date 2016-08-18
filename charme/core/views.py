from django.shortcuts import render
from .models import Posts


def home(request):
    return render(request, 'index.html')


def index(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)


def contato(request):
    return render(request, 'contato.html')


def about(request):
    return render(request, 'about.html')
