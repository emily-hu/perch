from flask import Flask, render_template# , redirect, session, url_for, request, escape
from routing import orgs, users, topics, candidates

app = Flask(__name__)

app.register_blueprint(orgs.org_api)
app.register_blueprint(users.user_api)
app.register_blueprint(topics.topic_api)
app.register_blueprint(candidates.candidate_api)

@app.route('/')
def main():
    # if 'username' in session:
    #     return 'Logged in as %s' % escape(session['username'])
    # return 'You are not logged in'
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # if request.method == 'POST':
    #     session['username'] = request.form['username']
    #     return redirect(url_for('main'))
    return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.errorhandler(403)
def forbidden(error):
    return 'This content is forbidden', 403

@app.errorhandler(400)
def bad_request(error):
    return 'Bad request', 400

# app.secret_key = 'jdkaslti543y8uarief'
