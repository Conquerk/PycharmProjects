import json

from flask import Flask, request

app = Flask(__name__)

@app.route("/01-server")
def server01():
    #接收前端传递过来的参数
    cd = request.args.get('callback')

    return cd+"('这是服务器端响应的内容')"

@app.route("/02-server")
def server02():
    cd = request.args.get('callback')
    dic = {
        "flightNO":"CA444",
        "from":"北京",
        "to":"LA",
        "time":"00:00"
    }
    jsonstr = json.dumps(dic)
    return cd+"("+jsonstr+");"


@app.route("/03-jq-cross")
def jq_cross():
    cd = request.args.get("callback")
    return cd + "('服务端响应回去的数据')"


@app.route("/03-server")
def server03():
    cd = request.args.get("huidiao")
    return cd + "('这是使用方案２响应的数据');"


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
