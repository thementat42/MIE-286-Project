install.packages("rjson")
library("rjson")
install.packages("car")
library(car)

# Loading data from the JSON file
averaged_data <- fromJSON(file = "averaged_data.json")

attach(averaged_data)

# Defining relative scores
relative_gain_feedback_accuracy = gain_feedback_accuracy - gain_baseline_accuracy
relative_gain_feedback_response_time = gain_feedback_response_time - gain_baseline_response_time
relative_loss_feedback_accuracy = loss_feedback_accuracy - loss_baseline_accuracy
relative_loss_feedback_response_time = loss_feedback_response_time - loss_baseline_response_time

# Q-Q plots

## Baselines
qqPlot(gain_baseline_accuracy, distribution = "norm", 
       main = "Baseline Accuracy (Gain-Based Feedback Participants)",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(gain_baseline_response_time, distribution = "norm", 
       main = "Baseline Response Time (Gain-Based Feedback Participants)",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(loss_baseline_accuracy, distribution = "norm", 
       main = "Baseline Accuracy (Loss-Based Feedback Participants)",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(loss_baseline_response_time, distribution = "norm", 
       main = "Baseline Response Time (Loss-Based Feedback Participants)",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))

## GAIN
qqPlot(gain_feedback_accuracy, distribution = "norm", 
       main = "Accuracy for Gain-Based Feedback Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(gain_feedback_response_time, distribution = "norm", 
       main = "Response Time for Gain-Based Feedback Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))

qqPlot(relative_gain_feedback_accuracy, distribution = "norm", 
       main = "Relative Accuracy for Gain-Based Feedback Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(relative_gain_feedback_response_time, distribution = "norm", 
       main = "Relative Response Time for Gain-Based Feedback Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))

## LOSS
qqPlot(loss_feedback_accuracy, distribution = "norm", 
       main = "Accuracy for Loss-Based Feedback Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(loss_feedback_response_time, distribution = "norm", 
       main = "Response Time for Loss-Based Feedback Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(relative_loss_feedback_accuracy, distribution = "norm", 
       main = "Relative Accuracy for Loss-Based Feedback Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))
qqPlot(relative_loss_feedback_response_time, distribution = "norm", 
       main = "Relative Response Time for Loss-Based Feedback Normal Q-Q Plot",
       ylab = "sample quantiles",
       envelope=0.95,
       line = c("robust"))

# One-sided t-tests

## Loss vs. baseline
t.test(loss_feedback_accuracy, loss_baseline_accuracy,
       alternative = c("greater"), paired=TRUE)
t.test(loss_feedback_response_time, loss_baseline_response_time,
       alternative = c("greater"), paired=TRUE)

## Gain vs. baseline
t.test(gain_feedback_accuracy, gain_baseline_accuracy,
       alternative = c("greater"), paired=TRUE)
t.test(gain_feedback_response_time, gain_baseline_response_time,
       alternative = c("greater"), paired=TRUE)

## Loss vs. Gain
t.test(loss_feedback_accuracy, gain_feedback_accuracy[1:14], 
       alternative = c("greater"), paired=FALSE)
t.test(relative_loss_feedback_accuracy, relative_gain_feedback_accuracy[1:14], 
       alternative = c("greater"), paired=FALSE)
t.test(loss_feedback_response_time, gain_feedback_response_time[1:14], 
       alternative = c("greater"), paired=FALSE)
t.test(relative_loss_feedback_response_time, relative_gain_feedback_response_time[1:14], 
       alternative = c("greater"), paired=FALSE)

# Two-sided t-tests

## Loss vs. baseline
t.test(loss_feedback_accuracy, loss_baseline_accuracy,
       alternative = c("two.sided"), paired=TRUE)
t.test(loss_feedback_response_time, loss_baseline_response_time,
       alternative = c("two.sided"), paired=TRUE)

## Gain vs. baseline
t.test(gain_feedback_accuracy, gain_baseline_accuracy,
       alternative = c("two.sided"), paired=TRUE)
t.test(gain_feedback_response_time, gain_baseline_response_time,
       alternative = c("two.sided"), paired=TRUE)

## Loss vs. Gain
t.test(loss_feedback_accuracy, gain_feedback_accuracy[1:14], 
       alternative = c("two.sided"), paired=FALSE)
t.test(relative_loss_feedback_accuracy, relative_gain_feedback_accuracy[1:14], 
       alternative = c("two.sided"), paired=FALSE)
t.test(loss_feedback_response_time, gain_feedback_response_time[1:14], 
       alternative = c("two.sided"), paired=FALSE)
t.test(relative_loss_feedback_response_time, relative_gain_feedback_response_time[1:14], 
       alternative = c("two.sided"), paired=FALSE)

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


# Box Plots 

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