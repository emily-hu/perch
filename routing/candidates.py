from flask import Blueprint

candidate_api = Blueprint('candidate_api', __name__)

@candidate_api.route('/orgs/<org_name>/candidates/', methods=['POST'])
def create_topic(org_name): # name, description, topic_id
    pass # return cand_id

@candidate_api.route('/orgs/<org_name>/candidates/', methods=['GET'])
def get_cand(org_name): # topic_id
    pass # return json

@candidate_api.route('/orgs/<org_name>/candidates/<cand_id>/description', methods=['PUT'])
def update_cand_description(org_name, cand_id): # description
    pass

@candidate_api.route('/orgs/<org_name>/candidates/<cand_id>/ratings', methods=['POST'])
def rate_cand(org_name, cand_id): # rating (int 1 to 5)
    pass

@candidate_api.route('/orgs/<org_name>/candidates/<cand_id>/', methods=['DELETE'])
def rm_cand(org_name, cand_id):
    pass
