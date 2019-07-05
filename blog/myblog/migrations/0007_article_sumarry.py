# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20160523_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sumarry',
            field=models.CharField(max_length=280, verbose_name='梗概', default=''),
        ),
    ]
