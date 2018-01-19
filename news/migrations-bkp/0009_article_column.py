# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_remove_article_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(default=None, verbose_name='Column', to='news.Column'),
        ),
    ]
