import pandas as pd



# function to handle cases where the entered food might not be in the database
# asks the user if they want to add the food to the database
def noFoodResult(foodInput):
    isTrue = True
    userInput = input("The food you entered might be out of range, do you want to add it to the database? yes/no: ")
    if userInput.lower() != "yes" and userInput.lower() != "no": # validate user input
        isTrue = False
    while not isTrue: # continue prompting until valid input is received
        print("Invalid, please re Enter") 
        userInput = input("Please enter yes/no: ")
        if userInput.lower() != "yes" or userInput.lower() != "no": # corrected the condition to "and"
            isTrue = True
    if userInput == 'yes': # Process user decision
        addFood(foodInput.capitalize())
    else:  # If user chooses not to add, it would prompt the function of foodfind and start new enquiry
        foodInput = findFood()
    return foodInput 


# function to add a new food to the database if it doesn't already exist
def addFood(foodInput):
    isTrue = True
    food = pd.read_csv("FoodCalories.csv") #read the data base
    foodName = food["Food"].tolist() 
    if foodInput not in foodName:  # check if the food input by the user is in the “foodname” in the database
        nFoodCal = input("Please enter the food calories per 100g: ")
        if not nFoodCal.replace(".", "").isnumeric():
            isTrue = False
        while not isTrue:
            print("not a number, Please re Enter.")
            nFoodCal = input()
            if nFoodCal.replace(".", "").isnumeric():
                isTrue = True

        food.loc[len(food)] = [foodInput, 100, nFoodCal]
        food.to_csv("FoodCalories.csv", index=False)
    else:
        print("This food already exist")
        

 # function to find a food in the database or handle cases where the entered food might not be found
def findFood():
    food = pd.read_csv("FoodCalories.csv") # read food data from the CSV file
    foodName = food["Food"].tolist() # get a list of food names from the dataframe
    foodInput = input("Please enter food you ate today: ") # ask the user to input the food they ate
    
    pFood = [i for i in foodName if foodInput.lower() in str(i).lower()] #find the foodname that match the user input (case-insensitive)
    
    if len(pFood) != 0: # if there are matching foods, provide a list for the user to choose from
        print("here is a list food you are probably looking for:")
        print(pFood)
        
        userCheck = input("Please enter the food you ate (Please match the food in the list): or enter 'add' to add "
                          "new food: ") # Ask the user to confirm the food choice or add a new food
        
        if userCheck.lower() == 'add': # if the user wants to add a new food
            addFood(foodInput.capitalize())
            
        elif userCheck in foodName: # if the user entered an existing food from the list
            return userCheck
        else: # If the user input is not valid, loop until a valid input is provided
            isTrue = False
            while not isTrue:
                print("Invalid food, please try again")
                foodInput = input("Please enter food you ate today: ")
                pFood = [i for i in foodName if foodInput.lower() in str(i).lower()]
                
                
                if len(pFood) != 0: # If there are matching foods, provide a list for the user to choose from
                    print("here is a list food you are probably looking for:")
                    print(pFood)
                    
                    userCheck = input(
                        "Please enter the food you ate (Please match the food in the list): or enter 'add' to add "
                        "new food: ")  # ask the user to confirm the food choice or add a new food
                    if userCheck.lower() == 'add':  # if the user wants to add a new food
                        addFood(foodInput.capitalize())
                        food = pd.read_csv("FoodCalories.csv")
                        foodName = food["Food"].tolist()
                    if foodInput.capitalize() in foodName and userCheck == foodInput: # if the user entered an existing food from the list
                        isTrue = True
                else: # if there are no matching foods, handle the case
                    foodInput = noFoodResult(foodInput)

    else:
        foodInput = noFoodResult(foodInput)

    return foodInput.capitalize()


# function to add a new exercise to the database if it doesn't already exist
def addExec(execInput):
    isTrue = True
    exercise = pd.read_csv("Calories Burned in 30-minute activities.csv") # read exercise data from the CSV file
    execName = exercise["Activity"].tolist() # get a list of exercise names from the dataframe
    if execInput not in execName: # check if the provided exercise is not already in the list
        nExecCal = input("Please enter the exercise calories per 30Min: ")
        if not nExecCal.replace(".", "").isnumeric():# validate user input
            isTrue = False
        while not isTrue: # continue prompting until valid input is received
            print("not a number, Please re Enter.")
            nExecCal = input()
            if nExecCal.replace(".", "").isnumeric(): # validate user input
                isTrue = True

        exercise.loc[len(exercise)] = [execInput, nExecCal]  # add the new exercise to the dataframe
        exercise.to_csv("Calories Burned in 30-minute activities.csv", index=False)  # save the updated dataframe to the CSV file
    else:
        print("This exercise already exist") # inform the user that the exercise already exists

# function to handle cases where the entered exercise might not be in the database
# asks the user if they want to add the exercise to the database

def noExecResult(execInput):
    isTrue = True
    userInput = input("The exercise you entered might be out of range, do you want to add it to the database? "
                      "yes/no: ") # ask the user if they want to add the exercise to the database
    if userInput.lower() != "yes" and userInput.lower() != "no": #validate user input
        isTrue = False
    while not isTrue: # continue prompting until valid input is received
        print("Invalid, please re Enter")
        userInput = input("Please enter yes/no: ")
        if userInput.lower() != "yes" or userInput.lower() != "no": #vValidate user input
            isTrue = True
    if userInput == 'yes':  # if the user wants to add the exercise, call the addExec function
        addExec(execInput.capitalize())
    else:  # if the user doesn't want to add the exercise, try finding another exercise
        execInput = findExec()
    return execInput


# function to handle cases where the entered exercise might not be in the database
# asks the user if they want to add the exercise to the database
def findExec():
    exercise = pd.read_csv("Calories Burned in 30-minute activities.csv") #read the database 
    execName = exercise["Activity"].tolist()  # get a list of exercise names from the dataframe
    execInput = input("Please enter exercise you done today: ") # ask the user to input the exercise they did
    pExec = [i for i in execName if execInput.lower() in str(i).lower()] # find exercises that match the user input (case-insensitive)
    if len(pExec) != 0:  # if there are matching exercises, provide a list for the user to choose from
        print("here is a list exercise you are probably looking for:")
        print(pExec)
        userCheck = input("Please enter the exercise you take (Please match the exercise in the list): or enter 'add' "
                          "to add new exercise: ")  # ask the user to confirm the exercise choice or add a new exercise
        if userCheck.lower() == 'add':  # if the user wants to add a new exercise
            addExec(execInput.capitalize())
        elif userCheck in execName:  # if the user entered an existing exercise from the list
            return userCheck
        else: # if the user input is not valid, loop until a valid input is provided
            isTrue = False
            while not isTrue:
                print("Invalid exercise, please try again")
                execInput = input("Please enter exercise you done today: ")
                pExec = [i for i in execName if execInput.lower() in str(i).lower()]
                if len(pExec) != 0: # if there are matching exercises, provide a list for the user to choose from
                    print("here is a list exercise you are probably looking for:")
                    print(pExec)

                    userCheck = input("Please enter the exercise you take (Please match the exercise in the list): or "
                                      "enter 'add' to add new exercise: ")  # ask the user to confirm the exercise choice or add a new exercise
                    if userCheck.lower() == 'add':  # if the user wants to add a new exercise
                        addExec(execInput.capitalize())
                        exercise = pd.read_csv("Calories Burned in 30-minute activities.csv")
                        execName = exercise["Activity"].tolist()
                    if execInput.capitalize() in execName and userCheck == execInput: # if the user entered an existing exercise from the list
                        isTrue = True
                else: # if there are no matching exercises, handle the case
                    execInput = noExecResult(execInput)
    else: # if there are no matching exercises, handle the case
        execInput = noExecResult(execInput)

    return execInput.capitalize() # return the selected or added exercise (capitalized)

# function to get the calorie content of a specific food from the database
def getFoodCalories(foodInput):
    food = pd.read_csv("FoodCalories.csv") # read food data from the CSV file
    foodCal = food["calories (cal)"] # extract the "calories (cal)" column from the dataframe
    foodName = food["Food"].tolist()  # get a list of food names from the dataframe
    calIndex = foodName.index(foodInput) # find the index of the given food input in the list of food names
    return foodCal[calIndex] # return the calorie content corresponding to the given food input

# function to get the calorie content of a specific exercise from the database
def getExecCalories(execInput):
    exercise = pd.read_csv("Calories Burned in 30-minute activities.csv") # read fexercise data from the CSV file
    execName = exercise["Activity"].tolist() # get a list of activity names from the dataframe
    execCal = exercise["Calories"]   # extract the "Calories" column from the dataframe
    calIndex = execName.index(execInput) # find the index of the given activity input in the list of activity names
    return execCal[calIndex]  # return the calorie content corresponding to the given activity input


# main function to calculate total calories based on user input of food intake and exercise activities
# using functions like findFood and findExec to handle user input and retrieve calorie information
def calculate():
    isTrue = True
    totalCal = 0
    user = input("Please begin add your food intake, to continue add, enter 1, to stop, enter 2: ") # prompt the user to add food intake or stop
    if not user.isdigit(): # validate user input
        isTrue = False
    while not isTrue:
        print("not a number, Please re Enter. Or press number 9 for instructions")
        user = input("Please enter a number: ")
        if user.isdigit():
            isTrue = True
    while int(user) != 2:  # continue adding food intake until the user decides to stop
        if int(user) == 1:
            foodInput = findFood()  # find and add food intake
            amount = input("How many grams did you take: ")
            if not amount.replace(".", "").isnumeric(): # validate amount input
                isTrue = False
            while not isTrue: # continue prompting until valid input is received
                print("not a number, Please re Enter.")
                amount = input()
                if amount.replace(".", "").isnumeric():
                    isTrue = True
            cal = getFoodCalories(foodInput) * (eval(amount) / 100)  # calculate and update total calories
            totalCal += cal
        else:
            print("Invalid number, please try again")
            print("Enter 1 to keep add food intake")
            print("Enter 2 to stop")
        user = input("Please begin add your food intake, to continue add, enter 1, to stop, enter 2: ")
        if not user.isdigit():
            isTrue = False
        while not isTrue:
            print("not a number, Please re Enter.")
            user = input("Please enter a number: ")
            if user.isdigit():
                isTrue = True
    user = input("Please begin add exercise you have done, to continue add, enter 1, to stop, enter 2: ") # prompt the user to add food intake or stop
    if not user.isdigit(): # validate user input
        isTrue = False
    while not isTrue: # continue prompting until valid input is received
        print("not a number, Please re Enter. Or press number 9 for instructions")
        user = input("Please enter a number: ")
        if user.isdigit():
            isTrue = True
    while int(user) != 2: # continue adding exercise until the user decides to stop
        if int(user) == 1:
            execInput = findExec() # find and add exercise
            amount = input("How many minutes did you do: ") # validate amount input
            if not amount.replace(".", "").isnumeric():
                isTrue = False
            while not isTrue:
                print("not a number, Please re Enter.")
                amount = input()
                if amount.replace(".", "").isnumeric():
                    isTrue = True
            cal = getExecCalories(execInput) * (eval(amount) / 30) # calculate and update total calories
            totalCal -= cal
        else:
            print("Invalid number, please try again")
            print("Enter 1 to keep add food intake")
            print("Enter 2 to stop")
        user = input("Please begin add your food intake, to continue add, enter 1, to stop, enter 2: ")
        if not user.isdigit():
            isTrue = False
        while not isTrue:
            print("not a number, Please re Enter.")
            user = input("Please enter a number: ")
            if user.isdigit():
                isTrue = True
    print('totalCal is ' + str(totalCal)) # display total calories and provide feedback
    if totalCal < 0:
        print("Congratulations, you have lost some weight!")
    elif totalCal == 0:
        print("Congratulations, you did not gain any weight")
    else:
        print("You have gain some extra calories, don't worry, let's do some more exercises.")
