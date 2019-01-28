from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

# Create your views here.

def request_views(request):
    # print(dir(request))
    # print(request.META)
    scheme = request.scheme
    body = request.body
    path = request.get_host()
    method = request.method
    get = request.GET
    post = request.POST
    cookies = request.COOKIES

    return render(request,'01-request.html',locals())

def referer_views(request):
    #获取请求元地址如果没有则获取一个/
    referer = request.META.get('HTTP_REFERER','/')
    return HttpResponse('Referer is :'+referer)

def login_views(request):
    if request.method == 'GET':
        return render(request,'03-login.html')
    else:
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        print("用户名：%s,密码：%s"%(uname,upwd))
        return HttpResponse('POST 接收成功')

def form_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request,'04-form.html',locals())
    else:
        #1.通过RemarkForm的构造，接收请求提交的数据
        form = RemarkForm(request.POST)
        #2.通过验证
        if form.is_valid():
        #3.取值
            cd = form.cleaned_data
            print(cd)
        return HttpResponse('取值成功')

def modelform_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request,'05-modelsform.html',locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(**form.cleaned_data)
            print('uname:%s,upwd:%s,uemail:%s'%(user.uname,user.upwd,user.uemail))
        return HttpResponse('OK')