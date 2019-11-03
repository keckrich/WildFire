import os
from flask import Flask, abort, session, request, redirect, render_template
from flask.json import jsonify
from random import randint, uniform, randrange
import pandas as pd
import os
import datetime

app = Flask(__name__, template_folder='../public',static_folder='../public', static_url_path='')

from server.routes import *
from server.services import *

name = []
for i in range(100):
    name.append([uniform(33, 40), uniform(-121, -115), str(randrange(200, 2000))])


@app.route('/test')
def test():
    return render_template('test.html', name='KYle')


@app.route('/api/<startmonth>/<endmonth>/<startyear>/<endyear>/<confidence>')
def api(startmonth, endmonth, startyear, endyear, confidence):
    print (startmonth, endmonth, startyear, endyear, confidence)
    result = get_data(int(startmonth), int(endmonth), int(startyear), int(endyear), int(confidence))
    return jsonify(result)


@app.route('/getpythondata')
def gpd():
    return jsonify('test')


def get_data(startmonth, endmonth, startyear, endyear, confidence):
    csv = pd.read_csv("server/predict_subset.csv")

    csv['acq_date'] = pd.to_datetime(csv['acq_date'])

    if endmonth == 2:
        dai = 28
    elif endmonth == 4 or endmonth == 6 or endmonth == 9 or endmonth == 11:
        dai = 30
    else:
        dai = 31
    startdate = datetime.datetime(year=startyear, month=startmonth, day=1)
    enddate = datetime.datetime(year=endyear, month=endmonth, day=dai)

    new = csv[ (csv['acq_date'] >= startdate) & (csv['acq_date'] <= enddate) ]
    new = new.drop("acq_date", 1)

    new = new[ new["PREDICTED"] >= confidence ]

    new = new.values.tolist()

    return new
	
	
initServices(app)

if 'FLASK_LIVE_RELOAD' in os.environ and os.environ['FLASK_LIVE_RELOAD'] == 'true':
    import livereload
    app.debug = True
    server = livereload.Server(app.wsgi_app)
    server.serve(port=os.environ['port'], host=os.environ['host'])

			
