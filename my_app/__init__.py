# Get things started and initialized here
import os
from base64 import b64encode

#Creating the Flask app must happen FIRST
from flask import Flask
app = Flask(__name__)

# Assign App Config Variables / Create a random token for Flask Session
token = os.urandom(64)
token = b64encode(token).decode('utf-8')
app.config['SECRET_KEY']= token

# Get the Passwords and Keys
from my_app import my_secrets
print ("I have a DB Password: ",my_secrets.passwords["DB_PASSWORD"])
print ("I have an API Key: ",my_secrets.passwords["SS_TOKEN"])

#Now get all views and models in
from my_app import views
from my_app import models

print ('hello from __init__')