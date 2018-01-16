# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20171226_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(unique=True, max_length=256, verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='column',
            name='slug',
            field=models.CharField(unique=True, max_length=256, verbose_name='Column Site'),
        ),
    ]
