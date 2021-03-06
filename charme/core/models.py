# -*- coding: utf-8 -*-
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
    imagem_vitrine = models.CharField('Imagem vitrine home', max_length=255)
    imagem = models.CharField('Imagem do Post', max_length=255)
    brief_body = models.TextField(
        'Resumo da Novidade',
        max_length=200,
        default='Resumo do post da novidade.'
    )
    body = RichTextField('Corpo do Post')
    created_date = models.DateTimeField(
        'Data de criação', auto_now_add=True, auto_now=False
    )
    updated_date = models.DateTimeField(
        'Data de alteração', auto_now_add=False, auto_now=True
    )
    men_line = models.BooleanField("Linha masculina", default=False)

    class Meta:
        verbose_name_plural = 'Posts da Home'
        verbose_name = 'Post da Home'
        ordering = ('-created_date',)

    def __str__(self):
        return self.title


class Depoimentos(models.Model):
    name = models.CharField('Nome do Cliente', max_length=255)
    texto = models.TextField('Depoimento', max_length=400)

    def __str__(self):
        return self.name


class PostCategories(models.Model):

    name = models.CharField('Categoria', max_length=255, default='1')

    class Meta:
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'

    def __str__(self):
        return self.name


class PostsBlog(models.Model):

    title = models.CharField('Titulo', max_length=200)
    imagem_vitrine = models.CharField('Imagem vitrine home', max_length=255)
    imagem = models.CharField('Imagem do Post', max_length=255)
    video = models.CharField('Video', max_length=255, blank=True)
    brief_body = models.TextField(
        'Resumo do Post', max_length=200, default='Resumo do post do blog.'
    )
    body = RichTextField('Corpo do Post')
    created_date = models.DateTimeField(
        'Data de criação', auto_now_add=True, auto_now=False
    )
    updated_date = models.DateTimeField(
        'Data de alteração', auto_now_add=False, auto_now=True
    )
    author = models.ForeignKey(Author)

    class Meta:
        verbose_name_plural = 'Posts do Blog'
        verbose_name = 'Post do Blog'
        ordering = ('-created_date',)

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
        ordering = ('-id',)

    def __str__(self):
        return self.nome


class Videos(models.Model):

    titulo = models.CharField(u'Título', max_length=180)
    link = models.CharField('Link', max_length=255)
    video_destaque = models.BooleanField(u'Vídeo Destaque', default=False)
    descricao = models.CharField('Descrição', max_length=255)
    imagem_capa = models.CharField('Imagem capa', max_length=255)
    category = models.ForeignKey(PostCategories)

    class Meta:
        verbose_name_plural = 'Vídeos'
        verbose_name = 'Vídeo'
        ordering = ('-id',)

    def __str__(self):
        return self.titulo


class ImagensSlideshow(models.Model):

    link_imagem = models.CharField('Link da imagem', max_length=255)

    class Meta:
        verbose_name_plural = 'Imagens Slideshow'
        verbose_name = 'Imagem Slideshow'

    def __str__(self):
        return self.link_imagem


class ImagensSlideshowLoja(models.Model):

    link_imagem = models.CharField('Link da imagem', max_length=255)

    class Meta:
        verbose_name_plural = 'Imagens Slideshow Loja'
        verbose_name = 'Imagem Slideshow Loja'

    def __str__(self):
        return self.link_imagem


class Vitrines(models.Model):

    link_vitrine_blog = models.CharField(
        'Vitrine página blog', max_length=255
    )
    titulo_vitrine_blog = models.CharField(
        'Título vitrine página blog', max_length=180, blank=True
    )
    sub_titulo_vitrine_blog = models.CharField(
        'Sub Título vitrine página blog', max_length=180, blank=True
    )
    link_vitrine_novidades = models.CharField(
        'Vitrine página novidades', max_length=255
    )
    titulo_vitrine_novidades = models.CharField(
        'Título vitrine página novidades', max_length=180, blank=True
    )
    sub_titulo_vitrine_novidades = models.CharField(
        'Sub Título vitrine página novidades', max_length=180, blank=True
    )
    link_vitrine_videos = models.CharField(
        'Vitrine página vídeos', max_length=255
    )
    titulo_vitrine_videos = models.CharField(
        'Título vitrine página vídeos', max_length=180, blank=True
    )
    sub_titulo_vitrine_videos = models.CharField(
        'Sub Título vitrine página vídeos', max_length=180, blank=True
    )
    link_vitrine_about = models.CharField(
        'Vitrine página sobre nós', max_length=255
    )
    titulo_vitrine_about = models.CharField(
        'Título vitrine página sobre nós', max_length=180, blank=True
    )
    sub_titulo_vitrine_about = models.CharField(
        'Sub Título vitrine página sobre nós', max_length=180, blank=True
    )
    link_vitrine_contato = models.CharField(
        'Vitrine página contato', max_length=255
    )
    titulo_vitrine_contato = models.CharField(
        'Título vitrine página contato', max_length=180, blank=True
    )
    sub_titulo_vitrine_contato = models.CharField(
        'Sub Título vitrine página contato', max_length=180, blank=True
    )
    link_vitrine_men = models.CharField(
        'Vitrine página linha men', max_length=255
    )
    titulo_vitrine_men = models.CharField(
        'Título vitrine página linha men', max_length=180, blank=True
    )
    sub_titulo_vitrine_men = models.CharField(
        'Sub Título vitrine página linha men', max_length=180, blank=True
    )
    link_vitrine_loja = models.CharField(
        'Vitrine página loja', max_length=255
    )
    titulo_vitrine_loja = models.CharField(
        'Título vitrine página loja', max_length=180, blank=True
    )
    sub_titulo_vitrine_loja = models.CharField(
        'Sub Título vitrine página loja', max_length=180, blank=True
    )
    imagem_lateral_novidade = models.CharField(
        'Imagem lateral das Novidades', max_length=255, blank=True
    )

    class Meta:
        verbose_name_plural = 'Vitrines do site'
        verbose_name = 'Vitrine do site'

    def __str__(self):
        return 'Vitrines'
