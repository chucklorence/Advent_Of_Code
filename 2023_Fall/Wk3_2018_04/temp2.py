'''
import datetime

# Create a list of datetime objects
datetime_list = [datetime.datetime(2023, 3, 8, 0, 0),
                 datetime.datetime(2023, 3, 8, 9, 0),
                 datetime.datetime(2023, 3, 8, 10, 0),
                 datetime.datetime(2023, 3, 8, 11, 0),
                 datetime.datetime(2023, 3, 8, 12, 0)]

# Find the datetime objects within 90 minutes of midnight
midnight_datetimes = [dt for dt in datetime_list if (dt - datetime.datetime(2023, 3, 8, 0, 0)).total_seconds() // 60 >= 90]

# Print the datetime objects within 90 minutes of midnight
for datetime in midnight_datetimes:
    print(datetime)
'''


import datetime

# Get the specific date and time
specific_datetime = datetime.datetime(2023, 3, 8, 0, 0, 0)

# Create a list of all the datetime objects in the list
datetime_list = [datetime.datetime(2023, 3, 8, 0, 10, 0),
                 datetime.datetime(2023, 3, 7, 23, 55, 0),
                 datetime.datetime(2023, 3, 8, 13, 0, 0),
                 datetime.datetime(2023, 3, 8, 14, 0, 0),
                 datetime.datetime(2023, 3, 8, 15, 0, 0)]

# Find the objects within 90 minutes of the specific datetime object
within_90_minutes = [datetime_object for datetime_object in datetime_list if (datetime_object - specific_datetime).total_seconds() < 5400]

# Print the list of objects within 90 minutes of the specific datetime object
print(within_90_minutes)

# 1518-10-09 23:57
dt = datetime.datetime(1518, 10, 9, 23, 57, 0)

str_dt = dt.strftime('%Y-%m-%d %H:%M:%S')

print(str_dt)