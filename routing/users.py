from flask import Blueprint
import sys
sys.path.append("..")
from database import users

user_api = Blueprint('user_api', __name__)

@user_api.route('/users/', methods=['POST'])
def create_user(): # name, email, password
    pass # return json

@user_api.route('/users/<user_id>/name/', methods=['GET'])
def get_user_name(user_id):
    # name = users.get_name(user_id)
    return user_id

@user_api.route('/users/<user_id>/orgs/', methods=['GET'])
def get_user_orgs(user_id):
    org_list = users.get_orgs(user_id)
    name = get_name(user_id)
    if len(name) == 0:
        abort(404)
    return org_list

@user_api.route('/users/<user_id>/password/', methods=['PUT'])
def change_password(user_id): # new password
    pass # return success
