from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import PostsHome, PostsBlog, Contato, Videos, ImagensSlideshow, Vitrines, PostCategories
from .forms import ContatoForm


def home(request):
    return render(request, 'index.html')


def index(request):
    posts = PostsHome.objects.all().order_by('-created_date')[:7]
    posts_blog = PostsBlog.objects.all().order_by('-created_date')[:3]
    imagens_slideshow = ImagensSlideshow.objects.all().order_by('-id')[:4]

    context = {
        'posts': posts,
        'posts_blogs': posts_blog,
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


def blog_page(request, category=None):
    vitrines = Vitrines.objects.all().order_by('id')
    categories = PostCategories.objects.all()
    if category:
        posts_ids = PostsBlog.objects.filter(category=category).order_by('-created_date')
    else:
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
        'categories': categories,
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


def video(request):
    vitrines = Vitrines.objects.all().order_by('id')
    videos_ids = Videos.objects.all().order_by('-id')
    video_destaque = Videos.objects.all().filter(video_destaque=True).order_by('-id')
    paginator = Paginator(videos_ids, 12)

    page = request.GET.get('page')
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    context = {
        'vitrines': vitrines[0],
        'videos': videos,
        'video_destaque': video_destaque[0] if video_destaque else False,
    }

    return render(request, 'videos.html', context)
