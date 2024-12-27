import datetime

dtBirth = datetime.date(1991,12,8)
print(dtBirth.weekday())

dtNow = datetime.date.today()
print(dtBirth < dtNow)

life =dtNow - dtBirth
print(life.days, life.total_seconds())

delta = datetime.timedelta(days = -10)
newDate = dtNow + delta
print(newDate.year, newDate.month, newDate.day, newDate.weekday())
print(newDate.strftime(r'%m/%d/%y'))

newDate = datetime.datetime.strptime("2020.08.05", "%Y.%m.%d")
print(newDate.strftime("%Y%m%d"))