# featureAnalysis.R

# Chu Luo

setwd("d:/Chu Doc/research/2018/meta learning/virus")


train <- read.csv("2010-2013X.csv")

for (i in c(1:479)){
  
  uniqueSet = as.data.frame(unique(train[,i]))
  
  uniqueCount= nrow(uniqueSet)
  
  if(uniqueCount>1)
  {
    print("feature number ")
    print(i)
    print("count is ")
    print(uniqueCount)
  }
  
}

uniqueSet = as.data.frame(unique(train[,21]))

uniqueCount= nrow(uniqueSet)

uniqueItems = as.data.frame(train[,21])


test <- read.csv("2014X.csv")


uniqueSet = as.data.frame(unique(test[,21]))

uniqueCount= nrow(uniqueSet)

uniqueItems = as.data.frame(test[,21])


zcount = 0 
for (i in c(1:25538)){
  
  if (test[i,21] == 0)
  {
    zcount = zcount + 1
  }
  
}

