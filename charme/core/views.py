from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import PostsHome, PostsBlog, Contato, Videos, ImagensSlideshow, Vitrines, PostCategories
from .forms import ContatoForm
from django.db.models.functions import Lower
import random


def home(request):
    return render(request, 'index.html')


def index(request):
    newest_posts = PostsHome.objects.all().filter(men_line=False).order_by('-created_date')[:4]
    posts_list = PostsHome.objects.all().filter(men_line=False)[:3]
    posts = [
        posts_list[
            random.randint(0, len(posts_list)-1),
            random.randint(0, len(posts_list)-1),
            random.randint(0, len(posts_list)-1),
        ]
    ]
    men_posts = PostsHome.objects.all().filter(
        men_line=True
    ).order_by('-created_date')[:3]
    imagens_slideshow = ImagensSlideshow.objects.all().order_by('-id')[:4]

    context = {
        'newest_posts': newest_posts,
        'posts': posts,
        'men_posts': men_posts,
        'imagens_slideshow': imagens_slideshow,
    }
    return render(request, 'home.html', context)


def novidades_page(request):
    vitrines = Vitrines.objects.all().order_by('id')
    novidades_ids = PostsHome.objects.all().order_by('-created_date')
    paginator = Paginator(novidades_ids, 8)

    page = request.GET.get('page')
    try:
        novidades = paginator.page(page)
    except PageNotAnInteger:
        novidades = paginator.page(1)
    except EmptyPage:
        novidades = paginator.page(paginator.num_pages)

    context = {
        'vitrines': vitrines[0],
        'novidades': novidades,
    }
    return render(request, 'novidades.html', context)


def novidades_post(request, novidade_id=None):
    vitrines = Vitrines.objects.all().order_by('id')
    if novidade_id:
        post = PostsHome.objects.filter(id=novidade_id)

    context = {
        'vitrines': vitrines[0],
        'posts': post,
    }
    return render(request, 'novidades-post.html', context)


def blog_page(request):
    vitrines = Vitrines.objects.all().order_by('id')
    posts_ids = PostsBlog.objects.all().order_by('-created_date')

    paginator = Paginator(posts_ids, 8)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'vitrines': vitrines[0],
        'posts': posts,
    }

    return render(request, 'blog.html', context)


def blog_post(request, post_id=None):
    vitrines = Vitrines.objects.all().order_by('id')
    posts = PostsBlog.objects.filter(id=post_id)
    context = {
        'vitrines': vitrines[0],
        'posts': posts,
    }

    return render(request, 'blog-post.html', context)


def contato(request):
    vitrines = Vitrines.objects.all().order_by('id')
    form = ContatoForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data.get("name")
        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")

        contato_site = Contato(
            nome=name,
            telefone=phone,
            email=email,
            mensagem=message
        )
        contato_site.save()

        context = {
            'vitrines': vitrines[0],
            'flag_enviado': True,
            'form': ContatoForm(),
        }
    else:
        context = {
            'vitrines': vitrines[0],
            'flag_enviado': False,
            'form': ContatoForm(),
        }

    return render(request, 'contato.html', context)


def about(request):
    vitrines = Vitrines.objects.all().order_by('id')
    context = {
        'vitrines': vitrines[0],
    }
    return render(request, 'about.html', context)


def video(request, category=None):
    vitrines = Vitrines.objects.all().order_by('id')
    categories = PostCategories.objects.all().order_by(Lower('name'))
    print (categories)
    if category:
        videos_ids = Videos.objects.filter(
            category=category, video_destaque=False).order_by('-id')
    else:
        videos_ids = Videos.objects.all().filter(
            video_destaque=False).order_by('-id')
    video_destaque = Videos.objects.all().filter(
        video_destaque=True).order_by('-id')
    paginator = Paginator(videos_ids, 6)

    page = request.GET.get('page')
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    context = {
        'vitrines': vitrines[0],
        'categories': categories,
        'videos': videos,
        'video_destaque': video_destaque[0] if video_destaque else False,
    }

    return render(request, 'videos.html', context)
