# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20180117_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='column',
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(to='news.Column', verbose_name='Column'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(unique=True, max_length=256, verbose_name='Site'),
        ),
    ]
