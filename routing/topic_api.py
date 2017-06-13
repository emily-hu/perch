from flask import Flask, render_template

app = Flask(__name__)

@app.route('/orgs/<org_name>/topics/', methods=['POST'])
def create_topic(org_name): # name, description, anon
    pass # return topic_id

@app.route('/orgs/<org_name>/topics/', methods=['GET'])
def get_topics(org_name):
    pass # return str array, list of topic ids

@app.route('/orgs/<org_name>/topics/<topic_id>/anon/', methods=['GET'])
def is_anon(org_name, topic_id):
    pass # return bool, anonymity

@app.route('/orgs/org_name>/topics/<topic_id>/', methods=['DELETE'])
def rm_topic(org_name, topic_id):
    pass
