# Exercise: Make a Simple Stopwatch
tic=proc.time()[3]

for (i in 1:1000000){
  j <- i + 10
}

toc=proc.time()[3]
time_elapsed = toc - tic
print(time_elapsed)