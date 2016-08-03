# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('First_time', models.DateTimeField(verbose_name='第一次发表时间', auto_now_add=True)),
                ('Revise_time', models.DateTimeField(verbose_name='修改时间')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
            ],
            options={
                'ordering': ['-Revise_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=32, verbose_name='文章类别')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('phone', models.CharField(max_length=32, verbose_name='电话')),
                ('email', models.EmailField(max_length=256, verbose_name='电邮')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='myblog.Category'),
        ),
    ]
