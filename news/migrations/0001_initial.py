# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
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
                ('slug', models.CharField(max_length=256, verbose_name='Site', db_index=True)),
                ('content', models.TextField(default='', verbose_name='Content', blank=True)),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
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
                ('slug', models.CharField(max_length=256, verbose_name='Column Site', db_index=True)),
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
            field=models.ManyToManyField(to='news.Column', verbose_name='Column'),
        ),
    ]
