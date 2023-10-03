library(dplyr)
library(rstudioapi)
library(ggplot2)

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

data <- read.csv("Kwatermistrz - Baza.csv") |> 
  dplyr::mutate(Rok.urodzenia=as.numeric(Rok.urodzenia))

ggplot(data) +
  geom_histogram(aes(y=Rok.urodzenia)) +
  coord_flip()

data$Rok.urodzenia |> na.omit() |> mean()

years <- data$Rok.urodzenia |> unique() |> na.omit()

values <- sapply(years, function(i){
  sum(na.omit(data$Rok.urodzenia == i))
})


data2 <- tibble::tibble(ilosc = values)

row.names(data2) <- as.character(years)


