# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_article_sumarry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduce',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='题目')),
                ('First_time', models.DateTimeField(auto_now_add=True, verbose_name='第一次发表时间')),
                ('Revise_time', models.DateTimeField(verbose_name='修改时间')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
            ],
        ),
    ]
