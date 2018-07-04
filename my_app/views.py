from my_app import app
import logging

from flask import render_template, flash, redirect, url_for, request, session,jsonify
import sys

# User Passwords kept here
from my_app import my_secrets

logging.basicConfig(level=logging.DEBUG)
print ('hello from views')


@app.route('/', methods=['GET', 'POST'])
def login():
    print ("request is a",request.method)
    print ("Looking for: ",url_for('static',filename='images/ta_logo.png'))
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == my_secrets.passwords["USER_PASSWORD"]:
            print('found password')
            session['user'] = request.form['username']
            return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/index')
def index():
    # Check in on a DB here
    my_ver = sys.version
    print (dir(app))
    logging.debug(app)
    return render_template('index.html',my_ver = my_ver)
