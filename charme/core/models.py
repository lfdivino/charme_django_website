from django.db import models


class Author(models.Model):

    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)

    class Meta:
        verbose_name_plural = 'Autores'
        verbose_name = 'Autor'

    def __str__(self):
        return self.name


class Posts(models.Model):

    title = models.CharField('Titulo', max_length=200)
    imagem = models.CharField('Imagem do Post', max_length=255)
    body = models.TextField('Corpo do Post')
    created_date = models.DateTimeField('Data de criação', auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField('Data de alteração', auto_now_add=False, auto_now=True)
    author = models.ForeignKey(Author)

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'

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
