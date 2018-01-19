# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20180117_0646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='column',
        ),
    ]
