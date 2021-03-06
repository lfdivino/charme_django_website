# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-08 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20161101_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='vitrines',
            name='sub_titulo_vitrine_about',
            field=models.CharField(blank=True, max_length=180, verbose_name='Sub Título vitrine página sobre nós'),
        ),
        migrations.AddField(
            model_name='vitrines',
            name='sub_titulo_vitrine_blog',
            field=models.CharField(blank=True, max_length=180, verbose_name='Sub Título vitrine página blog'),
        ),
        migrations.AddField(
            model_name='vitrines',
            name='sub_titulo_vitrine_contato',
            field=models.CharField(blank=True, max_length=180, verbose_name='Sub Título vitrine página contato'),
        ),
        migrations.AddField(
            model_name='vitrines',
            name='sub_titulo_vitrine_novidades',
            field=models.CharField(blank=True, max_length=180, verbose_name='Sub Título vitrine página novidades'),
        ),
        migrations.AddField(
            model_name='vitrines',
            name='sub_titulo_vitrine_videos',
            field=models.CharField(blank=True, max_length=180, verbose_name='Sub Título vitrine página vídeos'),
        ),
    ]
