from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import DatabaseError
from django.contrib.auth.hashers import make_password,check_password
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import json
import logging
from django.contrib.auth import authenticate,login,logout


# Create your views here.


def register(request):
    if request.method == 'POST':
        new_user = UserInfo()
        new_user.username = request.POST.get('username')
        try:
            olduser = UserInfo.objects.filter(username=new_user.username)
            if len(olduser)>0:
                return render(request,'register.html',{'message':'用户名已存在'})
                #return HttpResponse(json.dumps({'result':False,'data':"",'error':'用户名已存在'}))
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if request.POST.get('pwd') == request.POST.get('cpwd'):
            return render(request,'register.html',{'message':'两次密码不一致'})
        new_user.password = make_password(request.POST.get('pwd'),None,'pbkdf2_sha1')
        new_user.save()
        return render(request,'login.html')
        #return HttpResponse(json.dumps({'result': True, 'data':'注册成功','error':''}))

def login_(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('pwd')
        #用户名密码为空
        user = authenticate(username=uname,password=pwd)
        if user is not None and user.is_active:
            login(request,user)
            url = request.COOKIES.get('source_url','')
            return HttpResponse(json.dumps({'result':True,'data':'此用户已登录','error':''}))

def logout_(request):
    logout(request)
    return render(request,'index.html')


def register_(request):
    #验证用户是否具有合法性
    if request.user.is_authenticated():
        pass


    


