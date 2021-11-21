from os import name, stat_result
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
from init import db

# app = Flask(__name__)

# '''配置数据库'''
# app.config['SECRET_KEY'] = 'hard to guess'#一个字符串，密码。也可以是其他如加密过的

# #在此登录的是root用户，要填上密码如123456，MySQL默认端口是3306。并填上创建的数据库名如youcaihua
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1z2x3c@127.0.0.1:3306/test_0'

# #设置下方这行code后，在每次请求结束后会自动提交数据库中的变动
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# db = SQLAlchemy(app)#实例化数据库对象，它提供访问Flask-SQLAlchemy的所有功能

'''定义模型，建立关系'''
class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    category = db.Column(db.Integer)
    price = db.Column(db.Float)
    photo = db.Column(db.String(100))
    description = db.Column(db.String(500))

    __table_args__ = {
        "mysql_charset" : "utf8"
    }

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(50))

    __table_args__ = {
        "mysql_charset" : "utf8"
    }

class Correlation(db.Model):
    __tablename__ = 'correlation'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    state = db.Column(db.Integer)

class History(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    user_perspective = db.Column(db.Integer)
    day = db.Column(db.Date)
    time = db.Column(db.Time)

class Category_info(db.Model):
    __tablename__ = 'category_info'

    id = db.Column(db.Integer, primary_key = True)
    category_n = db.Column(db.String(60))
    __table_args__ = {
        "mysql_charset" : "utf8"
    }

'''
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username
'''



# '''进行数据库操作'''
# if __name__ == '__main__':
#     #删除旧表
#     db.drop_all()
#     db.create_all()#创建新表

#     user1 = User(id = 1, name='scarlyw', password = '123457')
#     user2 = User(id = 2, name='闫旭东', password = '123')
#     user3 = User(id = 3, name = '畅畅子yyds', password = '666666')

#     product1 = Product(id = 1, name = '数分三', price = 10.111, description = '好书一本哦，大家注意！！！')
#     product2 = Product(id = 2, name = 'test', price = 12334, description = 'test！！！')

#     correlation1 = Correlation(user_id = 1, product_id = 2, state = 0)
#     correlation2 = Correlation(user_id = 2, product_id = 1, state = 4)

#     #在将对象写入数据库之前，先将其添加到会话中，数据库会话db.session和Flask session对象没有关系，数据库会话也称 事物 译作Database Transaction。
#     db.session.add_all([user1, user2, user3, product1, product2, correlation1, correlation2])
#     #提交会话到数据库
#     db.session.commit()

#     #修改roles名
#     user1.name = '刘雨薇yuweil'
#     db.session.add(user1)
#     db.session.commit()

#     #删除数据库会话，从数据库中删除“Moderator”角色
#     #db.session.delete(mod_role)
#     #db.session.commit()#注意：删除 和插入、更新一样，都是在数据库会话提交后执行

#     #查询
#     print("debug")
#     print(User.query.all())