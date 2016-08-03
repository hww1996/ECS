# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_auto_20160613_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='photoupdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo_name', models.CharField(verbose_name='相片名字', default='请输入相片的名字', max_length=30)),
                ('usage', models.CharField(verbose_name='用于（什么的文章）', default='作死', max_length=30)),
                ('time', models.DateTimeField(verbose_name='时间')),
                ('headImg', models.FileField(verbose_name='上传的图片', upload_to='./myblog/static/photo/')),
            ],
        ),
    ]
