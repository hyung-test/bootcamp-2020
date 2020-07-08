# author: hyung
# date: 2020-Jul-8
# load a random number generator
install.packages("random")
library(random)
# make some random numbers
dataset <- randomSequence(min=1, max=20, col=1, check=TRUE)
sample <- c(1,2,3,4,5)
# make a histogram
hist(dataset)
hist(sample)