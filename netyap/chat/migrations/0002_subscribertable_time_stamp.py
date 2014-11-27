# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribertable',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 27, 8, 41, 11, 274670), auto_now_add=True),
            preserve_default=False,
        ),
    ]
