# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='html_body',
            field=models.CharField(default='This is html_body', max_length=1024, verbose_name='Html'),
        ),
    ]
