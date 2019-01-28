from django.conf.urls import url
from .views import *

urlpatterns =  [
    #当我的访问路径为index/的时候，则将请求交给index_views 试图处理函数去处理
    #完整的请求路径为http://localhost/music/index
    #url(r'^index/$',index_views),
    #当访问路径为　的时候，将请求交给index_views处理
    url(r'^$',index_views),
]