import os
from flask import Flask, abort, session, request, redirect, render_template
from flask.json import jsonify

app = Flask(__name__, template_folder="../public", static_folder="../public", static_url_path='')

from server.routes import *
from server.services import *

name = ["Kyle","Ryan", "Eric"]

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
