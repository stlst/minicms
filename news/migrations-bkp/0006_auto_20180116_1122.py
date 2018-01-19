# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180116_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='column',
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(default=None, to='news.Column', verbose_name='Column'),
        ),
    ]
