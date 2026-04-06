install.packages("rjson")
library("rjson")
install.packages("car")
library(car)

averaged_data <- fromJSON(file = "averaged_data.json")
# print(averaged_data)

attach(averaged_data)

# Defining relative scores
relative_gain_feedback_accuracy = gain_feedback_accuracy - gain_baseline_accuracy
relative_gain_feedback_response_time = gain_feedback_response_time - gain_baseline_response_time
relative_loss_feedback_accuracy = loss_feedback_accuracy - loss_baseline_accuracy
relative_loss_feedback_response_time = loss_feedback_response_time - loss_baseline_response_time

# Q-Q plots

## Baselines
qqPlot(gain_baseline_accuracy, distribution = "norm", 
       main = "Baseline Accuracy Normal Q-Q Plot (Gain-Based Feedback Participants)",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(gain_baseline_response_time, distribution = "norm", 
       main = "Baseline Response Time Normal Q-Q Plot (Gain-Based Feedback Participants)",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(loss_baseline_accuracy, distribution = "norm", 
       main = "Baseline Accuracy Normal Q-Q Plot (Loss-Based Feedback Participants)",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(loss_baseline_response_time, distribution = "norm", 
       main = "Baseline Response Time Normal Q-Q Plot (Loss-Based Feedback Participants)",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))

## GAIN
qqPlot(gain_feedback_accuracy, distribution = "norm", 
       main = "Gain-Based Feedback Accuracy Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(gain_feedback_response_time, distribution = "norm", 
       main = "Gain-Based Feedback Response Time Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))

## LOSS
qqPlot(loss_feedback_accuracy, distribution = "norm", 
       main = "Loss-Based Feedback Accuracy Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(loss_feedback_response_time, distribution = "norm", 
       main = "Loss-Based Feedback Response Time Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))


# qqnorm(gain_feedback_accuracy, main = "Gain-Based Feedback Accuracy Normal Q-Q Plot")
# qqnorm(gain_feedback_response_time, main = "Gain-Based Feedback Response Time Normal Q-Q Plot")
# qqnorm(loss_feedback_accuracy, main = "Loss-Based Feedback Accuracy Normal Q-Q Plot")
# qqnorm(loss_feedback_response_time, main = "Loss-Based Feedback Response Time Normal Q-Q Plot")
# qqnorm(relative_gain_feedback_accuracy, main = "Relative Gain-Based Feedback Accuracy Normal Q-Q Plot")
# qqnorm(relative_gain_feedback_response_time, main = "Relative Gain-Based Feedback Response Time Normal Q-Q Plot")
# qqnorm(relative_loss_feedback_accuracy, main = "Relative Loss-Based Feedback Accuracy Normal Q-Q Plot")
# qqnorm(relative_loss_feedback_response_time, main = "Relative Loss-Based Feedback Response Time Normal Q-Q Plot")

# One-sided t-tests

## Loss vs. baseline

## Gain vs. baseline

## Loss vs. Gain
t.test(gain_feedback_accuracy[1:14], loss_feedback_accuracy, paired=T)
t.test(relative_gain_feedback_accuracy[1:14], relative_loss_feedback_accuracy, paired=T)
t.test(gain_feedback_response_time[1:14], loss_feedback_response_time, paired=T)
t.test(relative_gain_feedback_response_time[1:14], relative_loss_feedback_response_time, paired=T)

# Two-sided t-tests
t.test(gain_feedback_accuracy[1:14], loss_feedback_accuracy, paired=FALSE)
t.test(relative_gain_feedback_accuracy[1:14], relative_loss_feedback_accuracy, paired=FALSE)
t.test(gain_feedback_response_time[1:14], loss_feedback_response_time, paired=FALSE)
t.test(relative_gain_feedback_response_time[1:14], relative_loss_feedback_response_time, paired=FALSE)

# Histograms
## GAIN
hist(gain_baseline_accuracy, 
     main = paste("Accuracy for Baseline Trials (Gain-Based Feedback Participants)"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)
hist(gain_feedback_accuracy, 
     main = paste("Accuracy for Gain-Based Feedback Trials"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)
hist(gain_baseline_response_time, 
     main = paste("Response Time for Baseline Trials (Gain-Based Feedback Participants)"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)
hist(gain_feedback_response_time, 
     main = paste("Response Time for Gain-Based Feedback Trials"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)

hist(relative_gain_feedback_accuracy, 
     main = paste("Relative Accuracy for Gain-Based Feedback Trials"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)
hist(relative_gain_feedback_response_time, 
     main = paste("Relative Response Time for Gain-Based Feedback Trials"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)

## LOSS
hist(loss_baseline_accuracy, 
     main = paste("Accuracy for Baseline Trials (Loss-Based Feedback Participants)"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)
hist(loss_feedback_accuracy, 
     main = paste("Accuracy for Loss-Based Feedback Trials"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)
hist(loss_baseline_response_time, 
     main = paste("Response Time for Baseline Trials (Loss-Based Feedback Participants)"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)
hist(loss_feedback_response_time, 
     main = paste("Response Time for Loss-Based Feedback Trials"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)

hist(relative_loss_feedback_accuracy, 
     main = paste("Relative Accuracy for Loss-Based Feedback Trials"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)
hist(relative_loss_feedback_response_time, 
     main = paste("Relative Response Time for Loss-Based Feedback Trials"),
     xlab =  "Accuracy", axes = TRUE, plot = TRUE)


par(mfrow = c(1, 2)) 
 
boxplot(gain_feedback_accuracy, loss_feedback_accuracy,
        names = c("Gain", "Loss"),
        main = "Accuracy by Feedback Type (Absolute)",
        ylab = "Accuracy",
        col = c("lightblue", "lightcoral"))

stripchart(list(gain_feedback_accuracy, loss_feedback_accuracy),
           method = "jitter",
           pch = 16,
           col = rgb(0, 0, 0, 0.5),
           vertical = TRUE,
           add = TRUE)

boxplot(gain_feedback_response_time, loss_feedback_response_time,
        names = c("Gain", "Loss"),
        main = "Response Time by Feedback Type (Absolute)",
        ylab = "Response Time (ms)",
        col = c("lightblue", "lightcoral"))

stripchart(list(gain_feedback_response_time, loss_feedback_response_time),
           method = "jitter",
           pch = 16,
           col = rgb(0, 0, 0, 0.5),
           vertical = TRUE,
           add = TRUE)

par(mfrow = c(1, 2)) 

boxplot(relative_gain_feedback_accuracy, relative_loss_feedback_accuracy,
        names = c("Gain", "Loss"),
        main = "Accuracy by Feedback Type (Relative to Basline)",
        ylab = "Accuracy",
        col = c("lightblue", "lightcoral"))

stripchart(list(relative_gain_feedback_accuracy, relative_loss_feedback_accuracy),
           method = "jitter",
           pch = 16,
           col = rgb(0, 0, 0, 0.5),
           vertical = TRUE,
           add = TRUE)

boxplot(relative_gain_feedback_response_time, relative_loss_feedback_response_time,
        names = c("Gain", "Loss"),
        main = "Response Time by Feedback Type (Relative to Basline)",
        ylab = "Response Time (ms)",
        col = c("lightblue", "lightcoral"))

stripchart(list(relative_gain_feedback_response_time, relative_loss_feedback_response_time),
           method = "jitter",
           pch = 16,
           col = rgb(0, 0, 0, 0.5),
           vertical = TRUE,
           add = TRUE)