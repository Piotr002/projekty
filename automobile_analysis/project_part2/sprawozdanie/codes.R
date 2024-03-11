five_fold_cv_conf_matrix <- function(dataset, class, classifier){
  conf <- matrix(0, 5, 5)
  rownames(conf) <- c(-1, 0, 1, 2, 3)
  colnames(conf) <- c(-1, 0, 1, 2, 3)
  splits <- createFolds(class, k = 5, list = FALSE, returnTrain = FALSE)
  datasets <- list(dataset[splits==1,],
                   dataset[splits==2,],
                   dataset[splits==3,],
                   dataset[splits==4,],
                   dataset[splits==5,])
  
  classes <- list(class[splits==1] |> as.numeric(),
                  class[splits==2] |> as.numeric(),
                  class[splits==3] |> as.numeric(),
                  class[splits==4] |> as.numeric(),
                  class[splits==5] |> as.numeric())
  bind_datasets <- list(rbind(datasets[[2]], datasets[[3]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[3]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[3]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[3]], datasets[[4]]))
  bind_classes <- list(c(classes[[2]], classes[[3]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[3]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[3]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[3]], classes[[4]]))
  for (i in 1:5){
    class1 <- bind_classes[[i]] |> as_tibble() |> 
      mutate(value=ifelse(bind_classes[[i]]==-1, 1, 0)) |> 
      dplyr::pull()
    class2 <- bind_classes[[i]] |> as_tibble() |> 
      mutate(value=ifelse(bind_classes[[i]]==0, 1, 0)) |> 
      dplyr::pull()
    class3 <- bind_classes[[i]] |> as_tibble() |> 
      mutate(value=ifelse(bind_classes[[i]]==1, 1, 0)) |> 
      dplyr::pull()
    class4 <- bind_classes[[i]] |> as_tibble() |> 
      mutate(value=ifelse(bind_classes[[i]]==2, 1, 0)) |> 
      dplyr::pull()
    class5 <- bind_classes[[i]] |> as_tibble() |> 
      mutate(value=ifelse(bind_classes[[i]]==3, 1, 0)) |> 
      dplyr::pull()
    lm1 <- classifier(class1 ~ ., data=bind_datasets[[i]])
    lm2 <- classifier(class2 ~ ., data=bind_datasets[[i]])
    lm3 <- classifier(class3 ~ ., data=bind_datasets[[i]])
    lm4 <- classifier(class4 ~ ., data=bind_datasets[[i]])
    lm5 <- classifier(class5 ~ ., data=bind_datasets[[i]])
    predicted <- unlist(sapply(1:nrow(bind_datasets[[i]]), function(j){
      c(predict(lm1, datasets[[i]][j, ]), predict(lm2, datasets[[i]][j, ]), predict(lm3, datasets[[i]][j, ]),
        predict(lm4, datasets[[i]][j, ]), predict(lm5, datasets[[i]][j, ])) |> 
        which.max()
    })) %>%
      replace(.==1, -1) %>%
      replace(.==2, 0) %>%
      replace(.==3, 1) %>%
      replace(.==4, 2) %>%
      replace(.==5, 3)
    for (k in 1:length(predicted)){
      conf[as.numeric(predicted[k]), as.numeric(classes[[i]][k])] <- conf[as.numeric(predicted[k]), as.numeric(classes[[i]][k])] + 1
    }
  }
  conf
}


five_fold_cv_logistic_conf_matrix <- function(dataset, class, classifier){
  splits <- createFolds(class, k = 5, list = FALSE, returnTrain = FALSE)
  conf <- matrix(0, 5, 5)
  rownames(conf) <- c(-1, 0, 1, 2, 3)
  colnames(conf) <- c(-1, 0, 1, 2, 3)
  datasets <- list(dataset[splits==1,],
                   dataset[splits==2,],
                   dataset[splits==3,],
                   dataset[splits==4,],
                   dataset[splits==5,])
  
  classes <- list(class[splits==1] |> as.numeric(),
                  class[splits==2] |> as.numeric(),
                  class[splits==3] |> as.numeric(),
                  class[splits==4] |> as.numeric(),
                  class[splits==5] |> as.numeric())
  bind_datasets <- list(rbind(datasets[[2]], datasets[[3]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[3]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[3]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[3]], datasets[[4]]))
  bind_classes <- list(c(classes[[2]], classes[[3]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[3]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[3]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[3]], classes[[4]]))
  for (i in 1:5){
    class1 <- bind_classes[[i]] |> as_tibble() |> 
      mutate(value=ifelse(bind_classes[[i]]==-1, 1, 0)) |> 
      dplyr::pull()
    class2 <- bind_classes[[i]] |> as_tibble() |> 
      mutate(value=ifelse(bind_classes[[i]]==0, 1, 0)) |> 
      dplyr::pull()
    class3 <- bind_classes[[i]] |> as_tibble() |> 
      mutate(value=ifelse(bind_classes[[i]]==1, 1, 0)) |> 
      dplyr::pull()
    class4 <- bind_classes[[i]] |> as_tibble() |> 
      mutate(value=ifelse(bind_classes[[i]]==2, 1, 0)) |> 
      dplyr::pull()
    class5 <- bind_classes[[i]] |> as_tibble() |> 
      mutate(value=ifelse(bind_classes[[i]]==3, 1, 0)) |> 
      dplyr::pull()
    glm1 <- classifier(class1 ~ ., data=bind_datasets[[i]], family = binomial)
    glm2 <- classifier(class2 ~ ., data=bind_datasets[[i]], family = binomial)
    glm3 <- classifier(class3 ~ ., data=bind_datasets[[i]], family = binomial)
    glm4 <- classifier(class4 ~ ., data=bind_datasets[[i]], family = binomial)
    glm5 <- classifier(class5 ~ ., data=bind_datasets[[i]], family = binomial)
    predicted <- unlist(sapply(1:nrow(bind_datasets[[i]]), function(j){
      c(predict(glm1, datasets[[i]][j, ]), predict(glm2, datasets[[i]][j, ]), predict(glm3, datasets[[i]][j, ]),
        predict(glm4, datasets[[i]][j, ]), predict(glm5, datasets[[i]][j, ])) |> 
        which.max()
    })) %>%
      replace(.==1, -1) %>%
      replace(.==2, 0) %>%
      replace(.==3, 1) %>%
      replace(.==4, 2) %>%
      replace(.==5, 3)
    for (k in 1:length(predicted)){
      conf[as.numeric(predicted[k]), as.numeric(classes[[i]][k])] <- conf[as.numeric(predicted[k]), as.numeric(classes[[i]][k])] + 1
    }
  }
  conf
}

knn_accuracy <- function(dataset, class, opt_k){
  splits <- createFolds(class, k = 5, list = FALSE, returnTrain = FALSE)
  conf1 <- matrix(0, 5, 5)
  rownames(conf1) <- c(-1, 0, 1, 2, 3)
  colnames(conf1) <- c(-1, 0, 1, 2, 3)
  
  conf2 <- matrix(0, 5, 5)
  rownames(conf2) <- c(-1, 0, 1, 2, 3)
  colnames(conf2) <- c(-1, 0, 1, 2, 3)
  
  datasets <- list(dataset[splits==1,],
                   dataset[splits==2,],
                   dataset[splits==3,],
                   dataset[splits==4,],
                   dataset[splits==5,])
  
  
  classes <- list(class[splits==1] |> as.numeric(),
                  class[splits==2] |> as.numeric(),
                  class[splits==3] |> as.numeric(),
                  class[splits==4] |> as.numeric(),
                  class[splits==5] |> as.numeric())
  
  bind_datasets <- list(rbind(datasets[[2]], datasets[[3]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[3]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[3]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[3]], datasets[[4]]))
  
  
  bind_classes <- list(c(classes[[2]], classes[[3]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[3]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[3]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[3]], classes[[4]]))
  
  
  for (i in 1:5){
    predicted.labels1 <- class::knn(bind_datasets[[i]], datasets[[i]], bind_classes[[i]], k = opt_k)
    confusion.matrix1 <- table(predicted.labels1, classes[[i]])
    conf1 <- conf1 + confusion.matrix1
    
    predicted.labels2 <- class::knn(bind_datasets[[i]], bind_datasets[[i]], bind_classes[[i]], k = opt_k)
    confusion.matrix2 <- table(predicted.labels2, bind_classes[[i]])
    conf2 <- conf2 + confusion.matrix2
  }
  list(conf1, conf2)
}

five_fold_cv_LDA_conf_matrix <- function(dataset, class){
  splits <- createFolds(class, k = 5, list = FALSE, returnTrain = FALSE)
  conf <- matrix(0, 5, 5)
  rownames(conf) <- c(-1, 0, 1, 2, 3)
  colnames(conf) <- c(-1, 0, 1, 2, 3)
  datasets <- list(dataset[splits==1,],
                   dataset[splits==2,],
                   dataset[splits==3,],
                   dataset[splits==4,],
                   dataset[splits==5,])
  
  classes <- list(class[splits==1] |> as.numeric(),
                  class[splits==2] |> as.numeric(),
                  class[splits==3] |> as.numeric(),
                  class[splits==4] |> as.numeric(),
                  class[splits==5] |> as.numeric())
  bind_datasets <- list(rbind(datasets[[2]], datasets[[3]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[3]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[4]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[3]], datasets[[5]]),
                        rbind(datasets[[1]], datasets[[2]], datasets[[3]], datasets[[4]]))
  bind_classes <- list(c(classes[[2]], classes[[3]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[3]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[4]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[3]], classes[[5]]),
                       c(classes[[1]], classes[[2]], classes[[3]], classes[[4]]))
  for (i in 1:5){
    model <- MASS::lda(bind_classes[[i]]~., data=bind_datasets[[i]] |> janitor::remove_constant())
    predicted.labels <- predict(model, datasets[[i]])$class
    confusion.matrix <- table(predicted.labels, classes[[i]])
    conf <- conf + confusion.matrix
  }
  conf
}

five_fold_ctree <- function(dataset, class){
  dataset <- dataset |> dplyr::mutate(class=class)
  train_control <- caret::trainControl(method = "repeatedcv",
                                       number = 5,
                                       repeats = 1) 
  
  tune_grid <- expand.grid(cp=c(0.001, 0.01, 0.1))
  
  cv_tree <- caret::train(class~., data=dataset,
                          method="rpart",
                          trControl=train_control,
                          tuneGrid=tune_grid,
                          maxdepth=20,
                          minbucket=5)
  cv_tree
}

rf_5_fold_cv <- function(dataset, class){
  dataset <- dataset |> dplyr::mutate(class=class)
  train_control <- caret::trainControl(method = "repeatedcv",
                                       number = 5,
                                       repeats = 1) 
  
  tune_grid <- expand.grid(.mtry=(round(sqrt(ncol(dataset)))-1):(round(sqrt(ncol(dataset)))+2))
  
  cv_rf <- caret::train(class~., data=dataset,
                        method="rf",
                        metric="Accuracy",
                        trControl=train_control,
                        tuneGrid=tune_grid)
  cv_rf
}

svm_5_fold_lin <- function(dataset, class){
  dataset <- dataset |> dplyr::mutate(class=class)
  train_control <- caret::trainControl(method = "repeatedcv",
                                       number = 5,
                                       repeats = 1) 
  
  cv_svm <- caret::train(class~., data=dataset,
                         method="svmLinear",
                         trControl=train_control,
                         tuneLength=4)
  cv_svm
}

svm_5_fold_radial <- function(dataset, class){
  dataset <- dataset |> dplyr::mutate(class=class)
  train_control <- caret::trainControl(method = "repeatedcv",
                                       number = 5,
                                       repeats = 1) 
  
  cv_svm <- caret::train(class~., data=dataset,
                         method="svmRadial",
                         trControl=train_control,
                         tuneLength=10)
  cv_svm
}

svm_5_fold_poly <- function(dataset, class){
  dataset <- dataset |> dplyr::mutate(class=class)
  train_control <- caret::trainControl(method = "repeatedcv",
                                       number = 5,
                                       repeats = 1) 
  
  cv_svm <- caret::train(class~., data=dataset,
                         method="svmPoly",
                         trControl=train_control,
                         tuneLength=5)
  cv_svm
}

