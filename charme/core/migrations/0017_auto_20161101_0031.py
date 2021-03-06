# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-01 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20161031_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='vitrines',
            name='titulo_vitrine_about',
            field=models.CharField(max_length=180, blank=True, verbose_name='Título vitrine página sobre nós'),
        ),
        migrations.AddField(
            model_name='vitrines',
            name='titulo_vitrine_blog',
            field=models.CharField(max_length=180, blank=True, verbose_name='Título vitrine página blog'),
        ),
        migrations.AddField(
            model_name='vitrines',
            name='titulo_vitrine_contato',
            field=models.CharField(max_length=180, blank=True, verbose_name='Título vitrine página contato'),
        ),
        migrations.AddField(
            model_name='vitrines',
            name='titulo_vitrine_novidades',
            field=models.CharField(max_length=180, blank=True, verbose_name='Título vitrine página novidades'),
        ),
        migrations.AddField(
            model_name='vitrines',
            name='titulo_vitrine_videos',
            field=models.CharField(max_length=180, blank=True, verbose_name='Título vitrine página vídeos'),
        ),
        migrations.AlterField(
            model_name='vitrines',
            name='link_vitrine_blog',
            field=models.CharField(max_length=255, verbose_name='Vitrine página blog'),
        ),
    ]
