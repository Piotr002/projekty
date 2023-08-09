library(dplyr)
library(rstudioapi)
library(tidyr)

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

data <- read.csv("titanic.csv")
data <- data |> 
  dplyr::mutate(Age = tidyr::replace_na(data$Age, mean(na.omit(data$Age))))