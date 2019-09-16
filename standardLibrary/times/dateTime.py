from datetime import datetime
import time

dt = datetime(2018, 1, 1)

print(dt)


currentDay = datetime.now()
print('currentDay', currentDay)


formatTime = datetime.strptime('2018/01/01', '%Y/%m/%d')

print('formatTime', formatTime)

date = datetime.fromtimestamp(time.time())
print('date', date)

print(dt.year)
print(dt.month)
print(dt.day)

