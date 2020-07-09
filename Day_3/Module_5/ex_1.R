library(glue)
current_time <- format(Sys.time(), "%X")

# with glue paste0
print(paste0("Current time is ", current_time))

# with glue lib
glue("Current time is: {current_time}")

# with message
message("Current time is ", current_time)