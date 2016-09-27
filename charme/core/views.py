from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import PostsHome, PostsBlog, Contato
from .forms import ContatoForm


def home(request):
    return render(request, 'index.html')


def index(request):
    posts = PostsHome.objects.all().order_by('-created_date')[:7]
    posts_blog = PostsBlog.objects.all().order_by('-created_date')[:3]
    context = {
        'posts': posts,
        'posts_blogs': posts_blog,
    }
    return render(request, 'home.html', context)


def novidades_page(request):
    novidades_ids = PostsHome.objects.all().order_by('-created_date')
    paginator = Paginator(novidades_ids, 8)

    page = request.GET.get('page')
    try:
        novidades = paginator.page(page)
    except PageNotAnInteger:
        novidades = paginator.page(1)
    except EmptyPage:
        novidades = paginater.page(paginator.num_pages)

    context = {
        'novidades': novidades,
    }
    return render(request, 'novidades.html', context)


def novidades_post(request, novidade_id=None):
    if novidade_id:
        post = PostsHome.objects.filter(id=novidade_id)

    context = {
        'posts': post,
    }
    return render(request, 'novidades-post.html', context)


def blog_page(request):
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
        'posts': posts,
    }

    return render(request, 'blog.html', context)


def blog_post(request, post_id=None):
    posts = PostsBlog.objects.filter(id=post_id)
    context = {
        'posts': posts,
    }

    return render(request, 'blog-post.html', context)


def contato(request):
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
            'flag_enviado': True,
            'form': ContatoForm(),
        }
    else:
        context = {
            'flag_enviado': False,
            'form': ContatoForm(),
        }

    return render(request, 'contato.html', context)


def about(request):
    return render(request, 'about.html')
