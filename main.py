# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import User
import Init
import pandas as pd
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    # Read food information from a CSV file
    foodInfo = pd.read_csv("FoodCalories.csv")
    # Initialize username and login status
    username, isLogIn = Init.init()
    userInput = None
    
    # While loop to continue execution until the user enters "Quit"
    while userInput != "Quit":
        # Execute the user basic information and user operation in the login state
        while isLogIn:
            User.userBasic(username)
            User.userOperation(username)
            # Set login status to False to exit the loop
            isLogIn = False
    
    # Prompt the user to quit or continue    
    userInput = input("To quit health management, enter 'Quit', else, enter anything to continue: ")
    # Reinitialize the username and login status
    username, isLogIn = Init.init()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

