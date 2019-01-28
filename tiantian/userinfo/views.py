from django.shortcuts import render, redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist
import logging
from django.contrib.auth.hashers import make_password,check_password
from django.db import DatabaseError
# Create your views here.

auth_check = 'MarceArhut'


def register_in(request):
    return render(request,'register.html')

def register_(request):
    #1.判断传递过来的方法
    #2.获取用户
    #3.判断用户是否存在
    #4.判断两次密码是否一致
    #5.如果两次密码一致则注册用户(密码加密)
    #6.返回
    if request.method == 'POST':
        #声明用户类
        new_user = Userinfo()
        #获取用户
        new_user.uname = request.POST.get('user_name')
        #查询
        try:
            a=Userinfo.objects.filter(uname=new_user.uname)
            if a:
                return render(request,'register.html',{'message':'该用户已经存在'})
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if request.POST.get('pwd') != request.POST.get('cpwd'):
            return render(request,'register.html',{'message':'两次密码不一致'})
        new_user_upwd = make_password(request.POST.get('pwd'),auth_check,'pbkdf2_sha1')
        #参数１:加密的密码
        #参数２:任意的字符串
        #参数３：加密方式
        new_user.upassword = new_user_upwd
        new_user.email = request.POST.get('email')
        try:
            new_user.save()
        except DatabaseError as e:
            logging.warning(e)
        return render(request,'login.html')

#重定向登录界面
def signin(request):
    return render(request,'login.html')

def login_(request):
    #1.判断传递方式
    #2.获取用户，密码
    #3.判断用户是否注册
    #4.判断密码是否正确
    #5.存session
    if request.method == 'POST':
        user = Userinfo()
        user.uname = request.POST.get('user_name')
        user.upassword = request.POST.get('pwd')
        try:
            find_user = Userinfo.objects.filter(uname=user.uname)
            if len(find_user) <=0:
                return render(request,'login.html',{'message':'该用户未注册'})
            #参数１明文密码
            #参数２ 加密后的密文密码
            if not check_password(user.upassword,find_user[0].upassword):
                return render(request,'login.html',{'message':'用户名或者密码错误'})
        except ObjectDoesNotExist as e:
            logging.warning(e)
        request.session['user_id'] = find_user[0].id
        request.session['user_name'] = user.uname
        #return render(request,'login.html',{'message':'登陆成功'})
        return redirect('/')

def login_out(request):
    try:
        if request.session['user_name']:
            del request.session['user_id']
            del request.session['user_name']
    except KeyError as e:
        logging.warning(e)
    return redirect('/')
















