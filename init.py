from flask import Flask
from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy 
from flask import jsonify
from flask import request

db = SQLAlchemy()

# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'hard to guess'#一个字符串，密码。也可以是其他如加密过的

# #在此登录的是root用户，要填上密码如123456，MySQL默认端口是3306。并填上创建的数据库名如youcaihua
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1z2x3c@127.0.0.1:3306/test_0'

# #设置下方这行code后，在每次请求结束后会自动提交数据库中的变动
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db = SQLAlchemy(app)#实例化数据库对象，它提供访问Flask-SQLAlchemy的所有功能
# 这里使用 flask 是因为 flask 轻量,两三行代码就能起一个项目,方便,使用Django在这就显得笨拙
