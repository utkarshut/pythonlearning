import datetime

d = datetime.date(2017, 7, 28)  # not allow (2017, 07, 28)
print(d)

tday = datetime.date.today()

print(tday, tday.year, tday.day, tday.month)

print(tday.weekday())  # monday 0 sunday 6
print(tday.isoweekday())  # mondat 1 sunday 7

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)
print(tday - tdelta)

bday = datetime.date(1993, 9, 10)

print((tday - bday).days)

print((tday - bday).total_seconds())

dt = datetime.datetime(2019, 10, 8, 12, 34, 55, 1000)

print(dt)
print(dt.time())
print(dt.date())
print(dt.year)

tdelta1 = datetime.timedelta(days=1)  # hours=12
print(dt + tdelta1)

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

import pytz

print('timezone', datetime.datetime(2019, 11, 2, 12, 34, tzinfo=pytz.UTC))

mtn_tz= pytz.timezone('Asia/Calcutta')
# for tz in pytz.all_timezones:
#     print(tz)
current=datetime.datetime.now()

print(mtn_tz.localize(current))

#https://docs.python.org/2/library/datetime.html