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

app.config['SECRET_KEY'] = 'hard to guess'  # 一个字符串，密码。也可以是其他如加密过的

# connect with the mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:a7459529@127.0.0.1:3306/test_0'

# automatically update the database
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

# to_dict
# transform info into python dict
# forbidden to take null inputs
def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

# user_all_products
# post: show all products that have been posted by one specific user
# implemented by lexie, 2021.11.24
@app.route('/userallproducts', methods=['GET', 'POST', 'OPTIONS'])
def user_all_products():
    info = json.loads(request.get_data())
    dict1 = to_dict(Product.query.first())
    print(dict1)
    # search products based on the posted id
    # the result is a list
    dict_result = to_dict(Product.query.filter(Product.source_id == info["source_id"]).all())
    print("search result")
    print(dict_result)
    res = make_response(json.dumps(dict_result))
    print("make result")
    print(res)
    print(json.dumps(dict_result) + " user_all_products")
    res.headers["Access-Control-Allow-Origin"] = '*'
    print("after adding header")
    print(res)
    return res

# initial function implemented for checking
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

    # 删除数据库会话，从数据库中删除“Moderator”角色
    # db.session.delete(mod_role)
    # db.session.commit()#注意：删除 和插入、更新一样，都是在数据库会话提交后执行
    app.run()