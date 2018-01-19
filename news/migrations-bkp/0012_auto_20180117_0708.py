# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20180117_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='column',
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(default=None, verbose_name='Column', to='news.Column'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True, max_length=256, verbose_name='Site'),
        ),
    ]
