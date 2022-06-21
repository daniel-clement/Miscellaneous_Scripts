# this script was written by Daniel Clement - 2022
"""
This script provides a function which will print the processing time of a script, by using Pythons time module.
This can be included in other scripts, by using this python file as a template and pasting your code into the area
below line 12 and above line 22.
"""

# import time module from python main library
import time

# Start time measurement -- <<<Goes at the beginning of the script>>>
startTime = time.time()


########################################################
########################################################
# Script's Code Goes HERE ##############################
########################################################
########################################################


# calculate time it took script to run in seconds -- <<<Goes at the end of the script>>>
executionTimeSec = (time.time() - startTime)


# define function to determine how long the script took to run, and generate the required print statement
def print_execution_time(executionTimeSec):
    if executionTimeSec < 60:
        execTimeSecRound = round(executionTimeSec, 2)
        print("Process completed in {} seconds".format(execTimeSecRound))
    elif 60 <= executionTimeSec < 3600:
        execTimeMin = executionTimeSec / 60
        execTimeMinRound = round(execTimeMin, 2)
        print("Process completed in {} minutes".format(execTimeMinRound))
    elif 3600 <= executionTimeSec < 86400:
        execTimeHours = executionTimeSec / 3600
        execTimeHoursRound = round(execTimeHours, 2)
        print("Process completed in {} hours".format(execTimeHoursRound))
    elif executionTimeSec >= 86400:
        execTimeDays = executionTimeSec / 86400
        execTimeDaysRound = round(execTimeDays, 2)
        print("Process completed in {} days".format(execTimeDaysRound))


# call the print_execution_time function to print the time it took the script to run
print_execution_time(executionTimeSec)
