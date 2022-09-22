import calendar

# print(calendar.calendar(2002))

import datetime
from datetime import datetime, timedelta, date, time

now = (datetime.now())
print(f'{now: %A, %B %d %Y}')

dd = datetime(year=2000, hour=23, day=5, month=7, minute=38)
print(dd)

t = dd + timedelta(days=-10)
print(dd.day)