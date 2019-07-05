# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myblog', '0004_remove_userprofile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('username', models.CharField(null=True, max_length=30, verbose_name='用户名', blank=True)),
                ('email', models.EmailField(null=True, max_length=50, verbose_name='邮箱地址', blank=True)),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('article', models.ForeignKey(to='myblog.Article', null=True, verbose_name='文章', blank=True)),
                ('pid', models.ForeignKey(to='myblog.Comment', null=True, verbose_name='父级评论', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='用户', blank=True)),
            ],
            options={
                'verbose_name_plural': '评论',
                'verbose_name': '评论',
            },
        ),
    ]
