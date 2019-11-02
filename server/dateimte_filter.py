import pandas as pd
import time
import datetime

csv = pd.read_csv("predict_subset.csv")

csv['acq_date'] = pd.to_datetime(csv['acq_date'])

print(len(csv))

startmonth = 1
startday = 1
startyear = 2017

startdate = datetime.datetime(year=startyear, month=startmonth, day=startday)

endmonth = 2
endday = 2
endyear = 2017

enddate = datetime.datetime(year=endyear, month=endmonth, day=endday)

new = csv[ (csv['acq_date'] >= startdate) & (csv['acq_date'] <= enddate) ]

new = new.values.tolist()

print("success")