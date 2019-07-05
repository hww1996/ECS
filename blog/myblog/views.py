#coding: utf-8
import logging
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,render_to_response
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.db import connection
from myblog.models import *
from django import forms
from myblog.forms import *
# Create your views here.

# 注销
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        logging.error(e)
    return HttpResponseRedirect('/')

# 注册
def do_reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                # 注册
                user = User.objects.create(username=reg_form.cleaned_data["username"],
                                    email=reg_form.cleaned_data["email"],
                                    password=make_password(reg_form.cleaned_data["password"]))
                print('fuck')
                user.save()

                # 登录
                user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                login(request, user)
                return HttpResponseRedirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        logging.error(e)
    return render(request, 'reg.html', locals())


def userRegister(request):
    try:
        if request.method=='POST':
            username=request.POST.get('name')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            errors=[]
            registerForm=RegForm({'username':username,'password1':password1,'password2':password2,'email':email})#b********
            if not registerForm.is_valid():
                errors.extend(registerForm.errors.values())
                return HttpResponse('注册成功')
            if password1!=password2:
                return HttpResponse('两次输入密码有误')
            filterResult=User.objects.filter(username=username)#c************
            if len(filterResult)>0:
                return HttpResponse('用户已存在')
            user=User()#d************************
            user.username=username
            user.set_password(password1)
            user.email=email
            user.save()
            #用户扩展信息 profile
            profile=UserProfile()#e*************************
            profile.user_id=user.id
            profile.phone=phone
            profile.save()
            #登录前需要先验证
            newUser=auth.authenticate(username=username,password=password1)#f***************
            if newUser is not None:
                auth.login(request, newUser)#g*******************
                return HttpResponseRedirect(request.POST.get('source_url'))
    except Exception as e:
        logging.error(e)
    return render(request, 'reg.html', locals())

# 登录
def do_login(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 登录
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                    login(request, user)
                else:
                    return render(request, 'failure.html', {'reason': '登录验证失败'})
                return HttpResponseRedirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        logging.error(e)
    return render(request, 'login.html', locals())


def article(request,article_content):
    article=Article.objects.get(title=article_content)
    return render(request, 'article.html' ,{'article':article})


def category(request,category_content):
    context_dict={}
    try:
        category=Category.objects.get(name=category_content)
        context_dict['category_name']=category.name
        article=category.article_set.all()
        paginator = Paginator(article, 5) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        context_dict['contacts']=contacts
        context_dict['category']=Category.objects.all()[:5]
        context_dict['more']=Category.objects.all()[5:]
    except Category.DoesNotExist:
        pass
    return render(request, 'list.html', context_dict)


def all_article(request):
    context_dict={}
    article=Article.objects.all()
    paginator = Paginator(article, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contact = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer, deliver first page.
        contact = paginator.page(1)
    except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
        contact = paginator.page(paginator.num_pages)
    except Article.DoesNotExist:
        pass
    context_dict['contacts']=contact
    context_dict['category']=Category.objects.all()[:5]
    context_dict['more']=Category.objects.all()[5:]
    '''paginator = Paginator(category, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)'''
    return render(request, 'index.html', context_dict)

def allofcategory(request):
    category=Category.objects.all()
    paginator = Paginator(category, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'category_all.html', {'category':contacts})


def introduce(request):
    introduce=Introduce.objects.all()
    return render(request,'introduce.html',{'introduce':introduce})