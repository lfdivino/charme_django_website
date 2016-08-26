from django.shortcuts import render
from .models import Posts, Contato
from .forms import ContatoForm


def home(request):
    return render(request, 'index.html')


def index(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)


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
