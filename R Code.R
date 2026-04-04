install.packages("rjson")
library("rjson")

averaged_data <- fromJSON(file = "C:\\Users\\surhi\\OneDrive\\Documents\\U of T 2025-2026\\Winter\\MIE286\\MIE-286-Project\\averaged_data.json")
# print(averaged_data)

attach(averaged_data)
qqnorm(gain_feedback_accuracy, main = "Gain-Based Feedback Accuracy Normal Q-Q Plot")
qqnorm(gain_feedback_response_time, main = "Gain-Based Feedback Response Time Normal Q-Q Plot")
qqnorm(loss_feedback_accuracy, main = "Loss-Based Feedback Accuracy Normal Q-Q Plot")
qqnorm(loss_feedback_response_time, main = "Loss-Based Feedback Response Time Normal Q-Q Plot")

relative_gain_feedback_accuracy = gain_feedback_accuracy - gain_baseline_accuracy
relative_gain_feedback_response_time = gain_feedback_response_time - gain_baseline_response_time
relative_loss_feedback_accuracy = loss_feedback_accuracy - loss_baseline_accuracy
relative_loss_feedback_response_time = loss_feedback_response_time - loss_baseline_response_time

qqnorm(relative_gain_feedback_accuracy, main = "Relative Gain-Based Feedback Accuracy Normal Q-Q Plot")
qqnorm(relative_gain_feedback_response_time, main = "Relative Gain-Based Feedback Response Time Normal Q-Q Plot")
qqnorm(relative_loss_feedback_accuracy, main = "Relative Loss-Based Feedback Accuracy Normal Q-Q Plot")
qqnorm(relative_loss_feedback_response_time, main = "Relative Loss-Based Feedback Response Time Normal Q-Q Plot")

t.test(gain_feedback_accuracy[1:14], loss_feedback_accuracy, paired=T)
t.test(relative_gain_feedback_accuracy, relative_loss_feedback_accuracy, paired=T)
t.test(gain_feedback_response_time, loss_feedback_response_time, paired=T)
t.test(relative_gain_feedback_response_time, relative_loss_feedback_response_time, paired=T)
  
