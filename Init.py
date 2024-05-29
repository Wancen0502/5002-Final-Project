import LogIn
import CreateAccount



def init():
    # Initializing variables
    isLogIn = False
    isTrue = True
    username = None
    print("Welcome to health management")
    print("Please choose the following:")
    print("Enter 1 to login")
    print("Enter 2 to create Account")
    print("Enter 3 to exit")
    # Getting user input
    userinput = input("Please enter a number: ")
    
    # Validating if the input is a digit
    if not userinput.isdigit():
        isTrue = False
        
    # Loop to ensure valid input
    while not isTrue:
        print("not a number, Please re Enter. Or press number 9 for instructions")
        userinput = input("Please enter a number: ")
        if userinput.isdigit():
            isTrue = True
            
    # Main loop for user interaction
    while int(userinput) != 3:
        if int(userinput) == 1:
            # Calling the LogIn module to perform login
            username, isLogIn = LogIn.testLogIn()
            if isLogIn:
                return username, isLogIn
        elif int(userinput) == 2:
            
            # Calling the CreateAccount module to create a new account
            CreateAccount.createUsername()
        elif int(userinput) == 9:
            print("Enter 1 to login")
            print("Enter 2 to create Account")
            print("Enter 3 to exit")
            # Handling invalid input
        else:
            print("Invalid number, please try again")
            print("Please choose the following:")
            print("Enter 1 to login")
            print("Enter 2 to create Account")
            print("Enter 3 to exit")
        # Getting user input for the next iteration
        userinput = input("Please enter a number: ")
        if not userinput.isdigit():
            isTrue = False
        while not isTrue:
            print("not a number, Please re Enter. Or press number 9 for instructions")
            userinput = input("Please enter a number: ")
            if userinput.isdigit():
                isTrue = True
    return username, isLogIn
