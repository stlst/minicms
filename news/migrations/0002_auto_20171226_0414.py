# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 26, 4, 14, 47, 443087, tzinfo=utc), verbose_name='Publish Date', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Update Date', null=True),
        ),
    ]
