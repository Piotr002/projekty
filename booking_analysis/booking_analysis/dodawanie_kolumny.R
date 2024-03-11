library(dplyr)

da <- read.csv("processed_data.csv")
t <- sapply(1:nrow(da), function(i){
  mean(na.omit(as.numeric(da[i, 7:13])))
})

da <- da |> 
  dplyr::mutate(calculated_average=t) |> 
  dplyr::mutate(roznica=abs(calculated_average - average_opinion))
