#Ask_User_if_they_have_played_before_yes_no_v1.py_Component
#The User will be asked if they have played the game before
#Yes/No Checker

#Check If they User's input is valid
def yes_no_checker(question):
    valid = False
    while not valid:
        response = input(question).lower()

        #If user response is either 'yes' or 'y' the response will be outputed as yes.
        if response == "yes" or response == "y":
            response = "yes"
            return response

        #If user response is either 'no' or 'n' the response will be outputed as no.
        elif response == "no" or response == "n":
            response = "no"
            return response

        #If user response is anything other than yes or no,user will be asked to answer yes or no.
        else:
            print("<error> please answer Yes/No (Y/N). ")

#Game information
def game_information():
    print("*****Game information*****")
    return""

#Looped for testing purposes
#Looped to make it easier to get test cases
#The 'xxx' is the exit code to stop the loop
played_before = ""
while played_before != "xxx":
    #Main Routine
    played_before = yes_no_checker("Have you played this game before? ")

    if played_before == "no":
        game_information()
        print()

    if played_before == "yes":
        print("program continues")
        print()

