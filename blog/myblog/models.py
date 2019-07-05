#coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,unique=True,verbose_name=('用户'))#a******
    email=models.EmailField('电邮',max_length=256)
    def __unicode__(self):
        return self.user.username


class Category(models.Model):
    name=models.CharField('文章类别',max_length=32)
    time=models.DateTimeField('第一次创建时间',auto_now_add=True)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering=['-time']


class Article(models.Model):
    title=models.CharField('标题',max_length=128)
    category=models.ManyToManyField(Category)
    First_time=models.DateTimeField('第一次发表时间',auto_now_add=True)
    Revise_time=models.DateTimeField('修改时间')
    sumarry=models.CharField('梗概',max_length=280,default='')
    content = RichTextField('内容')
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-Revise_time']

class Introduce(models.Model):
    title=models.CharField('题目',max_length=128)
    First_time=models.DateTimeField('第一次发表时间',auto_now_add=True)
    Revise_time=models.DateTimeField('修改时间')
    content = RichTextField('内容')
    def __unicode__(self):
        return self.title


class photoupdata(models.Model):
    photo_name = models.CharField('相片名字',max_length = 30,default='请输入相片的名字')
    usage=models.CharField('用于（什么的文章）',max_length=30,default='作死')
    time=models.DateTimeField('时间')
    headImg = models.FileField('上传的图片',upload_to = 'photo')

    def __unicode__(self):
        return self.photo_name
