import datetime
tm = datetime.datetime.now()
print(tm)
print(tm.year,tm.month,tm.day,tm.hour,tm.minute,
      tm.second,tm.microsecond)

tm1 = datetime.datetime(2024, 7, 18,
                       9, 0, 0)
print(tm1)
print(tm1.strftime("%Y%m%d %H:%M:%S"))
print(tm1.strftime("%Y%m%d %I:%M:%S %p"))

tm2 = datetime.datetime.strptime("2013.8.10 22:31:42",
                                 "%Y.%m.%d %H:%M:%S")
delta = tm - tm2
print(delta)
