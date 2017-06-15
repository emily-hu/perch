from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

def create_candidate(name, description, topic_id):
    return "psat"

def get_candidates(topic_id):
    return ['psat', 'psat2']

def get_name(cand_id):
    return "Priyanka Satpute"

def get_description(cand_id):
    return "So good"

def change_description(cand_id):
    return True

def get_avg_rating(cand_id):
    return 10

def get_all_ratings(cand_id):
    return [10, 10]

def add_rating(cand_id, rating):
    return True

def get_all_voters(cand_id):
    return ['emilyhu', 'tcqin']

def add_voter(cand_id, user_id):
    return True

def remove_candidate(org_name, cand_id):
    return True
