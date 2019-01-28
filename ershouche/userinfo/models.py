from django.db import models
from django.contrib.auth.models import AbstractUser

SEX_CHOICES = (
    (0,'男'),
    (1,'女'),
)
ROLE_CHOICES = (
    (0,'buy'),
    (1,'sale'),
    (2,'back')
)
BANK_CHOICES = (
    (0,'中国工商银行'),
    (1,'中国建设银行'),
    (2,'中国农业银行'),
    (3,'招商银行'),
    (4,'北京银行'),
    (5,'左俞银行'),

)
# Create your models here.
# 用户表Userinfo
# 用户名username(C)
# 密码password(C)
# 真实姓名realname(C)
# 身份证号iden(C)
# 住址ads(c)
# 手机号uphone(C)
# 性别sex(Ic)
# 角色role(Ic)
# 激活状态isActive(B)
# 是否禁用isBan(B)
class UserInfo(AbstractUser):
    # username = models.CharField('用户名',max_length=30,null=False)
    # password = models.CharField('密码',max_length=50,null=False)
    realname = models.CharField('真实姓名',max_length=30,null=False)
    iden = models.CharField('身份证号',max_length=18,null=False)
    abs = models.CharField('住址',max_length=200,null=False)
    uphone = models.CharField('手机号',max_length=20,null=False)
    sex = models.IntegerField(verbose_name='性别',choices=SEX_CHOICES,default=0)
    role = models.IntegerField(verbose_name='角色',choices=ROLE_CHOICES,default=0)
    isActive = models.BooleanField(verbose_name='是否激活',default=False)
    isBan = models.BooleanField(verbose_name='是否禁用',default=False)

    def __str__(self):
        return self.username



class Bank(models.Model):
    # 银行卡表Bank
    # 卡号cardNo(C)
    # 用户user(F)
    # 交易密码cpwd(C)
    # 开户银行bank(Ic)
    # 是否删除

    cardNo = models.CharField('银行卡号',max_length=50,null=False)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    cpwd = models.CharField('交易密码',max_length=200,null=False)
    bank = models.IntegerField(verbose_name='开户银行',choices=BANK_CHOICES)
    isDelete = models.BooleanField(verbose_name='是否删除',default=False)

    def __str__(self):
        return self.user.username




