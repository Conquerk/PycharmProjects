from django.http import HttpResponse


def show_views(request):
    return HttpResponse('我的第一个django处理程序')

def sh_views(request):
    return HttpResponse('访问路径中包含sh的处理程序')

#匹配访问路径为/show/四位数字/
#year表示四位数字
def show1_views(request,year):
    return HttpResponse("传递进来为年份为："+year)

def show2_views(request,year,month,day):
    return HttpResponse('传递过来的年%s月%s日%s'%(year,month,day))

def show3_views(request,name,age):
    return HttpResponse('传递过来的姓名：%s,年龄：%d'%(name,age))
