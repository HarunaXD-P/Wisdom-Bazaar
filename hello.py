from flask import Flask
from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy 
from flask import jsonify
from flask import request
import json
from init import db
from database import User, Product

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess'#一个字符串，密码。也可以是其他如加密过的

#在此登录的是root用户，要填上密码如123456，MySQL默认端口是3306。并填上创建的数据库名如youcaihua
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1z2x3c@127.0.0.1:3306/test_0'

#设置下方这行code后，在每次请求结束后会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

# db = SQLAlchemy(app)#实例化数据库对象，它提供访问Flask-SQLAlchemy的所有功能
# # 这里使用 flask 是因为 flask 轻量,两三行代码就能起一个项目,方便,使用Django在这就显得笨拙

# @app.route('/')
# def index():
#     print('前端请求来了')
#     # res = make_response('畅畅子yyds!')
#     # 在 header 中加入 ACRS = 所有 (跨域资源共享)
#     res.headers["Access-Control-Allow-Origin"] = '*'
        
#     return res

def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
 

# @app.route('/' , methods=['GET', 'POST'])
@app.route('/',  methods=['GET', 'POST', 'OPTIONS'])
def index():
    a = request.get_data()
    print("!Q!!!!!!!!!!!!!POST")
    dict1 = to_dict(Product.query.first())
    print(dict1)
    # dict1 = json.lods(a)
    # resp = ""
    # for key, value in dict1.items():
    #     resp = resp + key + value
    res = make_response(json.dumps(dict1))
    print(json.dumps(dict1) + "!Q!!!!!!!!!!!!!POST")
    res.headers["Access-Control-Allow-Origin"] = '*'
    return res


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'  

if __name__ == '__main__':
    app.run()