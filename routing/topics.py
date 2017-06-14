from flask import Blueprint

topic_api = Blueprint('topic_api', __name__)

@topic_api.route('/orgs/<org_name>/topics/', methods=['POST'])
def create_topic(org_name): # name, description, anon
    pass # return topic_id

@topic_api.route('/orgs/<org_name>/topics/', methods=['GET'])
def get_topics(org_name):
    pass # return str array, list of topic ids

@topic_api.route('/orgs/<org_name>/topics/<topic_id>/anon/', methods=['GET'])
def is_anon(org_name, topic_id):
    pass # return bool, anonymity

@topic_api.route('/orgs/org_name>/topics/<topic_id>/', methods=['DELETE'])
def rm_topic(org_name, topic_id):
    pass
