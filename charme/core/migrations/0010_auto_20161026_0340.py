# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-26 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_videos_video_destaque'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ('-id',), 'verbose_name': 'Contato', 'verbose_name_plural': 'Contatos'},
        ),
        migrations.AlterModelOptions(
            name='imagensslideshow',
            options={'verbose_name': 'Imagem Slideshow', 'verbose_name_plural': 'Imagens Slideshow'},
        ),
        migrations.AlterModelOptions(
            name='postsblog',
            options={'ordering': ('-created_date',), 'verbose_name': 'Post do Blog', 'verbose_name_plural': 'Posts do Blog'},
        ),
        migrations.AlterModelOptions(
            name='postshome',
            options={'ordering': ('-created_date',), 'verbose_name': 'Post da Home', 'verbose_name_plural': 'Posts da Home'},
        ),
        migrations.AlterModelOptions(
            name='videos',
            options={'ordering': ('-id',), 'verbose_name': 'Vídeo', 'verbose_name_plural': 'Vídeos'},
        ),
        migrations.AddField(
            model_name='imagensslideshow',
            name='show_home',
            field=models.BooleanField(default=True, verbose_name='Mostar na Home?'),
        ),
    ]
