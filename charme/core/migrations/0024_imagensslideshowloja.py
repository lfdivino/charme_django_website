# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-26 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20170113_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagensSlideshowLoja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_imagem', models.CharField(max_length=255, verbose_name='Link da imagem')),
            ],
            options={
                'verbose_name_plural': 'Imagens Slideshow Loja',
                'verbose_name': 'Imagem Slideshow Loja',
            },
        ),
    ]
