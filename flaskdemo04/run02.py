from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
#创建数据库应用示例
db = SQLAlchemy(app)

#创建模型类　ｕｓｅｒｓ映射岛数据库叫users表
#创建字段　ｉｄ，主键,自增
#创建字段ｕｓｅｒｎａｍｅ长度为80，不允许为空值唯一
#创建字段age整数
#创建字段　email 长度为120的字符　唯一

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable=False,unique=True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120),unique=True)

#将创建好的实体类映射回数据库
db.create_all()

@app.route('/')
def index():
    print(db)
    return '创建ｄｂ成功'



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
