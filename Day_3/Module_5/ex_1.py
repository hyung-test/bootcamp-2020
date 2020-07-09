from datetime import datetime
import time
# Exercise: Print the Time

# with datetime module
now = datetime.now()
current_time = now.strftime("%H:%M:%S %p")
print("Current Time is ", current_time)

# with time module
t = time.localtime()
current_time = time.strftime("%H:%M:%S %p", t)
print("Current Time is ", current_time)

# sources: https://www.programiz.com/python-programming/datetime/current-time
