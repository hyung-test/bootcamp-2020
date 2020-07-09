library(tidyverse)
setwd("/home/h/Git/bootcamp2020/Day_3/Module_6")
# Part 1: Read data into data frame
df <- read_csv("andre.csv", col_name = TRUE)

# Part 2: remove data from 1976 and after 1993
df <- filter(df, Year != 1976)
df <- filter(df, Year < 1994)

# Part 3: make a histogram
ggplot(data=df, aes(df$H)) + geom_histogram()