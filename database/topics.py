from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

def create_topic(org_name, name, description, anon):
    return "fa17"

def is_topic(topic_id):
    return True

def get_topics(org_name):
    return ["fa17", "fc17"]

def is_anon(org_name, topic_id):
    return False

def remove_topic(org_name, topic_id):
    return True
