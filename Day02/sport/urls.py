from django.conf.urls import url
from .views import *

urlpatterns = [
    #当访问路径为index/将请求交给index_views
    url(r'^index/$',index_views),
]