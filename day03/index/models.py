from django.db import models

# Create your models here.

#创建一个实体类 - publisher  表示‘出版社’
# #1.name：出版社名称 - varchar
#2.address：出版社地址-varchar
#3.city：出版社所在城市- varchar
#4.country：出版社所在城市-varchar
#5.website：出版社网址 - varchar
class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='出版社')
    address = models.CharField(max_length=200,verbose_name='地址')
    city = models.CharField(max_length=30,verbose_name='城市')
    country = models.CharField(max_length=30,verbose_name='国家')
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(max_length=30,null=True,verbose_name='电子邮箱')
    isActive = models.CharField(max_length=10,default=True,verbose_name='激活')

    #重写str函数以便在后台的表示方式
    def __str__(self):
        return self.name

    class Meta:
        #1.指定表名
        db_table = 'author'
        #指定显示的名称verbose_name
        verbose_name = '作者'
        #3.指定显示的名称
        verbose_name_plural = verbose_name
        #4.指定在ａｄｍｉｎ中按照年龄降序排序
        ordering = ['-age']




class Book(models.Model):
    title = models.CharField(max_length=30)
    publicate_date = models.DateField()

    #增加对publisher的一对多的引用关系
    publisher = models.ForeignKey(Publisher,null=True)
    #增加多对多引用
    author_set = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
        ordering = ['-publicate_date']


class Wife(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    #增加对Author的一对一关联
    author = models.OneToOneField(Author)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'