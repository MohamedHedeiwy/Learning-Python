from datetime import *

# the first number represents hours then minuits etc..
mytime = time(15, 20, 23)
print('This is a predefined time: ', mytime)
# can grab by hour by just calling it also can call by minute etc..
print('Selecting the hours from the predefined time: ', mytime.hour)

print()

# printing today's date use today().month,year or day to grab each individually
print('Today\'s date: ', date.today())

print()

# ctime wont include time
print('ctime will print the date in this fomat: ', date.today().ctime())

print()

# date time will include time
print('Date time will print date in this format: ',datetime(2021, 10, 3, 14, 20, 1))
