from flask import Flask, render_template
from flask import request
app = Flask(__name__)


@app.route("/01-parent")
def parent():
    return render_template("01-parent.html")


@app.route("/02-child")
def child():
    return render_template("02-child.html")


@app.route("/03-request")
def request_views():
    #print(dir(request))
    #获取请求方案
    scheme = request.scheme
    #获取请求方式
    method = request.method
    #获取ｇｉｔ请求的数据
    args = request.args
    #获取ｐｏｓｔ请求的数据
    form = request.form
    #获取cookies中的数据
    cookies = request.cookies
    #获取请求头的相关信息
    headers = request.headers
    #获取请求资源的路径
    path = request.path
    #获取请求资源的路径（参数）
    full_path = request.full_path
    #获取完整的请求地址
    url = request.url
    #具体的请求消息头
    Referer = request.headers.get('Referer','/')
    us = request.headers['User-Agent']
    return render_template('03-request.html',params=locals())


@app.route("/04-form")
def form_views():
    return render_template("04-form.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route("/05-get",methods=['POST','GET'])
def get_views():
    #接收04-ｆｏｒｍ传递过来的数据
    if request.method == 'GET':
        uname = request.args.get('uname','')
        upwd = request.args.get('upwd','')
    if request.method == "POST":
        uname = request.form.get('uname', '')
        upwd = request.form.get('upwd', '')
    return '<h2>用户名:%s,密码:%s</h2>'%(uname,upwd)


@app.route("/06-form",methods=['POST','GET'])
def form6():
    if request.method == 'GET':
        return render_template('06-form.html')
    else:
        uname = request.form['uname']
        upwd = request.form['upwd']
        dz = request.form['dz']
        xname = request.form['xname']

        print(uname,upwd,dz,xname)
        return 'OK'

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")