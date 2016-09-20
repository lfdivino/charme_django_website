from django.db import models

from ckeditor.fields import RichTextField


class Author(models.Model):

    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)

    class Meta:
        verbose_name_plural = 'Autores'
        verbose_name = 'Autor'

    def __str__(self):
        return self.name


class PostsHome(models.Model):

    title = models.CharField('Titulo', max_length=200)
    imagem = models.CharField('Imagem do Post', max_length=255)
    brief_body = models.TextField('Resumo da Novidade', max_length=200, default='Resumo do post da novidade.')
    body = RichTextField('Corpo do Post')
    created_date = models.DateTimeField('Data de criação', auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField('Data de alteração', auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Posts da Home'
        verbose_name = 'Post da Home'

    def __str__(self):
        return self.title


class PostsBlog(models.Model):

    title = models.CharField('Titulo', max_length=200)
    imagem = models.CharField('Imagem do Post', max_length=255)
    video = models.CharField('Video', max_length=255)
    brief_body = models.TextField('Resumo do Post', max_length=200, default='Resumo do post do blog.')
    body = RichTextField('Corpo do Post')
    created_date = models.DateTimeField('Data de criação', auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField('Data de alteração', auto_now_add=False, auto_now=True)
    author = models.ForeignKey(Author)

    class Meta:
        verbose_name_plural = 'Posts do Blog'
        verbose_name = 'Post do Blog'

    def __str__(self):
        return self.title


class Contato(models.Model):

    nome = models.CharField('Nome', max_length=200)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail')
    mensagem = models.TextField('Mensagem')

    class Meta:
        verbose_name_plural = 'Contatos'
        verbose_name = 'Contato'

    def __str__(self):
        return self.nome
