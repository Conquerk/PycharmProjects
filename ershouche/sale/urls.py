from django.conf.urls import url
from sale import views
urlpatterns = [
    url(r'photo',views.Upimg,name = 'upimg')
]