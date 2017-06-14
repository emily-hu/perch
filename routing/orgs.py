from flask import Flask, render_template
import sys
sys.path.append("..")
from database import orgs

app = Flask(__name__)

@app.route('/orgs/<org_name>', methods=['PUT', 'DELETE'])
def create_org(org_name):
    pass # return json {success: bool}

@app.route('/orgs/<org_name>/admins/', methods=['GET', 'POST'])
def org_admin(org_name): # if POST: require user_id and action (add/rm)
    pass # if GET: return str array list of admins

@app.route('/orgs/<org_name>/users/', methods=['GET', 'POST'])
def org_user(org_name): # if POST: require user_id and action (add/rm)
    pass # if GET: return str array list of users
