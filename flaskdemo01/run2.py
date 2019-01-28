from flask import Flask, url_for

app=Flask(__name__)

#多url的路由匹配
@app.route("/")
@app.route("/index")
@app.route("/<int:num>")
@app.route("/index/<int:num>")
def index(num=None):
    if num is None:
        num = 1
    return "您访问的页数为{}".format(num)


@app.route('/method',methods=['POST','GET'])
def method():
    return "这是使用POST/GET请求提交过来的"


@app.route("/admin/login/form/show/<name>/<age>")
def show1(name,age):
    return "参数name的值为：%s,参数age的值为：%s"%(name,age)


@app.route("/url")
def url():
    # url = url_for('show')
    # print("反向生成的url为"+ url)
    # # return "<a href='/admin/login/form/show'>去往show</a>"
    # return "<a href='%s'>去往show</a>"%url
    url = url_for('show1',name="wangwc",age=35)
    print("反向生成的地址为:"+url)
    return "<a href='%s'>去往show</a>"%url


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')