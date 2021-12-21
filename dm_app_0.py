import os.path
from flask import Flask
from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask import request
import json
from init import db
from dm_database import User, Product, History, Wanted
from sqlalchemy import and_, or_
import base64
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'  # 一个字符串，密码。也可以是其他如加密过的

# connect with the mysql database
# The default database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/test_0'

# automatically update the database
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

# to_dict
# transform info into python dict
# forbidden to take null inputs
def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

# take_price
# get the desired value
def take_price(x):
    return x.price

# take_category
# get the category number
def take_category(x):
    return x.category_value

# user_post_product
# post: post a product
# implemented by lexie, 2021.11.23
@app.route('/userpostproduct', methods=['GET', 'POST', 'OPTIONS'])
def user_post_product():
    print("enter_user_post_product")
    info = json.loads(request.get_data())
    print(info)
    # directly return
    if request.method == 'GET':
        return
    # post a new product
    elif request.method == 'POST':
        photo_picture_string = info["photo"]
        basedir = os.path.abspath(os.path.dirname(__file__))
        print(basedir)
        path_photo_picture_folder = basedir + "/static/img/"
        photo_picture_name = "lexie_crazy_picture.png"
        path_photo_picture_save = path_photo_picture_folder + photo_picture_name
        print(path_photo_picture_save)

        with open(path_photo_picture_save, 'wb') as f:
            f.write(base64.b64decode(photo_picture_string))

        url = '/static/img/' + photo_picture_name
        product_new = Product(product_name=info["product_name"],
                              category_value=info["category_value"],
                              price=info["price"],
                              photo_path=url,
                              description=info["description"],
                              availability_state=1,
                              source_id=info["source_id"])
        db.session.add(product_new)
        db.session.commit()
        dict1 = to_dict(product_new)
        res = make_response(json.dumps(dict1))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("product options error!")
        return

# user_post_wanted
# post: post a wanted
# need check: photo functions added
@app.route('/userpostwanted', methods=['GET', 'POST', 'OPTIONS'])
def user_post_wanted():
    info = json.loads(request.get_data())
    # directly return
    if request.method == 'GET':
        return
    # post a new product
    elif request.method == 'POST':
        wanted_new = Wanted(wanted_name=info["wanted_name"],
                              category_value=info["category_value"],
                              price=info["price"],
                              description=info["description"],
                              availability_state=1,
                              source_id=info["source_id"])
        db.session.add(wanted_new)
        db.session.commit()
        dict1 = to_dict(wanted_new)
        res = make_response(json.dumps(dict1))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("wanted options error!")
        return

# user_all_products
# post: show all products that have been posted by one specific user
# implemented by lexie, 2021.11.24
@app.route('/userallproducts', methods=['GET', 'POST', 'OPTIONS'])
def user_all_products():
    info = json.loads(request.get_data())
    # directly return
    if request.method == 'GET':
        return
    # search the posted items from a specific user
    elif request.method == 'POST':
        # strategy_first = 0, all products
        if info["strategy_0"] == 0:
            if info["source_id"] != 0:
                search_result = Product.query.filter(Product.source_id == info["source_id"]).all()
            else:
                search_result = Product.query.filter(Product.source_id > 0).all()

        # only want one category
        elif info["strategy_0"] == 1:
            if info["source_id"] != 0:
                search_result = Product.query.filter(and_(Product.source_id == info["source_id"],
                                                     Product.category_value == info["category_value"])).all()
            else:
                search_result = Product.uery.filter(Product.category_value == info["category_value"]).all()

        # different sorting strategies
        # automatically present the product by id
        if info["strategy_1"] == 0:
            search_result_1 = search_result

        # sorted by price
        elif info["strategy_1"] == 1:
            search_result_1 = search_result
            search_result_1.sort(key=take_price)
            # print(search_result_1)

        # sorted by category
        elif info["strategy_1"] == 2:
            search_result_1 = search_result
            search_result_1.sort(key=take_category)

        # change the type of list
        for i in range(len(search_result_1)):
            item_original = search_result_1[i]
            item_modify = to_dict(item_original)
            search_result_1[i] = item_modify

        res = make_response(json.dumps(search_result_1))
        res.headers["Access-Control-Allow-Origin"] = '*'
        print(res)
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("product options error!")
        return

# user_all_wanted
# post: show all wanted that have been posted by one specific user
@app.route('/userallwanted', methods=['GET', 'POST', 'OPTIONS'])
def user_all_wanted():
    info = json.loads(request.get_data())
    # directly return
    if request.method == 'GET':
        return
    # search the posted items from a specific user
    elif request.method == 'POST':
        # strategy_first = 0, all products
        if info["strategy_0"] == 0:
            if info["source_id"] != 0:
                search_result = Wanted.query.filter(Product.source_id == info["source_id"]).all()
            else:
                search_result = Wanted.query.filter(Product.source_id != 0).all()

        # only want one category
        elif info["strategy_0"] == 1:
            if info["source_id"] != 0:
                search_result = Wanted.query.filter(and_(Wanted.source_id == info["source_id"],
                                                     Wanted.category_value == info["category_value"])).all()
            else:
                search_result = Wanted.uery.filter(Wanted.category_value == info["category_value"]).all()

        # different sorting strategies
        # automatically present the product by id
        if info["strategy_1"] == 0:
            search_result_1 = search_result

        # sorted by price
        elif info["strategy_1"] == 1:
            search_result_1 = search_result
            search_result_1.sort(key=take_price)
            # print(search_result_1)

        # sorted by category
        elif info["strategy_1"] == 2:
            search_result_1 = search_result
            search_result_1.sort(key=take_category)

        # change the type of list
        for i in range(len(search_result_1)):
            item_original = search_result_1[i]
            item_modify = to_dict(item_original)
            search_result_1[i] = item_modify

        res = make_response(json.dumps(search_result_1))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("product options error!")
        return

# user_product_search
# post: search one specific posted items
# implemented by lexie, 2021.11.24
@app.route('/userproductsearch', methods=['GET', 'POST', 'OPTIONS'])
def user_product_search():
    info = json.loads(request.get_data())
    if request.method == 'GET':
        return

    # search the posted items from a specific user
    elif request.method == 'POST':
        dict1 = to_dict(Product.query.first())
        print(dict1)
        # search product based on name and source id
        dict_result = to_dict(Product.query.filter(Product.product_name.in_(
            Product.query(Product.product_name)).filter(Product.source_id == info["source_id"])))

        res = make_response(json.dumps(dict_result))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("product options error!")
        return

# user_modify_product
# post: modify the target product according to the latest info
# implemented by lexie, 2021.11.23
# never been checked!
@app.route('/usermodifyproduct', methods=['GET', 'POST', 'OPTIONS'])
def user_modify_product():
    info = json.loads(request.get_data())
    # directly return
    if request.method == 'GET':
        return

    # search the posted items from a specific user
    elif request.method == 'POST':
        dict1 = to_dict(Product.query.first())
        # search the target product based on the id
        target_product = Product.query.filter(and_(Product.product_id == info["product_id"],
                                                   Product.source_id == info["source_id"])).first()
        # modification
        target_product.product_name = info["product_name"]
        target_product.category_value = info["category_value"]
        target_product.price = info["price"]
        target_product.photo = info["photo"]
        target_product.description = info["description"]

        # a successful modification
        response_dict = to_dict(target_product)
        response_dict["result"] = "success"
        res = make_response(json.dumps(response_dict))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("product options error!")
        return

# delete_produt
# post: delete the target product
# implemented by lexie, 2021.11.23
# modified by lexie, 2021.12.21
@app.route('/deleteproduct', methods=['GET', 'POST', 'OPTIONS'])
def delete_product():
    info = json.loads(request.get_data())
    if request.method == 'GET':
        print("delete product get error")
        return

    elif request.method == 'POST':
        product_x = db.session.query(Product).filter(Product.product_id == info["product_id"]).first()
        product_x.source_id = -1
        db.session.add(product_x)
        db.session.commit()
        user_dict = to_dict(product_x)
        print(user_dict)
        user_dict["result"] = "success"
        res = make_response(json.dumps(user_dict))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("delete product options error!")
        return

# plain_search
# post: search the desired product by name
# not user-specific
# implemented by lexie, 2021.11.24
@app.route('/plainsearch', methods=['GET', 'POST', 'OPTIONS'])
def plain_search():
    info = json.loads(request.get_data())
    # directly return
    if request.method == 'GET':
        return

    # search the posted items from a specific user
    elif request.method == 'POST':
        # all categories
        if info["strategy_0"] == 0:
            search_result = Product.query.filter(Product.product_name.in_([info["product_name"]])).all()

        # only want one category
        elif info["strategy_0"] == 1:
            search_result = Product.query.filter(and_(Product.product_name.in_([info["product_name"]]),
                                                      Product.category_value == info["category_value"])).all()

        # automatically present the product by id
        if info["strategy_1"] == 0:
            search_result_1 = search_result

        # sorted by price
        elif info["strategy_1"] == 1:
            search_result_1 = search_result
            search_result_1.sort(key=take_price)

        # sorted by category
        elif info["strategy_1"] == 2:
            search_result_1 = search_result
            search_result_1.sort(key=take_category)

        # change the type of list
        for i in range(len(search_result_1)):
            item_original = search_result_1[i]
            item_modify = to_dict(item_original)
            search_result_1[i] = item_modify

        res = make_response(json.dumps(search_result_1))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("product options error!")
        return

# product_info
# post: show the details of the product
# implemented by lexie, 2021.11.23
# consult Cai for further improvements
@app.route('/productinfo', methods=['GET', 'POST', 'OPTIONS'])
def product_info():
    info = json.loads(request.get_data())

    # directly return
    if request.method == 'GET':
        return

    # search the posted items from a specific user
    elif request.method == 'POST':
        dict1 = to_dict(Product.query.first())
        # search products based on the posted id
        # the result is a list
        # notice: use first as the search condition
        dict_result = to_dict((Product.query.filter(Product.product_id == info["product_id"])).first())
        dict_result["result"] = "success"
        res = make_response(json.dumps(dict_result))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("product options error!")
        return

# log_in
# post: log in and send the status
# implemented by lexie, 2021.11.23
# updated by lexie, 2021.12.8
# need test: log in logic has been changed
@app.route('/login', methods=['GET', 'POST', 'OPTIONS'])
def log_in():
    info = json.loads(request.get_data())

    if request.method == 'GET':
        print("log in get error!")
        return

    # log in status
    elif request.method == 'POST':
        user_cnt = User.query.filter(User.user_name == info["user_name"]).count()
        if user_cnt == 0:
            email_cnt = User.query.filter(User.email == info["email"]).count()
            if email_cnt == 0:
                res = "failed: user name does not exist"
                res.headers["Accesss-Control-Allow-Origin"] = '*'
                return res
            else:
                user_search = to_dict(User.query.filter(User.email == info["email"]).first())
        else:
            # search for the account of the unique user name
            user_search = to_dict(User.query.filter(User.user_name == info["user_name"]).first())

        # check the log in status
        if info["password"] != user_search["password"]:
            user_search["result"] = "failed"
            res = make_response(json.dumps(user_search))
            res.headers["Access-Control-Allow-Origin"] = '*'
            return res

        # correctly log in
        user_search["result"] = "success"
        res = make_response(json.dumps(user_search))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("log in options error!")
        return

# register_x
# post: register a new account
# implemented by lexie, 2021.11.23
# clear
@app.route('/register', methods=['GET', 'POST', 'OPTIONS'])
def register_x():
    info = json.loads(request.get_data())

    if request.method == 'GET':
        print("register get error!")
        return

    # register
    elif request.method == 'POST':
        user_cnt = User.query.filter(User.user_name == info["user_name"]).count()
        if user_cnt != 0:
            user_x = User(user_name=info["user_name"], password=info["password"])
            user_dict = to_dict(user_x)
            user_dict["result"] = "failed"
            res = make_response(json.dumps(user_dict))
            res.headers["Access-Control-Allow-Origin"] = '*'
            return res

        # create a new user account
        user_x = User(user_name=info["user_name"], password=info["password"])
        db.session.add(user_x)
        db.session.commit()

        # response to the front
        user_dict = to_dict(user_x)
        user_dict["result"] = "success"
        res = make_response(json.dumps(user_dict))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("log in options error!")
        return

# change_WeChat
# post: initialize the wechat id
# implemented by lexie, 2021.12.14
@app.route('/changeWeChat', methods=['GET', 'POST', 'OPTIONS'])
def change_WeChat():
    info = json.loads(request.get_data())
    if request.method == 'GET':
        print("change WeChat get error!")
        return
    # register
    elif request.method == 'POST':
        user_x = db.session.query(User).filter(User.id == info["user_id"]).first()
        user_x.WeChat_id=info["WeChat_id"]
        db.session.add(user_x)
        db.session.commit()
        # response to the front
        user_dict = to_dict(user_x)
        user_dict["result"] = "success"
        res = make_response(json.dumps(user_dict))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("change Wechat options error!")
        return

# buy_product
# post: buy a certain product and set its state
# implemented by lexie, 2021.12.14
@app.route('/buyproduct', methods=['GET', 'POST', 'OPTIONS'])
def buy_product():
    info = json.loads(request.get_data())

    if request.method == 'GET':
        print("buy product get error!")
        return

    # register
    elif request.method == 'POST':
        product_x = db.session.query(Product).filter(Product.product_id == info["sold_product_id"]).first()
        if product_x.availability_state == 2:
            user_dict = to_dict(product_x)
            user_dict["result"] = "failed"
            res = make_response(json.dumps(user_dict))
            res.headers["Access-Control-Allow-Origin"] = '*'
            return res

        # create a new user account
        history_x = History(user_provider_id=product_x.source_id,
                            user_purchaser_id=info["buyer_id"],
                            product_id=info["sold_product_id"],
                            time=info["time"])

        db.session.add(history_x)
        db.session.commit()

        product_x.availability_state = 2
        db.session.add(product_x)
        db.session.commit()

        user_x = User.query.filter(User.id == product_x.source_id).first()
        
        # response to the front
        user_dict = to_dict(history_x)
        user_dict["result"] = "success"
        user_dict["seller_wechat"] = user_x.WeChat_id
        res = make_response(json.dumps(user_dict))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("buy product options error!")
        return

# reset_pw
# post: retrieve the password of a certain account
# implemented by lexie, 2021.12.21
@app.route('/resetpw', methods=['GET', 'POST', 'OPTIONS'])
def reset_pw():
    info = json.loads(request.get_data())
    if request.method == 'GET':
        print("reset password get error!")
        return
    # register
    elif request.method == 'POST':
        user_x = db.session.query(User).filter(User.email == info["email"]).first()
        user_x.password = info["new_pw"]
        db.session.add(user_x)
        db.session.commit()
        user_dict = to_dict(user_x)
        user_dict["result"] = "success"
        res = make_response(json.dumps(user_dict))
        res.headers["Access-Control-Allow-Origin"] = '*'
        return res

    # undefined behavior
    elif request.method == 'OPTIONS':
        print("reset password options error!")
        return

# add_favorite
# post: add a product to the favorite folder

# initial function implemented for checking
@app.route('/')
def hello_world():
    return 'Hello world for dm_app_0 on our server.'

# the initialization of new tables
# not used in actual running process
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
