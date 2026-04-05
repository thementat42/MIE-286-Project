library(jsonlite)

# all data was stored in the data/ subdirectory
DATA_PATH <- "data"

# For a given feedback type, we want to extract all the baseline results (with no feedback)
# and the actual results (with feedback)
# splitting by feedback type makes it easier to place things in an array
get_data <- function(feedback_type) {
  # data was split in to gain_data and loss_data, so load from the appropriate one
  path <- file.path(DATA_PATH, paste0(feedback_type, "_data"))
  # get all files in the directory
  files <- list.files(path)
  # for debugging to ensure we got all of them
  print(files)
  
  # to store the processout output
  results <- list()
  
  for (file in files) {
    # if for some reason a file is incorrectly named, skip it (e.g., old testing files)
    if (!grepl(feedback_type, file)) {
      next
    }
    
    # get the name of the participant
    name <- strsplit(file, "_")[[1]][1]
    # get their baseline file
    baseline_file <- paste0(name, "_baseline.json")
    
    # load data as a dataframe from the json files
    feedback_data <- fromJSON(file.path(path, file))
    baseline_data <- fromJSON(file.path(path, baseline_file))
    
    # append it to the array (by inserting at the current length + 1)
    results[[length(results) + 1]] <- list(
      baseline = baseline_data,
      feedback = feedback_data
    )
  }
  
  # output the array, where each entry is the baseline + feedback data for a given participant
  return(results)
}

process <- function(feedback_type) {
  # get the data
  data <- get_data(feedback_type)
  
  # arrays to store the scores
  baseline_scores <- c()
  baseline_times <- c()
  feedback_scores <- c()
  feedback_times <- c()
  
  for (participant in data) {
    # load the individual data from the dataframes
    baseline <- participant$baseline
    feedback <- participant$feedback
    
    # compute the mean score and time taken in the baseline case
    baseline_score <- mean((baseline$correct))
    baseline_time <- mean((baseline$time_taken))
    
    # repeat for the feedback case
    feedback_score <- mean((feedback$correct))
    feedback_time <- mean((feedback$time_taken))
    
    # add these to the array
    baseline_scores <- c(baseline_scores, baseline_score)
    baseline_times <- c(baseline_times, baseline_time)
    feedback_scores <- c(feedback_scores, feedback_score)
    feedback_times <- c(feedback_times, feedback_time)
  }
  
  # output the data
  return(list(
    baseline_scores = baseline_scores,
    baseline_times = baseline_times,
    feedback_scores = feedback_scores,
    feedback_times = feedback_times
  ))
}

write_file <- function(filename) {
  # the main file that processes our raw data into a new JSON file (which can then be read by the analysis R code)
  gain <- process("gain")  # get gain data
  loss <- process("loss")  # get loss data
  
  # now we're just rearranging the arrays and mapping them to useful keys
  # this way in the analysis R code, we can import this as a dataframe and have access to arrays of relevant data
  # for example, doing data$gain_baseline_accuracy will give us a list of all baseline accuracies (on a scale from 0 to 1)
  # which we could then, say, plot on a QQ-norm plot
  result <- list(
    gain_baseline_accuracy = gain$baseline_scores,
    gain_baseline_response_time = gain$baseline_times,
    gain_feedback_accuracy = gain$feedback_scores,
    gain_feedback_response_time = gain$feedback_times,
    
    loss_baseline_accuracy = loss$baseline_scores,
    loss_baseline_response_time = loss$baseline_times,
    loss_feedback_accuracy = loss$feedback_scores,
    loss_feedback_response_time = loss$feedback_times
  )
  
  # write the data to a file
  # pretty = TRUE makes it more human readable (adding line breaks, etc. instead of one long string)
  # this doesn't affect the data in any way (R doesn't care, it can read the JSON file regardless of formatting)
  # but it makes it easier for us to check
  write_json(result, filename, pretty = TRUE, auto_unbox = TRUE)
}

# call the function to actually do the analysis
write_file("averaged_data.json")

