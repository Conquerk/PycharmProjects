from django import forms

#为topic做初始化数据
from index.models import User

TOPIC_CHOICE = (
    ('1','好评'),
    ('2','中评'),
    ('3','差评'),
)

#创建一个表示评论内容的表单控件们
#控件１ 评论标题　文本
#控件２  email   email
#控件３  评论内容  textarea
#控件４  评论级别　　　select
#控件５　　是否保存   checkbox

class RemarkForm(forms.Form):
    #评论标题
    #label表示控件前的文本
    subject = forms.CharField(max_length=30,label='标题')
    #email
    email = forms.EmailField(label='邮箱')
    #评论内容
    #widget=forms.Textarea将当前的文本框变成文本域
    message = forms.CharField(label='内容',widget=forms.Textarea)
    #评论级别
    topic = forms.ChoiceField(label='级别',choices=TOPIC_CHOICE)
    #isSaved - checkbox
    isSaved = forms.BooleanField(label='是否保存')


class RegisterForm(forms.ModelForm):
    class Meta:
        #1.指定关联的ｍｏｄｅｌ
        model = User
        #指定生成控件的属性
        fields = '__all__'
        #每个属性关联的ｌａｂｅｌ
        labels = {
            'uname':'用户名称',
            "upwd":'用户密码',
            'uemail':'电子邮箱'
        }