import time
# Exercise: Make a Simple Stopwatch

tic = time.time()

for i in range(1000000):
    j = i + 10
    
toc = time.time()
time_elapsed = toc - tic
print(time_elapsed)
