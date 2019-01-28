from django.conf.urls import url
from .views import *

urlpatterns =[
    #如果访问路径是login/的时候，交给index_views处理
    url(r'^login/$',login_views),
    url(r'^register/$',register_views),
    url(r'^$',index_views),

    url(r'^01-temp/$',temp_views),
    url(r'^02-temp/$',temp02_views),
    url(r'^03-var/$',var_views),

    url(r'^04-static/$',static_views),

    url(r'^05-alias01/$',alias01_views,name='a01'),
    url(r'^06-alias02/(\d{4})/$',alias02_views,name='a02'),

]