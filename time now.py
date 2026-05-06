from datetime import date, time, datetime

today = date.today()
now = datetime.now()
print("Today's date is", today)
print("Right now, it's", now)

print("\nDate components", today.day, today.month, today.year)
