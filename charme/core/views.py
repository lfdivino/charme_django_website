from django.shortcuts import render
from .models import PostsHome, PostsBlog, Contato
from .forms import ContatoForm


def home(request):
    return render(request, 'index.html')


def index(request):
    posts = PostsHome.objects.all().order_by('created_date')[:7]
    posts_blog = PostsBlog.objects.all().order_by('created_date')[:3]
    context = {
        'posts': posts,
        'posts_blogs': posts_blog,
    }
    return render(request, 'home.html', context)


def novidades(request):
    novidades_ids = PostsHome.objects.all()
    context = {
        'novidades': novidades_ids,
    }
    return render(request, 'novidades.html', context)


def novidades_post(request, novidade_id=None):
    if novidade_id:
        post = PostsHome.objects.filter(id=novidade_id)

    context = {
        'posts': post,
    }
    return render(request, 'novidades-post.html', context)


def blog(request):
    posts = PostsBlog.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'blog.html', context)


def blog_post(request, post_id=None):
    posts = PostsBlog.object.filter(id=post_id)
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
