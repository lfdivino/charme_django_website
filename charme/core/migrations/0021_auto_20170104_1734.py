# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-04 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_postshome_imagem_lateral'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postshome',
            name='imagem_lateral',
        ),
        migrations.AddField(
            model_name='postshome',
            name='men_line',
            field=models.BooleanField(default=False, verbose_name='Linha masculina'),
        ),
        migrations.AddField(
            model_name='vitrines',
            name='imagem_lateral_novidade',
            field=models.CharField(blank=True, max_length=255, verbose_name='Imagem lateral das Novidades'),
        ),
    ]