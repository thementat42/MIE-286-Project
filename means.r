install.packages("rjson")
library(rjson)

data <- fromJSON(file = "averaged_data.json")

for (key in names(data)) {
  xbar <- mean(data[[key]])
  S <- sd(data[[key]])
  
  cat(sprintf("%s: xbar = %.4f, S = %.4f\n", key, xbar, S))
}
