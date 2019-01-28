from flask import Flask, render_template

app = Flask(__name__)

@app.route("/01-var")
def var_views():
    name = "隔壁老王"
    age = 32
    salsry = 125.55
    tup=('老魏','老王','老吕','蒙蒙')
    list=['漩涡名人','苍井空']
    dic={
        'c':'china',
        'a':'america'
    }
    dog = Dog()

    return render_template('01-var.html',params=locals())

@app.route("/02-filter")
def filter():
    title = "This is my FIRST filter page"
    return render_template('02.filter.html',title=title)


@app.route("/03-if")
def if_views():
    return render_template("03-if.html",age=45,uname="wangwc")


@app.route("/04-for")
def for_views():
    list = ['武大郎','潘金莲','王宝强','王伟超']
    dic = {
        'SWK':'孙悟空',
        'ZWN':'猪无能',
        'SWJ':'杀吴境',
        'BLM':'白龙马',
        'TSZ':'搪三藏',
    }
    return render_template("04-for.html",params=locals())

@app.route('/05-macro')
def macro_views():
    list = ['苍山有井名为空','嵩山有岛一叶枫']
    return render_template("05-macro.html",params=locals())


@app.route('/06-static')
def static_views():
    return render_template('06-static.html')






class Dog(object):
    name = "旺财"
    def eat(self):
        return  self.name+ "吃狗粮"

if __name__ == "__main__":
    app.run(debug=True)