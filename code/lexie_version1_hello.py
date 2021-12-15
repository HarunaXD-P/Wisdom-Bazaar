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
#记得改密码
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/test_0'

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
    info = json.loads(request.get_data())
    ans = Product.query.filter(or_(Product.name == info["name"], Product.description == info["description"])).first()
    res = make_response(json.dumps({}))
    return 



@app.route('/check_user',  methods=['GET', 'POST', 'OPTIONS'])
def check_user():
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

# product_management
# dealing with queries associated with products
# get:
# post: post a product
# options: undefined scenario
@app.route('/product_management',  methods=['GET', 'POST', 'OPTIONS'])
def index():
    info = json.loads(request.get_data())
    # print(info)

    # return the product that this person has posted
    if request.method == 'GET':
        return

    # post a new product
    elif request.method == 'POST':
        product = Product(name=info["Title"], price=info["price"], description=info["description"])
        db.session.add(product)
        db.session.commit()
        dict1 = to_dict(Product.query.first())
        print(dict1)
        # dict1 = json.loads(a)
        # resp = ""
        # for key, value in dict1.items():
        #     resp = resp + key + value
        res = make_response(json.dumps(dict1))
        print(json.dumps(dict1) + "!Q!!!!!!!!!!!!!POST")
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("product options error!")
        return


@app.route('/')
def hello_world():
    return 'Hello, World!'


# the initialization of new tables
# not used in actual running process
if __name__ == '__main__':
    # db.create_all()  # 创建新表
    # db.drop_all()

    #
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
    #     #在将对象写入数据库之前，先将其添加到会话中，数据库会话db.session和Flask session对象没有关系，数据库会话也称 事物 译作Database Transaction。
    # db.session.add_all([user1, user2, user3, product1, product2, correlation1, correlation2])
    #     #提交会话到数据库
    # db.session.commit()
    #
    #     #修改roles名
    # user1.name = '刘雨薇yuweil'
    # db.session.add(user1)
    # db.session.commit()

        #删除数据库会话，从数据库中删除“Moderator”角色
        #db.session.delete(mod_role)
        #db.session.commit()#注意：删除 和插入、更新一样，都是在数据库会话提交后执行
    app.run()
