from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def addBook_views(request):
    # book = Book.objects.create(title = 'python基础',publicate_date='2015-10-12')
    # print('新增加的书籍的id为：%d'%book.id)

    #方式２
    # book = Book(title='数据库基础')
    # book.publicate_date = '2018-06-12'
    # book.save()
    # print('新增加的书籍的id为：%d' % book.id)
    Book.objects.create(title ='WEB开发基础',publicate_date='2018-01-15')
    Book.objects.create(title ='人工智能的发展',publicate_date='2018-06-12')
    Book.objects.create(title ='数据库的高级进阶',publicate_date='2015-11-07')
    Book.objects.create(title ='Python网络编程',publicate_date='2014-06-03')

    return HttpResponse('add Book Success')

def addAuthor_views(request):
    Author.objects.create(name='王wc',age=38,email='wangwc@163.com')
    Author.objects.create(name='李师师',age=24,email='Li@163.com')
    Author.objects.create(name='艾斯德斯',age=16,email='xxx@163.com')
    Author.objects.create(name='SongDF',age=31,email='Song@163.com')
    return HttpResponse('add Author Success')

def query_views(request):
    #1.基本的查询操作all()
    books = Book.objects.all()
    # print(type(books))
    # print(books)
    # for book in books:
    #     print('ID：%d,书名：%s,出版日期：%s'%(book.id,book.title,book.publicate_date))
    # print(books.query)#打印输出ｓｑｌ语句

    #查询返回部分列
    # books = Book.objects.values('title','publicate_date')
    # # print(books)
    # for book in books:
    #     print('书名：%s,出版日期:%s'%(book['title'],book['publicate_date']))

    #查询返回指定列的另一种方法
    # books = Book.objects.values_list('title','id')
    # print(books)

    #查询只返回一条数据
    # book = Book.objects.get(id=1)
    # print(book.title)

    #根据条件查询部分行的信息
    #id = 1的信息
    # list = Book.objects.filter(id=1)
    # print(list)
    # #publicat_date  = 2018-06-12 的信息
    # list2 = Book.objects.filter(publicate_date='2018-06-12')
    # print(list2)
    #查询 id为2并且publicate_date 为2018-06-12的book
    # list = Book.objects.filter(id=2,publicate_date='2018-06-12')
    # for book in list:
    #     print('ID:%d,书名：%s,出版日期:%s'%(book.id,book.title,book.publicate_date))
    #查询２０１８年的所有数据
    # list = Book.objects.filter(publicate_date__year__gt = 2015)
    # for book in list:
    #     print('ID:%d,书名：%s,出版日期:%s' % (book.id, book.title, book.publicate_date))

    # list = Author.objects.filter(age__gt=30)
    # list = Author.objects.filter(name__startswith='王')
    # list = Author.objects.filter(age__gt=(Author.objects.get(name='Rapwang').age))
    # for au in list:
    #     print('ID:%d,姓名：%s,年龄：%s,邮箱：%s'%(au.id,au.name,au.age,au.email))
        # 8.查询Author表中age大于等于30的Author的信息
        # list = Author.objects.filter(age__gt=30)
        # 9.查询Author表中所有姓“Wang”的Author的信息
        # list = Author.objects.filter(name__startswith='Wang')
        # 10.查询Author表中Email中包含"wang"的Author的信息
        # list = Author.objects.filter(email__contains='wang')
        # 11.查询Author表中age大于"RapWang"的age的所有的信息
        # list = Author.objects.filter(age__gt=(Author.objects.get(name='Rapwang').age))

        # 12.查询Author中年龄不大于35的人的信息
        # list = Author.objects.exclude(age__gt=35)
        # for au in list:
        #     print('ID:%d,姓名:%s,年龄:%d,邮箱:%s' % (au.id,au.name,au.age,au.email))
        # 13.查询Author表中所有人的平均年龄 - 聚合函数 aggregate()
        # result = Author.objects.aggregate(avg=Sum('age'))
        # print("总年龄为:%d" % result['avg'])
        # 14.查询Book表中每个publicate_date所发行的书籍的数量
        #list = Book.objects.values('publicate_date').annotate(count=Count('title')).values('publicate_date','count').all()

        #list = Book.objects.filter(id__gt=1).values('publicate_date').annotate(count=Count'title')).filter(count__gt=3).values('publicate_date', 'count').all()
        #print(list)
        # for book in list:
        #     print(book['publicate_date'])
    return HttpResponse("<script>alert('查询成功')</script>")

def show_views(request):
    authors = Author.objects.filter(isActive='True')
    return render(request,'show_authors.html',locals())


def update_views(request):
    # author = Author.objects.get(id=1)
    # author.age = 40
    # author.save()
    authors = Author.objects.exclude(id = 1)
    authors.update(age = 45)


    return HttpResponse('Update Success')
def delete_views(request,id2):
    id1 = id2
    author = Author.objects.get(id=id1)
    author.isActive = False
    author.save()
    return redirect('/03-show-Author')

def doQ_views(request):
    #1.查询 id = 1 或者 isActive = True 的author们的信息
    authors = Author.objects.filter(Q(id=1)|Q(isActive=True))
    for au in authors:
        print('id:%d,name:%s'%(au.id,au.name))
    return HttpResponse('查询成功')

def oto_views(request):
    #声明wife对象并指定autohr信息
    # wife = Wife()
    # wife.name = '小樱'
    # wife.age = 20
    # wife.author_id = 1
    # wife.save()

    #查询正向查询通过wife查找author
    wife = Wife.objects.get(id = 1)
    author = wife.author
    print(('wife:%s,Author:%s'%(wife,author)))

    return HttpResponse('oto ok')

def otm_views(request):
    #1.正向查询  通过ｂｏｏｋ查询ｐｕｂｌｉｓｈｅｒ
    book = Book.objects.get(id=1)
    publisher = book.publisher
    print('书籍名称：'+book.title)
    print('所在出版社:'+publisher.name)
    #2.反向查询  通过publisher查询book
    pub = Publisher.objects.get(id=1)
    books = pub.book_set.all()
    print('出版社名称:'+pub.name)
    print('出版的图书为:')
    for book in books:
        print('书籍名字：'+book.title)

    return HttpResponse('OK')

def mtm_views(request):
    #id为１的书的作者
    book = Book.objects.get(id=8)
    authors = book.author_set.all()
    print('书名：'+book.title)
    for au in authors:
        print('作者：'+au.name)
    #李小姐的书
    au = Author.objects.get(name='李小姐')
    books = au.book_set.all()
    print(au.name+'出版的书籍为:')
    for book in books:
        print('书名为：'+book.title)

    return HttpResponse('ok')