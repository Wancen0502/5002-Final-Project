import pandas as pd

import User


# Function to change user's height
def changeHeight():
    isTrue = True
    userinput = input("Please enter the height you want to change to: ")
    # Validate if input is numeric
    if not userinput.replace(".", "").isnumeric():
        isTrue = False
    # Loop to ensure valid input
    while not isTrue:
        print("not a number, Please re Enter.")
        userinput = input()
        if userinput.replace(".", "").isnumeric():
            isTrue = True
    return eval(userinput)


# Function to change user's gender
def changeGender():
    isTrue = True
    userinput = input("Please enter the gender you want to change to: ")
    # Validate if input is 'M' or 'F'
    if userinput != 'M' and userinput != 'F':
        isTrue = False
    # Loop to ensure valid input
    while not isTrue:
        print("Does not meet the requirement, Please re Enter.")
        userinput = input()
        if userinput == 'M' or userinput == 'F':
            isTrue = True
    return userinput


# Function to change user's age
def changeAge():
    isTrue = True
    userinput = input("Please enter the age you want to change to: ")
    if not userinput.isdigit():
        isTrue = False
    # Loop to ensure valid input
    while not isTrue:
        print("not a number, Please re Enter.")
        userinput = input()
        if userinput.isdigit():
            isTrue = True
    return eval(userinput)


# Function to change user's goal weight
def changeGweight():
    isTrue = True
    userinput = input("Please enter the goal you want to change to: ")
    if not userinput.replace(".", "").isnumeric():
        isTrue = False
    while not isTrue:
        print("not a number, Please re Enter.")
        userinput = input()
        if userinput.replace(".", "").isnumeric():
            isTrue = True
    return eval(userinput)


# Function to calculate BMI
def CalculateBMI(User_CWeight, User_CHeight):
    BMI = User_CWeight / User_CHeight ** 2
    return round(BMI, 2)

# Function to evaluate BMI and return result
def BMIevaluate(BMI):
    if BMI < 18.5:
        BMIresult = "underweight"

    elif 18.5 <= BMI < 24:
        BMIresult = "you are stay in health weight"

    elif 24 <= BMI < 27:
        BMIresult = "overweight"

    elif BMI >= 27:
        BMIresult = "fat"

    return BMIresult


# Function to change user's selected day
def changeDay():
    isTrue = True
    userinput = input("Please enter the day you want to change to: ")
    if not userinput.isdigit():
        isTrue = False
    # Loop to ensure valid input
    while not isTrue:
        print("not a number, Please re Enter.")
        userinput = input()
        if userinput.isdigit():
            isTrue = True
    return eval(userinput)


# Function to change user's current weight
def changeCweight():
    isTrue = True
    userinput = input("Please enter the Current Weight you want to change to: ")
    if not userinput.replace(".", "").isnumeric():
        isTrue = False
    # Loop to ensure valid input
    while not isTrue:
        print("not a number, Please re Enter.")
        userinput = input()
        if userinput.replace(".", "").isnumeric():
            isTrue = True
    return eval(userinput)


# Function to change user data based on input
def changeData(username):
    data = pd.read_csv("UserInfo.csv")
    isTrue = True
    usernameList = data['Username'].tolist()
    userIndex = usernameList.index(username)
    # Display options to the user
    print("Please choose the following:")
    print("Enter 1 to change gender")
    print("Enter 2 to change age")
    print("Enter 3 to change height")
    print("Enter 4 to change current weight")
    print("Enter 5 to change goal weight")
    print("Enter 6 to change day")
    print("Enter 7 to display Updated info")
    print("Enter 8 to exit")
    print("Enter 9 for instructions")
    userinput = input("Please enter a number: ")
    # Validate if input is numeric
    if not userinput.isdigit():
        isTrue = False
    # Loop to ensure valid input
    while not isTrue:
        print("not a number, Please re Enter.")
        userinput = input("Please enter a number: ")
        if userinput.isdigit():
            isTrue = True
    # Loop for user interaction
    while int(userinput) != 8:
        # Change user's gender
        if int(userinput) == 1:
            data = pd.read_csv("UserInfo.csv")
            data.loc[userIndex, 'Gender'] = changeGender()
            data.to_csv("UserInfo.csv", index=False)
        # Change user's age
        elif int(userinput) == 2:
            data = pd.read_csv("UserInfo.csv")
            data.loc[userIndex, 'Age'] = changeAge()
            data.to_csv("UserInfo.csv", index=False)
        # Change user's height
        elif int(userinput) == 3:
            data = pd.read_csv("UserInfo.csv")
            data.loc[userIndex, 'Height'] = changeHeight()
            data.to_csv("UserInfo.csv", index=False)
        # Change user's current weight
        elif int(userinput) == 4:
            data = pd.read_csv("UserInfo.csv")
            data.loc[userIndex, 'CurrentWeight'] = changeCweight()
            data.to_csv("UserInfo.csv", index=False)
            data = pd.read_csv("UserInfo.csv")
            BMI = CalculateBMI(data.loc[userIndex, 'CurrentWeight'], data.loc[userIndex, 'Height'])
            print(data.loc[userIndex, 'CurrentWeight'])
            print(data.loc[userIndex, 'Height'])
            result = BMIevaluate(BMI)
            data.loc[userIndex, 'BMI'] = BMI
            data.loc[userIndex, 'BMI Result'] = result
            data.to_csv("UserInfo.csv", index=False)
        # Change user's goal weight
        elif int(userinput) == 5:
            data = pd.read_csv("UserInfo.csv")
            data.loc[userIndex, 'Goal'] = changeGweight()
            data.to_csv("UserInfo.csv", index=False)
        # Change user's selected day
        elif int(userinput) == 6:
            data = pd.read_csv("UserInfo.csv")
            data.loc[userIndex, 'Day'] = changeDay()
            data.to_csv("UserInfo.csv", index=False)
        # Display updated user information
        elif int(userinput) == 7:
            User.userInfo(username)
        # Display instructions
        elif int(userinput) == 9:
            print("Enter 1 to change gender")
            print("Enter 2 to change age")
            print("Enter 3 to change height")
            print("Enter 4 to change current weight")
            print("Enter 5 to change goal weight")
            print("Enter 6 to change day")
            print("Enter 7 to display Updated info")
            print("Enter 8 to exit")
            print("Enter 9 for instructions")
        # Handle invalid input
        else:
            print("Invalid number, please try again, or press 9 for instructions")
            print("Enter 1 to change gender")
            print("Enter 2 to change age")
            print("Enter 3 to change height")
            print("Enter 4 to change current weight")
            print("Enter 5 to change goal weight")
            print("Enter 6 to change day")
            print("Enter 7 to display Updated info")
            print("Enter 8 to exit")
            print("Enter 9 for instructions")
        userinput = input("Please enter a number: ")
        # Validate if input is numeric
        if not userinput.isdigit():
            isTrue = False
        # Loop to ensure valid input
        while not isTrue:
            print("not a number, Please re Enter. Or press number 9 for instructions")
            userinput = input("Please enter a number: ")
            if userinput.isdigit():
                isTrue = True
