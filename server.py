from flask import Flask, request
from flask_cors import CORS
import logging
import sqlite3
import json
import os
import re

dirname = os.path.dirname(__file__)
app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

cors = CORS(app)
park = {}
climate = {}

def update_climate(climate_state):
	global climate
	climate = climate_state

def update_park(park_state):
	global park
	park = park_state

@app.route("/climate", methods=["GET"])
def get_climate():
	global climate
	return json.dumps(climate, indent=4, sort_keys=True)

@app.route("/park", methods=["GET"])
def get_park():
	global park
	return json.dumps(park, indent=4, sort_keys=True)

@app.route("/", methods=["GET"])
def get_all():
	return "blah"

def run():
	app.run(port=8888, host='0.0.0.0', use_reloader=False)