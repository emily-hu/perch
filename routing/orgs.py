from flask import Blueprint, jsonify, make_response, request
import sys
sys.path.append("..")
from database import orgs

org_api = Blueprint('org_api', __name__)

@org_api.route('/orgs/<org_name>', methods=['PUT', 'DELETE'])
def create_or_delete_org(org_name):
    if request.method == 'PUT':
        response = orgs.create_org(org_name)
        if response:
            # TODO: get user_id of requester
            orgs.add_admin(org_name, "user_id")
            orgs.add_user(org_name, "user_id")
            return make_response(jsonify({'success': True}), 201)
        else:
            return jsonify({'success': False})
    # TODO:check if request is from an admin
    if orgs.is_org(org_name):
        response = orgs.delete_org(org_name)
        if response:
            return "Successfully deleted."
        else:
            return make_response("An error has occurred.", 400)
    else:
        return make_response("Organization does not exist.", 404)

@org_api.route('/orgs/<org_name>/admins/', methods=['GET', 'POST', 'DELETE']) 
def org_admin(org_name):
    if request.method == 'GET':
        if not orgs.is_org(org_name):
            return make_response(jsonify([]), 404)
        else:
            return jsonify(orgs.get_admins(org_name))
    # TODO: check if request is from admin
    # TODO: check if only one admin is left
    user_id = request.args.get('user_id')
    if request.method == 'DELETE':
        response = orgs.rm_admin(org_name, user_id)
        if response:
            return jsonify({'success':True})
        else:
            return make_response(jsonify({'success':False}), 400)
    response = orgs.add_admin(org_name, user_id)
    if response:
        return jsonify({'success':True})
    else:
        return make_response(jsonify({'success':False}), 400)

@org_api.route('/orgs/<org_name>/users/', methods=['GET', 'POST', 'DELETE'])
def org_user(org_name): 
    if request.method == 'GET':
        if not orgs.is_org(org_name):
            return make_response(jsonify([]), 404)
        else:
            return jsonify(orgs.get_users(org_name))
    # TODO: check if request is from admin
    # TODO: check if only one user is left
    user_id = request.args.get('user_id')
    if request.method == 'DELETE':
        response = orgs.rm_user(org_name, user_id)
        if response:
            return jsonify({'success':True})
        else:
            return make_response(jsonify({'success':False}), 400)
    response = orgs.add_user(org_name, user_id)
    if response:
        return jsonify({'success':True})
    else:
        return make_response(jsonify({'success':False}), 400)
