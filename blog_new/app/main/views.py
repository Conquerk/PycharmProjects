#只处理与mian业务相关的路由和视图
import datetime
import os

from flask import render_template, request, make_response, session, redirect

from . import main
from .. import db
from ..models import *


@main.route('/')
def main1():
    #读取所有分类
    categorys = Category.query.all()
    #读取表中前五条数据
    topics = Topic.query.all()
    if "uid" in session and "loginname" in session:
        user = User.query.filter_by(ID = session.get("uid")).first()

    return render_template('index.html',proams=locals())

@main.route("/login",methods=['GET',"POST"])
def login1():
    if request.method == "GET":
        resp = make_response(render_template("login.html"))
        url = request.headers.get("Referer","/")
        resp.set_cookie("url",url)
        return resp
    else:
        loginname = request.form.get('username')
        upwd = request.form.get("password")
        url = request.cookies['url']
        user = User.query.filter_by(loginname=loginname,upwd=upwd).first()
        if user:
            session['uid'] = user.ID
            session["loginname"] = loginname
            resp = redirect(url)
            resp.delete_cookie("url")
            return resp
        else:
            return render_template('login.html',errmsg="用户名或者密码错误")

@main.route('/logout')
def logout():
    if 'uid' in session and 'loginname' in session:
        del session['uid']
        del session['loginname']
        url = request.headers.get('Referer','/')
    return  redirect(url)


@main.route('/release',methods=['GET','POST'])
def release():
    if request.method == "GET":
        #登录的身份验证
        if "uid" in session and 'loginname' in session:
            #有登录用户
            user = User.query.filter_by(ID=session.get('uid')).first()
            if user.is_author == 1:
                #查询所有的ｂｌｏｇｔｙｐｅ
                blogtypes = BlogType.query.all()
                #查询所有的ｃａｔｅｇｏｒｙ
                categroies = Category.query.all()
                return render_template("release.html",params = locals())
            else:
                msg = "<script>alert('您没权限发表博客');location.href='/';</script>";
                return msg
        else:
            return redirect("/login")
    else:
        #ｐｏｓｔ请求，增加博客到数据库中
        topic = Topic()
        topic.title = request.form.get('author')
        topic.blogtype_id = request.form.get('list')
        topic.category_id = request.form.get("category")
        topic.content = request.form.get("content")
        topic.pub_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        topic.user_id = session.get('uid')
        if request.files:
            #有图片上传,将图片上传并将图片名称赋值给topic.images
            file =request.files['pic']
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            ext = file.filename.split('.')[1]
            filename = ftime+"."+ext
            topic.images = 'images/'+filename
            basedir = os.path.dirname(os.path.dirname(__file__))
            upload_path = os.path.join(basedir,'static/images',filename)
            file.save(upload_path)
        db.session.add(topic)
        return redirect('/')







