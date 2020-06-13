from datetime import datetime

birthday=datetime(1994,2,15,4,25,12)
birthday.month
birthday.year
birthday.weekday()
datetime.now()-datetime(2017,1,1)

date=datetime.strptime("Jan 15, 2018","%b %d, %Y")
date.month

date_str=datetime.strftime(datetime.now(), "%b %d, %Y")
date_str