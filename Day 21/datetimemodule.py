#           Python Begineer Boost

#           Datetime Module in Python

import datetime

current_date = datetime.date.today()
print(current_date)
current_time = datetime.datetime.now().time()
print(current_time)

formatted_date = current_date.strftime("%B %d %Y")
print(formatted_date)
formatted_time = current_time.strftime("%I:%M %p")
print(formatted_time)


some_date = datetime.datetime(2020,12,1)
print(some_date)

new_date = some_date - datetime.timedelta(30)
print(new_date)