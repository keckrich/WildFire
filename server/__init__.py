import os
from flask import Flask, abort, session, request, redirect, render_template
from flask.json import jsonify
from random import randint, uniform, randrange
import pandas as pd
import os

app = Flask(__name__, template_folder='../public',static_folder='../public', static_url_path='')

from server.routes import *
from server.services import *

name = []
for i in range(100):
    name.append([uniform(33, 40), uniform(-121, -115), str(randrange(200, 2000))])


@app.route('/test')
def test():
    return render_template('test.html', name='KYle')


@app.route('/api')
def api():
    print (os.getcwd())
    csv = pd.read_csv("server\ile.csv")
    new = csv[["latitude", "longitude", "PREDICTED"]]
    newlist = new.values.tolist()
   # print (newlist)
    return jsonify(newlist)


@app.route('/getpythondata')
def gpd():
    return jsonify('test')

initServices(app)

if 'FLASK_LIVE_RELOAD' in os.environ and os.environ['FLASK_LIVE_RELOAD'] == 'true':
    import livereload
    app.debug = True
    server = livereload.Server(app.wsgi_app)
    server.serve(port=os.environ['port'], host=os.environ['host'])

			
