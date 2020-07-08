import os
import csv
os.chdir('/home/h/Git/bootcamp2020/Python')
with open('csv.html',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
