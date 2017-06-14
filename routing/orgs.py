from flask import Blueprint
import sys
sys.path.append("..")
from database import orgs

org_api = Blueprint('org_api', __name__)

@org_api.route('/orgs/<org_name>', methods=['PUT', 'DELETE'])
def create_org(org_name):
    pass # return json {success: bool}

@org_api.route('/orgs/<org_name>/admins/', methods=['GET', 'POST'])
def org_admin(org_name): # if POST: require user_id and action (add/rm)
    pass # if GET: return str array list of admins

@org_api.route('/orgs/<org_name>/users/', methods=['GET', 'POST'])
def org_user(org_name): # if POST: require user_id and action (add/rm)
    pass # if GET: return str array list of users
