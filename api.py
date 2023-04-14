import tinydb
from flask import request, jsonify, Blueprint

rest = Blueprint('api', __name__, template_folder='templates')

user_db = tinydb.TinyDB('store/user.json')


@rest.route('/api/login', methods=['POST'])
def login():
    '''login api'''
    param_json = request.get_json()
    username_ = param_json['username']
    password_ = param_json['password']
    cond = tinydb.Query()
    user_info = user_db.get(cond.username == username_)
    if user_info is not None:
        signup = user_info['password'] = password_
    else:
        signup = False
    return jsonify({
        "code": "0",
        "message": "ok",
        "data": signup
    })
