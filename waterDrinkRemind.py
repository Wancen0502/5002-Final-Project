#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:28:15 2023

@author: wancenyang
"""
import time 


# setting reminding message, based on how many cups of water left
def drinkWater(cupsLeft):
    if cupsLeft == 1: # check if there is only 1 cup left
        message ="It is time to drink last cup of water，you almost done!"
    elif cupsLeft == 2:  # Check if there are 2 cups left
        message = "It is time to drink water, and you still need to drink " +str(cupsLeft-1) +" cup of water."      
    else: # For all other cases (more than 2 cups left)
        message = "It is time to drink water, and you still need to drink " +str(cupsLeft-1) +" cups of water."
    print(message)

# users set relative information to their own water drinking reminder system.     
def getUserInput():
    startTime = input( "please enter start time:（HH:MM）:") # prompt the user to enter the start time in the format HH:MM 
    endTime = input( "please enter end time (HH:MM）:")# prompt the user to enter the end time in the format HH:MM 
    totalCups = int(input("How many cups of water do you want to drink during the period? ")) # Prompt the user to enter the total number of cups of water to drink during the period
    
    return startTime,endTime,totalCups 



def remindCount():
    
   
    startTime, endTime, totalCups = getUserInput()  # get user input for start time, end time, and total cups
    
    # convert start and end times to time.struct_time objects
    startTimeStruct = time.strptime(startTime, "%H:%M")
    endTimeStruct = time.strptime(endTime, "%H:%M")

    # calculate the time difference between end and start times
    timeDifference = time.mktime(endTimeStruct) - time.mktime(startTimeStruct)

    # calculate the time interval between each reminder
    interval = timeDifference / totalCups

    cupsLeft = (totalCups) # initialize cups left to the total number of cups
    
    
    while cupsLeft > 0: # loop through the remaining cups and remind the user
        time.sleep(interval) # pause execution for the calculated interval
        drinkWater(cupsLeft) # call the drinkWater function to remind the user
        cupsLeft = cupsLeft-1  # Decrement the cupsLeft counter
    
        
    


        
    
    
    
    
    
    
