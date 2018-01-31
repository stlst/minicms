# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_html_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='html_body',
            field=models.CharField(default='This is html_body', max_length=256, verbose_name='Html'),
        ),
    ]
