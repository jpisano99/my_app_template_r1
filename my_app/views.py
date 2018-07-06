from my_app import app
from flask import render_template, flash, redirect, url_for, request, session,jsonify
from my_app.cascade_select import *
import json
import logging
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
    logging.debug(app)
    return render_template('basic_index.html',my_ver = my_ver)


@app.route('/get_levels' ,methods=['GET','POST'])
def get_levels():
    if request.method == 'POST':
        hierarchy = json.loads((request.data).decode("utf-8"))
        levelArray = build_sales_list(hierarchy)
        return jsonify({'levels': levelArray})
    else:
        return render_template('cascade_select.html')


#
# Error handling pages
#


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500