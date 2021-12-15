from os import name, stat_result
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from init import db

app = Flask(__name__)
#
'''配置数据库'''
app.config['SECRET_KEY'] = 'hard to guess'#一个字符串，密码。也可以是其他如加密过的

#在此登录的是root用户，要填上密码如123456，MySQL默认端口是3306。并填上创建的数据库名如youcaihua
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/test_1_1'

#设置下方这行code后，在每次请求结束后会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)#实例化数据库对象，它提供访问Flask-SQLAlchemy的所有功能

'''定义模型，建立关系'''
class Product(db.Model):
    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String(64))
    category_value = db.Column(db.Integer)
    price = db.Column(db.Float)
    # number is about to be included
    photo_path = db.Column(db.String(100))
    description = db.Column(db.String(500))
    # add source id
    source_id = db.Column(db.Integer)


    __table_args__ = {
        "mysql_charset" : "utf8"
    }

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(64))
    password = db.Column(db.String(50))
    # add email
    email = db.Column(db.String(100))

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

#
# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User', backref='role', lazy='dynamic')
#
#     def __repr__(self):
#         return '<Role %r>' % self.name
#
#
# class Users(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#
#     def __repr__(self):
#         return '<User %r>' % self.username


#
#
'''进行数据库操作'''
if __name__ == '__main__':
    #删除旧表
    db.drop_all()
    db.create_all()#创建新表

    # user1 = User(id = 1, user_name = 'jessica', password = '123456', email='1@163.com')
    user2 = User(id = 2, user_name = 'scarlyw', password = '123', email='2@gmail.com')
    user3 = User(id=3, user_name='mysterioususer', password = '111', email='Just_a_string')

    # product1 = Product(product_id = 1, product_name='ICS', price = 100.1, description='没人理解计算机系统', category_value=1)
    # product2 = Product(product_id = 2, product_name='操统', price = 50.1, description='操统话剧排练', category_value=1)
    product3 = Product(product_id=3, product_name='软工', price=70.1, description='软件工程教材', category_value=1, source_id = 1)
    product4 = Product(product_id=4, product_name='yxd', price=100000, description='信科大三本科生', category_value=2, source_id = 1)
    product5 = Product(product_id=5, product_name='lyw', price=100010, description='信科大三一只猫', category_value=2, source_id = 2)

    product6 = Product(product_id=6, product_name='淑芬1', price=10.1, description='我就没学会过', category_value=1, source_id=3)
    product7 = Product(product_id=7, product_name='淑芬2', price=13.1, description='我就没学会过+1', category_value=1, source_id=3)
    product8 = Product(product_id=8, product_name='淑芬3', price=12.1, description='我就没学会过+1+1', category_value=1, source_id=3)
    # db.session.add_all([user1, user2, product1, product2])
    # db.session.add_all([product6, product7, product8])
    db.session.add_all([user2, user3, product3, product4, product5, product6, product7, product8])
    # db.session.add_all([user1, product1, product2])

    db.session.commit()

    # user1 = User(id = 1, name='scarlyw', password = '123457')
    # user2 = User(id = 2, name='闫旭东', password = '123')
    # user3 = User(id = 3, name = '畅畅子yyds', password = '666666')
    #
    # product1 = Product(id = 1, name = '数分三', price = 10.111, description = '好书一本哦，大家注意！！！')
    # product2 = Product(id = 2, name = 'test', price = 12334, description = 'test！！！')
    #
    # correlation1 = Correlation(user_id = 1, product_id = 2, state = 0)
    # correlation2 = Correlation(user_id = 2, product_id = 1, state = 4)
    #
    # #在将对象写入数据库之前，先将其添加到会话中，数据库会话db.session和Flask session对象没有关系，数据库会话也称 事物 译作Database Transaction。
    # db.session.add_all([user1, user2, user3, product1, product2, correlation1, correlation2])
    # #提交会话到数据库
    # db.session.commit()
    #
    # #修改roles名
    # user1.name = '刘雨薇yuweil'
    # db.session.add(user1)
    # db.session.commit()
    #
    # #删除数据库会话，从数据库中删除“Moderator”角色
    # #db.session.delete(mod_role)
    # #db.session.commit()#注意：删除 和插入、更新一样，都是在数据库会话提交后执行

    #查询
    print("debug")
    print(User.query.all())