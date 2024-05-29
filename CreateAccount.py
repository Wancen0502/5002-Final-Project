import pandas as pd


# Function to create a new username in the system
def createUsername():
    data = pd.read_csv("Account.csv")
    username = input("Please enter your username: ")
    # Convert the 'Username' column to a list for easier checking
    usernameList = data['Username'].tolist()
    
    # Check if the entered username already exists
    if username in usernameList:
        print("Username already exists, please re-enter!")
    
    else:
        data.loc[len(data)] = username
        password = input("Please enter your password: ")
        data['Password'][data.Username == username] = password
        print("Registration Successful!")
        # Save the data to the CSV file without the index
        data.to_csv("Account.csv", index=False)
    
    return data
