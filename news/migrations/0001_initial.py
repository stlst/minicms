# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markdownx.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, max_length=256, verbose_name='Site')),
                ('content', markdownx.models.MarkdownxField()),
                ('description', models.CharField(default='This is the description for article.', max_length=256, verbose_name='Article description')),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Publish Date')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='Update Date', null=True)),
                ('author', models.ForeignKey(verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='Column Name')),
                ('slug', models.CharField(unique=True, max_length=256, verbose_name='Column Site')),
                ('intro', models.CharField(default='', max_length=256, verbose_name='Column Intro')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Column',
                'verbose_name_plural': 'Column',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(verbose_name='Column', to='news.Column'),
        ),
    ]
