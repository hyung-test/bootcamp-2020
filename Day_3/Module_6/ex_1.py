import pandas as pd
# Part 1: read data into data frame
df = pd.read_csv("andre.csv")

# Part 2: remove data from 1979 and after 1993
df = df[ df.Year > 1976]
df = df[ df.Year < 1994]

# Part 3: make a histogram
df.hist("H", bins=100)