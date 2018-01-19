# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180116_1025'),
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
    ]
