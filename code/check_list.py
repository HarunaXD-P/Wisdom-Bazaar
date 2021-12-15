from flask import Flask
from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask import request
import json
from init import db
from database import User, Product
from sqlalchemy import and_, or_

random = [(2, 2), (3, 4), (4, 1), (1, 3)]

dict_result = dict(random)
print("dict result")
print(dict_result)
json_out = json.dumps(dict_result)
print("json out")
print(json_out)