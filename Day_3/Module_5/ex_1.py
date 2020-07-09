from datetime import datetime
import time


# with datetime module
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time is ", current_time)

# with time module
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("Current Time is ", current_time)

# sources: https://www.programiz.com/python-programming/datetime/current-time
