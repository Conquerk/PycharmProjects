from django.db import models
from userinfo.models import *

CAR_CHOISE = (
    (0,'审核中'),
    (1,'已审核'),
    (2,'待审核'),
    (3,'未通过')
)

# Create your models here.

class Brand(models.Model):
    title = models.CharField('名称',max_length=30)
    logo = models.ImageField(verbose_name='logo',upload_to='img/logo',default='')
    newprice = models.DecimalField(verbose_name='新车价格',max_digits=9,decimal_places=2)
    isDelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return self.title


class Carinfo(models.Model):
    brand = models.ForeignKey(Brand)
    regist_data = models.DateField('上牌日期')
    engineNo = models.CharField('发动机号',max_length=50,null=False)
    mileage = models.IntegerField(verbose_name='公里数')
    record = models.CharField('维修记录',max_length=200)
    price = models.DecimalField(verbose_name='期望成交价',max_digits=8,decimal_places=2)
    picture = models.ImageField('图片',upload_to='img/car')
    formalities = models.BooleanField('手续是否齐全',default=False)
    debt = models.BooleanField('是否有债务',default=False)
    promise = models.TextField(verbose_name='卖家承诺',null=True)
    status = models.IntegerField(verbose_name='审核状态',choices=CAR_CHOISE,default=2)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    isDelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return self.user.username


