log_file = open("um-server-01.txt") # open a file 


def sales_reports(log_file): # define a function to create a sales report in the file
    for line in log_file: # loop through each line of the file 
        line = line.rstrip() # remove trailing characters, spaces at the end 
        day = line[0:3] # get first three characters of the line and assign it to the variable day  
        if day == "Mon": # check if the day is Monday 
            print(line) # then print the result


sales_reports(log_file) # call the sales reports function and pass in the log file as an argument 
