import os
from flask import Flask, abort, session, request, redirect, render_template
from flask.json import jsonify
from random import randint

app = Flask(__name__, template_folder="../public", static_folder="../public", static_url_path='')

from server.routes import *
from server.services import *

name = []
for i in range(100):
	name.append([randint(-90,90), randint(-180,180), "250"])

@app.route('/test')
def test():
    return render_template('test.html', name=name)
	
@app.route('/api')
def api():
	return jsonify(name)

initServices(app)

if 'FLASK_LIVE_RELOAD' in os.environ and os.environ['FLASK_LIVE_RELOAD'] == 'true':
	import livereload
	app.debug = True
	server = livereload.Server(app.wsgi_app)
	server.serve(port=os.environ['port'], host=os.environ['host'])
