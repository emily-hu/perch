from flask import Blueprint, jsonify, make_response, request
import sys
sys.path.append("..")
from database import candidates, topics, orgs

candidate_api = Blueprint('candidate_api', __name__)

@candidate_api.route('/orgs/<org_name>/candidates/', methods=['GET','POST'])
def get_or_create_candidate(org_name):
    topic_id = request.args.get('topic_id')
    if not topics.is_topic(topic_id):
        return make_response("Topic does not exist.", 404)
    # TODO: check admin priveleges
    if request.method == 'POST':
        name = request.args.get('name')
        description = request.args.get('description')
        response = candidates.create_candidate(name, description, topic_id)
        return response
    all_c = []
    c_list = candidates.get_candidates(topic_id)
    for c in c_list:
        cand = {}
        cand['name'] = candidates.get_name(c)
        cand['description'] = candidates.get_description(c)
        cand['avg_rating'] = candidates.get_avg_rating(c)
        cand['all_ratings'] = candidates.get_all_ratings(c)
        cand['all_voters'] = candidates.get_all_voters(c)
        all_c.append(cand)
    return jsonify(all_c)


@candidate_api.route('/orgs/<org_name>/candidates/<cand_id>/description/', methods=['PUT'])
def update_candidate_description(org_name, cand_id):
    description = request.args.get('description')
    response = candidates.change_description(cand_id)
    return jsonify({'success':response})

@candidate_api.route('/orgs/<org_name>/candidates/<cand_id>/ratings/', methods=['POST'])
def rate_candidate(org_name, cand_id):
    rating = int(request.args.get('rating'))
    if rating < 1 or rating > 5:
        return make_response(jsonify({'success':False}), 400)
    # TODO: add user to voters list
    response = candidates.add_rating(cand_id, rating)
    return jsonify({'success':response})

@candidate_api.route('/orgs/<org_name>/candidates/<cand_id>/', methods=['DELETE'])
def remove_candidate(org_name, cand_id):
    # TODO: check admin priveleges
    response = candidates.remove_candidate(org_name, cand_id)
    return jsonify({'success':response})
