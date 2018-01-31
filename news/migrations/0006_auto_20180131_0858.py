# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180131_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(default='This is the description for article.', max_length=256, verbose_name='Article description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='html_body',
            field=models.TextField(default='This is html_body', verbose_name='Html'),
        ),
    ]
