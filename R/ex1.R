library(tidyverse)
print('hello world')
myphrase <- "goodbye"
class(myphrase)
print(myphrase)

c(2,4,6)
2:6
seq(2, 3, by=0.5)

x=rep(c(2,4,6), each=3)
print(x)
x[3]
table(x)
unique(x)

for (i in 1:4){
  j <- i + 10
  print(j)
}

print(i)
while (i<5){
  print(i)
  i <- i + 1
}

if (i>3){
  print('Yes')
} else {
  print('No')
}

square <-function(x){
  squared <- x*x
  return(squared)
}
