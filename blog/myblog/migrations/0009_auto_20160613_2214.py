# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_introduce'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='category',
            name='time',
            field=models.DateTimeField(verbose_name='第一次创建时间', auto_now_add=True, default=datetime.datetime(2016, 6, 13, 14, 14, 18, 565853, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
