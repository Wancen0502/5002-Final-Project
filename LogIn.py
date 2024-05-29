import pandas as pd


def testLogIn():
    isLogin = False
    # Read user account data from CSV file
    data = pd.read_csv("Account.csv")
    username_input = input("Please enter your username: ")
    password_input = input("Please enter your password: ")
    
    # Extract the Username column and Password column from data and convert them to list
    usernameList = data['Username'].tolist()
    passwordList = data['Password'].tolist()
    
    # Check if the entered username and password match any account in the data
    if username_input in usernameList and password_input in passwordList:
        # Check if the index of the entered username match the index of the entered password
        if usernameList.index(username_input) == passwordList.index(password_input):
            print("Logged in successfully!")
            isLogin = True # update the isLogin variable to True
    
    else:
        print("User name or password is wrong, please re-enter!")
    
    return username_input, isLogin


