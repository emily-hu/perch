from flask import Flask, render_template
        
app = Flask(__name__)

@app.route('/users/', methods=['POST'])
def create_user(): # name, email, password
    pass # return json

@app.route('/users/<user_id>/name/', methods=['GET'])
def get_user_name(user_id):
    name = get_name(user_id)
    if len(name) == 0:
        abort(404)
    return name

@app.route('/users/<user_id>/orgs/', methods=['GET'])
def get_user_orgs(user_id):
    org_list = get_orgs(user_id)
    name = get_name(user_id)
    if len(name) == 0:
        abort(404)
    return org_list

@app.route('/users/<user_id>/password/', methods=['PUT'])
def change_password(user_id): # new password
    pass # return success
