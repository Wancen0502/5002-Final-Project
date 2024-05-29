import numpy as np
import matplotlib as plt
import time


class BasicHealthStatementrecording:

    def __init__(self):
        self.User_day = None
        self.User_Gender = "unknown"
        self.User_age = 0
        self.User_CWeight = 0
        self.User_GWeight = 0

        self.User_CHeight = 0
        
        # lists for recording data over time
        self.User_CWeight_Rl = []
        self.User_BMI_Rl = []
        self.User_CWeight_Timel = []
        self.User_time = []
        
        # BMI related variables
        self.BMI = 0
        self.BMIresult = None
        
# record BMI values over time
    def RecordCBMIStatement(self):
        self.User_BMI_Rl.append(self.BMI)
        return self.User_BMI_Rl

# plot weight over time
    def WeightTendency(self):
        plt.ylabel("time") #naming the chart
        plt.xlabel("Weight(Kg)")

        for i in self.User_CWeight_Rl1:
            xpoints = np.array(i)
            ypoints = np.array(self.User_time[self.User_CWeight_Rl1.index(i)])
            plt.plot(xpoints, ypoints)
        return plt.show()

    def BMITendency(self):
        plt.ylabel("time") #naming the chart 
        plt.xlabel("BMI")

        for i in self.User_BMI_Rl:
            xpoints = np.array(i)
            ypoints = np.array(self.User_BMI_Rl(i))
            plt.plot(xpoints, ypoints)
        return plt.show()

# calculate BMI based on user's weight and height
def CalculateBMI(self):
    self.BMI = self.User_CWeight / self.User_CHeight ** 2
    return round(self.BMI, 2)

# evaluate BMI and provide a result
def BMIevaluate(self):
    if self.BMI < 18.5:
        BMIresult = "underweight"

    elif 18.5 <= self.BMI < 24:
        BMIresult = "you are stay in health weight"

    elif 24 <= self.BMI < 27:
        BMIresult = "overweight"

    elif self.BMI >= 27:
        BMIresult = "fat"

    return BMIresult

# collect basic information about the user
def User_Basic(self):
    isTrue = True
    print("your gender is: M/F")
    userinput = input() #user input gender
    if userinput != 'M' and userinput != 'F': # validate user input
        isTrue = False
    while not isTrue:  
        print("Does not meet the requirement, Please re Enter.")
        userinput = input()
        if userinput == 'M' or userinput == 'F':
            isTrue = True
    self.User_Gender = userinput

    print("How old are you:")
    userinput = input() #user input age
    if not userinput.isdigit(): # validate user input
        isTrue = False
    while not isTrue: 
        print("not a number, Please re Enter.")
        userinput = input()
        if userinput.isdigit():
            isTrue = True
    self.User_age = eval(userinput)

    print("your current height is:(m)")
    userinput = input() # user input cureent height 
    if not userinput.replace(".", "").isnumeric(): # validate user input
        isTrue = False
    while not isTrue: # continue prompting until valid input is received
        print("not a number, Please re Enter.")
        userinput = input()
        if userinput.replace(".", "").isnumeric():
            isTrue = True
    self.User_CHeight = eval(userinput)

    print("your current weight is:(Kg)")
    userinput = input() # user input current weight  
    if not userinput.replace(".", "").isnumeric(): # validate user input
        isTrue = False
    while not isTrue: # continue prompting until valid input is received
        print("not a number, Please re Enter.")
        userinput = input()
        if userinput.replace(".", "").isnumeric():
            isTrue = True
    self.User_CWeight = eval(userinput)

    print("your goal weight is: (Kg)")
    userinput = input() # user input goal weight 
    if not userinput.replace(".", "").isnumeric(): # validate user input
        isTrue = False
    while not isTrue: # continue prompting until valid input is received
        print("not a number, Please re Enter.")
        userinput = input()
        if userinput.replace(".", "").isnumeric():
            isTrue = True
    self.User_GWeight = eval(userinput)

    print("how many days do you want to take to achieve your goal：")
    userinput = input() #user input goal day 
    if not userinput.isdigit(): # validate user input
        isTrue = False
    while not isTrue: # continue prompting until valid input is received
        print("not a number, Please re Enter.")
        userinput = input()
        if userinput.isdigit(): 
            isTrue = True
    self.User_day = userinput 

# return user information
def getInformation(self):
    return self.User_age, self.User_Gender, self.User_CHeight, self.User_CWeight, self.User_GWeight, self.User_day

# change user gender
def ChangeGender(self):
    self.User_CHeight = str(input())
    return self.User_Gender

 # record current weight over time
def RecordCWeightStatement(self):
    self.User_CWeight_Rl1.append(self.User_CWeight)
    return self.User_CWeight_Rl1

# record current weight over time
def updateCurrentCweight(self, c):
    self.User_CWeight = c

# update current weight
def ClearCWeightStatement(self):
    self.User_CWeight_Rl1.clear()
    return self.User_CWeight_Rl1

# clear recorded current weight statements
def ClearGWeightStatement(self):
    self.User_GWeight = 0

# update goal weight statement
def UpdateGWeightStatement(self):
    self.User_GWeight = eval(input())

# Get current time and append to time list
def GetTime(self):
    input_time = time.ctime()
    self.User_time.append(input_time)
    return self.User_time
