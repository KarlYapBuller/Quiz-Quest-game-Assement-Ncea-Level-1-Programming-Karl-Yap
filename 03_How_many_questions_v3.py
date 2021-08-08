#How many questions component version 3
#This piece of code gives the User the option of how many questions they want to answer
#The User can choose how many questions they want to answer with the minimum number of questions the
#User has to input being 1 and there is
#no maximum number for how many questions they want to answer
#If thd User inputs a value less than 1 an Error message will appear
#If the User inputs a value more than or equal to 50 they will be asked if they wish to answer this many questions
#If the User answer yes the program will continue
#If the User answers no they will be advised to input a lower value
#This component is integrated with the Yes/No Checker

#Yes/No Checker
#Check If the User's input is valid
def yes_no_checker(question):
    valid = False
    while not valid:
        #The User response will be lowercased
        response = input(question).lower()

        #If user response is either 'yes' or 'y' the response will be outputed as yes.
        if response == "yes" or response == "y":
            response = "yes"
            return response

        #If user response is either 'no' or 'n' the response will be outputed as no.
        elif response == "no" or response == "n":
            response = "no"
            return response

        #If user response is anything other than yes or no, User will be asked to answer yes or no.
        else:
            print("<error> please answer Yes/No (Y/N). ")
            print()

def check_how_many_questions(question):
    while True:

        #How many questions error
        how_many_questions_error = "Please input either an integer that is more than 0."
        try:
            #Ask the User how many questions they want to answer
            #The User can choose how many questions they want to answer (minimum is 1 and there is no maximum)
            response = int(input(question))
            #If the User's response is too low, less than an error message will be displayed to the User and the question will be asked again
            if response < 1:
                print(how_many_questions_error)
                continue

            #If the User's respinse is more then 50, they will be aksed if they are sure they want to answer this many questions (Y/N)
            #This functions includes the yes no checker function
            if response >= 50:
                too_many_questions = yes_no_checker("Are you sure you want to answer {} questions (Y/N)? ".format(response))

                #If the User answers yes the program will continue
                if too_many_questions == "yes":
                    print("Ok! Sorry for asking")

                #If the User answers no they will be advised to input a lower value
                elif too_many_questions == "no":
                    print("Ok! Try input a lower value")
                    continue

            return response

        #If the User inputs an unexpected Value an error message will be displayed to the User and the question will be asked again
        except ValueError:
            print(how_many_questions_error)
            continue

#Main routine goes here

#Number of questions the User has answered
number_of_questions_answered = 0

#Ask the User how many questions they want to answer
user_choice_of_questions = check_how_many_questions("How many Questions would you like to answer (Please input an integer more than 0)? ")

#Question heading
heading = "Question {} of {}".format(number_of_questions_answered + 1, user_choice_of_questions)

#The question heading is outputed to the User
print(heading)
