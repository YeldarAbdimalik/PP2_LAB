#task 1

from datetime import datetime, timedelta

today = datetime.now()
new_date = today - timedelta(days=5)

print("Today:", today)
print("5 days ago:", new_date)

#task 2

from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#task 3

from datetime import date, timedelta

today = date.today()
print("Yesterday:", today - timedelta(days=1))
print("Today:", today)
print("Tomorrow:", today + timedelta(days=1))

#task  4

from datetime import datetime

date1 = datetime(2026, 2, 20, 10, 0, 0)
date2 = datetime(2026, 2, 25, 12, 0, 0)

difference = date2 - date1

seconds = difference.total_seconds()

print("Difference in seconds:", seconds)