from django.db import models
from userinfo.models import *
from sale.models import *

ORDER_CHOICES = (
    (0,'待支付'),
    (1,'已支付'),
    (2,'订到取消'),
    (3,'订单失败'),
    (4,'订单完成'),
)

# Create your models here.
class Cartinfo(models.Model):
    price = models.DecimalField('价格',max_digits=9,decimal_places=2)
    buser = models.ForeignKey(UserInfo)
    car = models.ForeignKey(Carinfo)

    def __str__(self):
        return self.buser.username


class OrderInfo(models.Model):
    buser = models.ForeignKey(UserInfo,related_name='buser')
    suser = models.ForeignKey(UserInfo,related_name='suser')
    car = models.TextField('汽车')
    price = models.DecimalField('价格',max_digits=9,decimal_places=2)
    orderNo = models.CharField('订单号',max_length=50)
    status = models.IntegerField('订单状态',choices=ORDER_CHOICES,default=0)
    datetime = models.DateTimeField('时间',auto_now=True)
    isDelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return self.orderNo
