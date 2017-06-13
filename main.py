from flask import Flask, render_template, redirect, session, url_for, request, escape

app = Flask(__name__)

@app.route('/')
def main():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'
    # return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('/'))
    return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

app.secret_key = 'jdkaslti543y8uarief'
