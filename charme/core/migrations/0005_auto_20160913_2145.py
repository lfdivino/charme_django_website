# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-13 21:45
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160830_0107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postsblog',
            options={'verbose_name': 'Post do Blog', 'verbose_name_plural': 'Posts do Blog'},
        ),
        migrations.AlterModelOptions(
            name='postshome',
            options={'verbose_name': 'Post da Home', 'verbose_name_plural': 'Posts da Home'},
        ),
        migrations.AlterField(
            model_name='postsblog',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='Corpo do Post'),
        ),
        migrations.AlterField(
            model_name='postshome',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='Corpo do Post'),
        ),
    ]