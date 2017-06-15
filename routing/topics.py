from flask import Blueprint, jsonify, make_response, request
import sys
sys.path.append("..")
from database import topics, orgs

topic_api = Blueprint('topic_api', __name__)

@topic_api.route('/orgs/<org_name>/topics/', methods=['GET','POST'])
def create_topic(org_name):
    if request.method == 'GET':
        # TODO: check that user is in org
        if orgs.is_org(org_name):
            return jsonify(topics.get_topics(org_name))
        else:
            return make_response(jsonify([]), 404)
    # TODO: check for admin priveleges
    if org.is_org(org_name):
        name = request.args.get('name')
        description = request.args.get('description')
        anon = request.args.get('anon')
        response = topics.create_topic(org_name, name, description, anon)
        return response
    else:
        return make_resposne("This organization does not exist.", 404)

@topic_api.route('/orgs/<org_name>/topics/<topic_id>/anon/', methods=['GET'])
def is_anon(org_name, topic_id):
    # TODO: make sure user is in the organization
    return jsonify({'anon':topics.is_anon(org_name, topic_id)})

@topic_api.route('/orgs/<org_name>/topics/<topic_id>/', methods=['DELETE'])
def remove_topic(org_name, topic_id):
    # TODO: check that user is admin of org
    response = topics.remove_topic(org_name,topic_id)
    return jsonify({'success':response})
