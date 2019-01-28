from django.contrib import admin
from .models import *
#声明Author的高级管理类
class AuthorAdmin(admin.ModelAdmin):
    #1.定义在列表页上显示的属性们
    list_display = ['name','age','email']
    #2.定义允许被点击的字段们
    list_display_links = ['name','email']
    #3.定义在列表也上允许被编辑的字段
    list_editable = ['age']
    #4.添加允许被搜索的字段们
    search_fields = ['name','email']
    #5.增加过滤器
    list_filter = ['name','email']

    #6.指定在详情页中指定显示哪些字段以及他们的顺序
    # fields = ['name','email','age']

    #指定在详情页中的字段分组们
    fieldsets = (
        #分组１：name,age
        ('基本选项',{
            'fields':('name','age')
        }),
        #分组２：email,isActive
        ('高级选项',{
            'fields':('email','isActive'),
            'classes':('collapse',)
        }),
    )

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','publicate_date']
    #顶部增加时间选择器
    date_hierarchy = 'publicate_date'

# class PublisherAdmin(admin.ModelAdmin):
#     list_display = ['name','address','city']
#     list_editable = ['address','city']
#     search_fields = ['city','address','name','website']
#     fieldsets = (
#         ('基本选项',{
#             'fields':('name','adress','city'),
#         }),
#         (
#             '高级选型',{
#                 'fields':('country','website'),
#                 'classes':('collapse',)
#             }),
#     )


# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher)
admin.site.register(Wife)

