from flask import Flask

#当前运行的主程序构建成Ｆｌａｓｋ应用# 接收用户的请求（request）和响应(response)
app = Flask(__name__)

#主要是用于定义Flsak中的路由,主要是定义用户的访问路径,"/"表示整个网站的根路径
@app.route("/")
#表示的是匹配@app.route()的路径后的处理程序,视图处理函数views所有的视图处理函数必须要有一个return,必须要return一个字符串
def index():
    return "My First Flask Demo"


@app.route("/login")
def login():
    return "欢迎访问登录页面"


@app.route("/register")
def register():
    return "欢迎访问注册页面"


#定义带参数的路由以及视图处理函数

@app.route("/show/<name>")
def show(name):
    return "<h1>传递进来的参数为{}</h1>".format(name)


@app.route("/show/<name>/<age>")
def show2(name,age):
    return "姓名:{},年龄:{}".format(name,age)


if __name__ == "__main__":
    #运行Flask应用(启动Flask服务),默认在本机开启5000端口,允许使用　http://localhost:5000/访问Flask的web应用
    #将运行模式更改为调试模式(开发环境中推荐使用True，生产环境中必须改为False)
    app.run(debug=True)