import os
import csv
import scipy
import random
import numpy as np
from matplotlib import pyplot as plt
os.chdir('/home/h/Git/bootcamp2020/Python')
with open('csv.html',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        
r = random.randint(1, 10)

data = []
for i in range(10):
    print(i)
    data.append(random.randint(1,10))
    
plt.hist(data, bins=20)
plt.show()