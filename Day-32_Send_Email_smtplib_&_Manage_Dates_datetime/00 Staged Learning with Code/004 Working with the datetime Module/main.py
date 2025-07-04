# 004: Working with the datetime Module


import datetime as dt

now = dt.datetime.now()

year = now.year
print(year)

month = now.month
print(month)

day_of_week = now.weekday()
print(day_of_week + 1)          # add 1 because counting starts from 0

date_of_birth = dt.datetime(year=2002, month=2, day=1, hour=4)
print(date_of_birth)