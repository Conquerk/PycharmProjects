from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.urls import reverse


def login_views(request):
    return HttpResponse('这是index中的login路径')

def register_views(request):
    return HttpResponse('这是index中的register路径')

def index_views(request):
    return HttpResponse('这是index中的__路径')

def temp_views(request):
    #加载模板
    t = loader.get_template('01-temp.html')
    #将模板渲染成字符串
    html = t.render()
    #将字符串相应给客户端
    return HttpResponse(html)

def temp02_views(request):
    return render(request,'01-temp.html')

def var_views(request):
    str = '这是模板中的字符串'
    num = 3306
    tup = ('西厢记','金瓶梅','红楼梦','三国演义')
    list = ['张三','李四','王五','赵六']
    dic = {
        'BJ':'北京',
        'SZ':'深圳',
        'SH':'上海',
    }
    dog = Animal()
    ret = sayHi()
    return render(request,'02-var.html',locals())


def sayHi():
    return 'Hello,this is a function ....'

class Animal(object):
    name = '旺财'
    def eat(self):
        return 'eat '+self.name

def static_views(request):
    return render(request,'04-static.html')

def alias01_views(request):
    #通过ａ０２以及对应的参数，反向解析生成ａ０２的地址
    url = reverse('a02',args=('2015',))
    print(url+'--a02的地址')
    return render(request,'05-alias.html')

def alias02_views(request,year):
    print('年份为：%s'%year)
    #通过ａ０１反向生成ａ０１的地址
    url = reverse('a01')
    print(url+"--a01的地址")
    return render(request,'06-alias.html')
