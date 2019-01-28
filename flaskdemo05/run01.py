from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import or_, func

pymysql.install_as_MySQLdb()
app = Flask(__name__)
#指定数据库的配置
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
#自动提交操作
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
#每次操作打印原始的字符串
# app.config['SQLALCHEMY_ECHO']=True
#创建数据据示例
db = SQLAlchemy(app)

#创建实体类
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120),unique=True)
    isActive = db.Column(db.Boolean,default=True)
    wife = db.relationship('Wife',backref = 'user',uselist=False)

    def __init__(self,username,age,email):
        self.username =username
        self.age = age
        self.email = email

    def __repr__(self):
        return "<User:%r>" % self.username

class Classes(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))

    students = db.relationship('Student',backref='classes',lazy='dynamic')

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return "<Classes:%r>"% self.name

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer)

    class_id = db.Column(db.Integer,db.ForeignKey('class.id'))

    def __init__(self, sname, sage):
        self.sname = sname
        self.sage = sage

    def __repr__(self):
        return '<Student:%r>' % self.sname

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer)
    tbirth = db.Column(db.Date)
    #增加一个列表示引用自course表的主键
    Course_id = db.Column(db.Integer,db.ForeignKey('course.id'))

    def  __init__(self,tname,tage,tbirth):
        self.tname = tname
        self.tage = tage
        self.tbirth = tbirth

    def __repr__(self):
        return "<Teacher:%r>" % self.tname

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)
    #增加关联属性和反向引用关系
    #关联属性:在course中通过哪个属性能够的岛对应的所有的teacher对象
    #反向引用:在teacher对象中通过哪个属性能够得到对应的course
    teachers = db.relationship('Teacher',backref='course',lazy='dynamic')


    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return "<Course:%r>" % self.cname

class Wife(db.Model):
    __tablename__ = 'wife'
    id = db.Column(db.Integer,primary_key=True)
    wname = db.Column(db.String(30))
    #增加对ｕｓｅｒｓ的一对一引用关系
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))

db.create_all()


@app.route('/01-add')
def add_views():
    #创建user对象
    users = Users('王老师',35,'mrwang@163.com')
    db.session.add(users)
    db.session.commit()
    return 'add ok'

@app.route("/register",methods=['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        #接收前端传递过来的数据
        uname = request.form.get('uname')
        uage = request.form.get('uage')
        uemail = request.form.get('uemail')
        #将数据构建实体对象
        user = Users(uname,uage,uemail)
        #将数据保存回数据库
        db.session.add(user)
        db.session.commit()
        return 'Register Success'

@app.route("/03-query")
def query_views():
    #查找列
    # users = db.session.query(Users.username,Users.age)
    # print(users)
    # users = db.session.query(Users).filter(Users.age>30).all()
    # users = db.session.query(Users).filter(Users.id>1,Users.age>30).all()
    # users = db.session.query(Users).filter(Users.email.like('%w%')).all()
    # users = db.session.query(Users).filter(Users.email.like('%w%')).all()
    # users = db.session.query(Users).filte
    # db.session.query(Users).filter(Users.email.like('%w%')).all()r(Users.id.in_([2,4])).all()
    # users = db.session.query(Users).filter(Users.age.between(20,50)).all()
    # for u in users:
    #     print("id：%d,姓名：%s,年龄：%d,邮箱：%s"%(u.id,u.username,u.age,u.email))
    #查询ｉｄ为1的user信息
    # user = db.session.query(Users).filter_by(id=1).first()
    # print(user)
    #查询Ｕｓｅｒ表中的前两条数据
    # users = db.session.query(Users).limit(2).all()
    #获取users表中过滤前三条数据取剩余的两条数据
    # users = db.session.query(Users).limit(2).offset(3).all()
    #排序
    # users = db.session.query(Users).order_by('age desc,id asc').all()
    #按age列进行分组
    # users = db.session.query(Users.age).group_by('age').all()
    # for u in users:
    #     print("id：%d,姓名：%s,年龄：%d,邮箱：%s"%(u.id,u.username,u.age,u.email))
    #聚合函数avg
    # result = db.session.query(func.avg(Users.age).label('avgage')).all()
    #按照年龄分组，球组内年龄的平局值
    # result = db.session.query(func.avg(Users.age)).group_by('age').all()
    # print(result)
    #基于Models的查询
    # users = Users.query.all()
    # users = Users.query.filter(Users.id>1).all()
    users = Users.query.filter_by(id = 3).all()
    for u in users:
         print("id：%d,姓名：%s,年龄：%d,邮箱：%s"%(u.id,u.username,u.age,u.email))

    return '<script>alert("Query OK");</script>'


@app.route('/04-queryall')
def queryall():
    users = Users.query.filter_by(isActive = True).all()
    return render_template('04-queryall.html',users = users)


@app.route('/05-update',methods=['POST','GET'])
def update_views():
    if request.method == 'GET':
        id = request.args.get('id')
        user = Users.query.filter_by(id = id).first()
        return render_template('05-update.html',user=user)
    else:
        id = request.form.get('id')
        user = Users.query.filter_by(id = id).first()
        username = request.form.get('uname')
        uage = request.form.get('uage')
        uemail = request.form.get('uemail')
        user.username = username
        user.age = uage
        user.email = uemail
        db.session.add(user)
        user1 = Users.query.all()
        return redirect('/04-queryall')


@app.route('/07-delete')
def delete1():
    id = request.args.get('id')
    user = Users.query.filter_by(id = id).first()
    #db.session.delete(user)
    #以修改来表示删除，将isactive的值更改为Ｆａｌｓｅ来表示删除
    user.isActive = False
    db.session.add(user)
    return redirect('/04-queryall')


@app.route('/06-update')
def update1():
    user = Users.query.filter_by(id = 3).first()
    user.username = 'brother chao'
    user.age = 99
    db.session.add(user)
    return 'UPDATE OK'

@app.route('/08-insert')
def insert_views():
    c1 = Course('钢管舞')
    c2 = Course('芭蕾舞')
    db.session.add(c1)
    db.session.add(c2)
    return 'Insert OK'

@app.route('/09-register-teacher')
def register_teacher():
    #通过关联属性关联数据
    # tea1 = Teacher('魏老师',40,'1985-10-01')
    # tea1.Course_id = 1
    # db.session.add(tea1)

    #通过反向引用属性关联数据
    tea2 = Teacher('王老师',45,'1975-10-01')
    #查询ｉｄ为1的course的信息
    course = Course.query.filter_by(id=1).first()
    tea2.course = course
    db.session.add(tea2)
    return 'Register Teacher OK'


@app.route('/10-query')
def query10_views():
    #通过过course对象查询所有的对应teachers
    # course = Course.query.filter_by(id = 1).first()
    # #teachers提供了对应的teacher查询
    # teachers = course.teachers.all()
    # print('课程名称：'+course.cname)
    # print('对应的老师们：')
    # for tea in teachers:
    #     print('姓名：%s' %tea.tname)


    tea = Teacher.query.filter_by(id=1).first()
    course = tea.course
    print('教师姓名：%s' % tea.tname)
    print('课程：%s' % course.cname)
    return 'Query OK'




@app.route('/add-class')
def add2_views():
    cl1 = Classes('1806')
    cl2 = Classes('1807')
    cl3 = Classes('1808')
    db.session.add(cl1)
    db.session.add(cl2)
    db.session.add(cl3)
    return 'Add OK'

@app.route('/11-register-stu',methods=['POST','GET'])
def register2():
    if request.method == 'GET':
        list = Classes.query.all()
        return render_template('11-register-stu.html',list = list)
    else:
        #获取前端的数据
        sname = request.form.get('sname')
        sage = request.form.get('sage')
        classes_id = request.form.get('classes')
        #构建student对象
        stu = Student(sname,sage)
        stu.class_id = classes_id
        #将对象保存到数据库
        db.session.add(stu)
        return redirect('/12-students')

@app.route('/12-students')
def students1_views():
    list = Student.query.all()
    return render_template('12-students.html',list=list)

@app.route('/13-wife')
def wife_users():
    #通过wife找users
    # wife = Wife.query.filter_by(id=1).first()
    # user = wife.user
    # print('Wife:%s' % wife.wname)
    # print('User:%s' % user.username)
    #通过users找wife
    user = Users.query.filter_by(id=2).first()
    wife = user.wife
    print('Wife:%s' % wife.wname)
    print('User:%s' % user.username)
    return 'Ｑuery ok'
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')