#声明所有的实体类


from . import db

class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer,primary_key=True)
    cate_name = db.Column(db.String(50),nullable=False)

    #关联关系和反向引用 - topic
    topics = db.relationship("Topic",backref = "category",lazy="dynamic")


class BlogType(db.Model):
    __tablename__ = "blogtype"
    id = db.Column(db.Integer,primary_key=True)
    type_name = db.Column(db.String(20),nullable=False)

    #topic关联属性和反向引用
    topics = db.relationship("Topic",backref="blogtype",lazy="dynamic")

class User(db.Model):
    __tablename__ = "user"
    ID = db.Column(db.Integer,primary_key=True)
    loginname = db.Column(db.String(50),nullable=False)
    uname = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    url = db.Column(db.String(200))
    upwd = db.Column(db.String(30),nullable=False)
    is_author = db.Column(db.SmallInteger,default=0)

    #与ｔｏｐｉｃ之间的关联属性和反向引用
    topics = db.relationship("Topic",backref="user",lazy="dynamic")

    #repil关联属性
    replies = db.relationship("Reply",backref="user",lazy="dynamic")

    #在ｕｓｅｒ中添加多对的关联属性和反向引用关系
    work_topics = db.relationship("Topic",secondary="work",lazy="dynamic",backref=db.backref("work_users",lazy="dynamic"))


class Topic(db.Model):
    __tablename__ = "topic"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    pub_date = db.Column(db.DateTime,nullable=False)
    read_num = db.Column(db.Integer,default=0)
    content = db.Column(db.Text,nullable=False)
    images = db.Column(db.Text)

    #一(Category)对多(topic)关系
    category_id = db.Column(db.Integer,db.ForeignKey("category.id"))

    #一(blogtype)对多
    blogtype_id =db.Column(db.Integer,db.ForeignKey("blogtype.id"))

    #一(user)对多
    user_id = db.Column(db.Integer,db.ForeignKey("user.ID"))

    #关联属性和引用关系
    replies = db.relationship("Reply",backref="topic",lazy="dynamic")



class Reply(db.Model):
    __tablename__ = "reply"
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text,nullable=False)
    reply_time = db.Column(db.DateTime)
    #一(topic)对多(reply)的关联关系
    topic_id = db.Column(db.Integer,db.ForeignKey("topic.id"))
    #一(user)对多
    user_id = db.Column(db.Integer,db.ForeignKey("user.ID"))

class Woke(db.Model):
    __tablename__  = "work"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("user.ID"))
    topic_id = db.Column(db.Integer,db.ForeignKey("topic.id"))

