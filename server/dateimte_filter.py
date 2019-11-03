import pandas as pd
import time
import datetime


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


asdf = get_data(1, 1, 2017, 2017, 30)
print(asdf)