import datetime
now = datetime.datetime.now()
valentines = datetime.datetime(2025, 2, 14, 0, 0, 0)
time_left = valentines - now
hours = time_left.total_seconds() / 3600

print("There are " + str(hours) + " hours left until February 14 12:00 AM.")
