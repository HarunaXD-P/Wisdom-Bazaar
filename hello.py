from flask import Flask
from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy 
from flask import jsonify
from flask import request
import json
from init import db
from database import User, Product
from sqlalchemy import and_, or_


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

# 将query出来的对象变成dict，但是不能传入空对象
def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
 
@app.route('/show_product',  methods=['GET', 'POST', 'OPTIONS'])
def show_product() :
    return 

@app.route('/check_user',  methods=['GET', 'POST', 'OPTIONS'])
def check_user():
    #
    #
    #
    info = json.loads(request.get_data())
    # info 为一个dict
    print(info["name"])
    print("check_user_POST")
    # 我不确定这么写对不对，大概就是找出来之后发回去是否正确（
    ans = User.query.filter(and_(User.name == info["name"], User.password == info["password"])).first()
    flag = True
    if not ans:
        flag = False    
    # make_response只能是字符串所以这么搞比较方便
    # make_response 只能是 json.dumps(dict)
    res = make_response(json.dumps({'status' : flag}))
    res.headers["Access-Control-Allow-Origin"] = '*'
    return res

# 目前不能用的框架
# @app.route('/add_user',  methods=['GET', 'POST', 'OPTIONS'])
# def add_user():
#     info = json.loads(request.get_data())
#     print("add_user_POST")
#     # dict1 = to_dict(User.query.filter(and_(User.name == info.name, User.password == info.password)).first())
#     user = User(name = info.name, password = info.password)
#     db.session.add(user)
#     db.session.commit()
#     res = True
#     # if not dict1:
#         # res = False
#     res.headers["Access-Control-Allow-Origin"] = '*'
#     return res

# 加入一个新的物品
# @app.route('/' , methods=['GET', 'POST'])
@app.route('/product',  methods=['GET', 'POST', 'OPTIONS'])
def index():
    info = json.loads(request.get_data())
    print("!product_POST")
    print(info)
    product = Product(name = info["Title"], price = info["price"], description = info["description"])
    db.session.add(product)
    db.session.commit()
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


@app.route('/')
def hello_world():
    return 'Hello, World!'  

if __name__ == '__main__':
    app.run()