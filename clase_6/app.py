#!/usr/bin/python3

import pickle
import base64
from flask import Flask, request

app = Flask(__name__)

@app.route("/vuln", methods = ["POST"])

def vuln():
	data = base64.urlsafe_b64decode(request.form['pickled'])
	deserialized = pickle.loads(data)

	return '', 204
