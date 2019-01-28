from flask import Flask, make_response, request, render_template, session

app = Flask(__name__)
app.config['SECRET_KEY']='AIXIESHAXIESHA'

@app.route('/01-setCookie')
def setCookie():
    resp=make_response('保存cookie成功')
    #保存uname进cookie,值为wangwc
    resp.set_cookie('uname','wangwc',3600)
    return resp

@app.route('/02-getCookie')
def getCookie():
    print(request.cookies)
    uname = request.cookies.get('uname')
    return 'uname的值为:%s'%uname

@app.route('/03-login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
        if 'uname' in request.cookies:
            uname = request.cookies.get('uname')
            return '欢迎:%s'% uname
        else:
            return render_template('03-login.html')
    else:
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        if uname == 'admin' and upwd == 'admin':
            resp = make_response('欢迎：'+uname)
            if 'remember' in request.form:
                resp.set_cookie('uname',uname,60*60*24*365)
            return resp
        else:
            return '登录失败'
    
@app.route('/04-setSession')
def setSession():
    session['uname'] = 'tarena'
    return '保存session成功'


@app.route('/05-getSession')
def getsession():
    if 'uname' in session:
        uname = session['uname']
        return 'uname:%s'%uname
    else:
        return '没有相关数据'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')