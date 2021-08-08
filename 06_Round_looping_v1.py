#Round looping component version 1
#The Round Looping component does not work as intended
#The problem is that if the User wants to quit the game (exit code 'xxx') and
#They press <ENTER> to play the game again,
#The round heading (the number of questions the User answered) does not reset

#The import random is used for the random integer between the specified ranges
import random

#Functions

#Yes/No Checker function
def yes_no_checker(question):
    valid = False
    while not valid:
        #The User will input a response to the given question
        #The User response will be lowercased
        #.lower() is used in the case the User types the correct input but with the wrong casing
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

#Function to check how many questions the User wants to play
#User has a choice of how many questions they want to answer
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

#Function to check what Game Mode the User wants to play
def game_mode_input_checker(question):
    while True:

        #Error message
        error_message = "Error please input an Integer between 1 and 4 (1. Addition 2. Subtraction 3. Multiplication 4. Division)"

        try:
            #It is an float input in the case the User inpurs a valid input but just with a .0
            response = float(input(question))

            #If User's response is 1 (Addition) return the response
            if response == 1:
                return response

            #If User's response is 2 (Subtraction) return the response
            elif response == 2:
                return response

            #If User's response is 3 (Multiplication) return the response
            elif response == 3:
                return response

            #If User's response is 4 (Division) return the response
            elif response == 4:
                return response

            #If User's response is not 1,2,3,4 print the ERROR message
            else:
                print(error_message)
                print()
                continue

        #If the User inputs an invalid value print the ERROR message
        except ValueError:
            print(error_message)
            print()

#Function to check the User's input
#In this instance this function is used to check if the User's input for the Mathematical questions is valid
def input_checker(question):
    while True:
        try:
            #The User will input a response to the given question
            #It is an float input in the case the User inputs a calid input but just with a .0
            response = float(input(question))
            return response
        # Error message will be printed out to the User
        except ValueError:
            print("<ERROR> Please enter an Integer\n")
            continue

#Continue the game function
#This functions purpose is to ask the User after each question or if they quit playing the game if they wish to continue or quit playing the game, 'xxx'
def continue_game(question):
    valid = False
    while not valid:
        #The User will input a response to the given question
        #.lower() is used in the case the User types the correct input but with the wrong casing
        response = input(question).lower()

        if response == "":
            return response

        elif response == "xxx":
            return response

        #If response is not "" or 'xxx' Error message will display to the User
        else:
            print()
            print("<Error> please enter either <Enter> or 'xxx'")
            print()

#Statement generator
#Decorates the statements in the Lucky Unicorn game
def statement_generator(statement, decoration):

    #The of the statement is the chosen decoration times by 3
    sides = decoration * 3

    #The statement outputed to the User is the chosen statement with
    #the sides on the left and right of the statement
    statement = "{} {} {}".format(sides, statement, sides)
    #The decotration on the top and bottom of the the statement is
    #the chosen decoration and it is the length of the statement
    top_bottom = decoration * len(statement)

    #top_bottom and statement variables are outputed to the User
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

#Main routine goes here

#Questions answered correct
questions_answered_correct = 0

#Questions answered incorrect
questions_answered_incorrect = 0

#Number of question answered
number_of_questions_answered = 0

#Game loop
game_loop = ""
while game_loop == "":

    #Ask the User how many questions they want to answer
    user_choice_of_questions = check_how_many_questions("How many Questions would you like to answer (Please input an integer more than 0)? ")


    #Asks the User what game mode they want to play (1. Addition 2. Subtraction 3. Multiplication 4. Division)
    game_mode = game_mode_input_checker("What game mode do you want to play (1. Addition 2. Subtraction 3. Multiplication 4. Division)? ")

    while number_of_questions_answered < user_choice_of_questions:

        #The heading is equal to the number of questions the User has answered out of
        #the number of questions the User has chosen to answer
        heading = "Question {} of {}".format(number_of_questions_answered + 1, user_choice_of_questions)

        #Game Mode 1. Addition
        if game_mode == 1:

            #Displays to the User the Question Number
            statement_generator(heading, "#")

            #Number 1 that is in the first position before
            #The addition is a random integer between 0 and 20
            number_1 = random.randint(0,20)
            #Number 2 that is in the first position before
            #The addition is a random integer between 0 and 20
            number_2 = random.randint(0,20)
            #The answer is equal to Number 1 + Number 2
            answer = number_1 + number_2

            #The question asked to the User
            #The Input Checker is a float input in the case the User input the correct answer but just with a .0
            response = input_checker("What is {} + {}?  ".format(number_1, number_2))

            #If the User's response is equal to the answer (Number 1 + Number 2) the User gets the question 'Correct'
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                number_of_questions_answered += 1
                questions_answered_correct += 1


            #If the User's response is not equal to the answer (Number 1 + Number 2) the User gets the question 'Incorrect'
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                number_of_questions_answered += 1
                questions_answered_incorrect += 1

            #The question outcome of question is outputed to the User
            print(question_outcome)

            #End game if the number of rounds has been played
            #The number of questions answered is reset back to 0
            if number_of_questions_answered == user_choice_of_questions:
                number_of_questions_answered = 0
                break

            #If the number of rounds played is more than or equal to
            #One the User will be asked if they wish to continue the game or if they wish to
            #Quit the game they should input 'xxx'
            if number_of_questions_answered >= 1:
                print()
                game_loop = continue_game("Press <Enter> if you wish to continue the game, if you wish to quit type 'xxx': ")
                print()

            #If the User inputs 'xxx' when they are asked if they want to continue the game or not
            #The Game Loop will end
            if game_loop == "xxx":
                break

        #Game Mode 2. Subtraction
        elif game_mode == 2:

            #Displays to the User the Question Number
            statement_generator(heading, "#")

            #Number 1 that is in the first position before
            #The subtraction is a random integer between 0 and 50
            number_1 = random.randint(0,50)
            #Number 2 that is in the first position before
            #The subtraction is a random integer between 0 and 20
            number_2 = random.randint(0,50)
            #The answer is Number 1 - Number 2
            answer = number_1 - number_2

            #If number 2 is bigger than number 1
            #The answer is equal to Number 2 - Number 1
            #This is set so the User does not have to answer negate subtraction questions
            if number_2 > number_1:
                answer = number_2 - number_1

            #The question asked to the User if the answer is equal to Number 1 - Number 2
            if answer == number_1 - number_2:
                response = input_checker("What is {} - {}? ".format(number_1, number_2))

            #The question asked to the User if tbe answer is equal to Number 2 - Number 1
            else:
                response = input_checker("What is {} - {}? ".format(number_2, number_1))

            #If the User's response is equal to the answer (Number 1 - Number 2/Number 2 - Number 1)
            #The User gets the question 'Correct'
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                number_of_questions_answered += 1
                questions_answered_correct += 1

            #If the User's response is not equal to the answer (Number 1 - Number 2/Number 2 - Number 1)
            #The User gets the question 'Incorrect'
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                number_of_questions_answered += 1
                questions_answered_incorrect += 1

            #The question outcome of question is outputed to the User
            print(question_outcome)

            #End game if the number of rounds has been played
            #The number of questions answered is reset back to 0
            if number_of_questions_answered == user_choice_of_questions:
                number_of_questions_answered = 0
                break

            #If the number of rounds played is more than or equal to
            #One the User will be asked if they wish to continue the game or if they wish to
            #Quit the game they should input 'xxx'
            if number_of_questions_answered >= 1:
                print()
                game_loop = continue_game("Press <Enter> if you wish to continue the game, if you wish to quit type 'xxx': ")
                print()

            #If the User inputs 'xxx' when they are asked if they want to continue the game or not
            #The Game Loop will end
            if game_loop == "xxx":
                break

        #Game Mode 3. Multiplication
        elif game_mode == 3:

            #Displays to the User the Question Number
            statement_generator(heading, "#")

            #Number 1 that is in the first position before
            #The multiplication is a random integer between 0 and 12
            number_1 = random.randint(0,12)
            #Number 2 that is in the first position before
            #The multiplication is a random integer between 0 and 12
            number_2 = random.randint(0,12)
            #The answer is Number 1 x Number 2
            answer = number_1 * number_2

            #The question asked to the User
            response = input_checker("What is {} x {}? ".format(number_1, number_2))

            #If the User's response is equal to the answer (Number 1 x Number 2)
            #The User gets the question 'Correct'
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                number_of_questions_answered += 1
                questions_answered_correct += 1

            #If the User's response is not equal to the answer (Number 1 x Number 2)
            #The User gets the question 'Incorrect'
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                number_of_questions_answered += 1
                questions_answered_incorrect += 1

            #The question outcome of question is outputed to the User
            print(question_outcome)

            #End game if the number of rounds has been played
            #The number of questions answered is reset back to 0
            if number_of_questions_answered == user_choice_of_questions:
                number_of_questions_answered = 0
                break

            #If the number of rounds played is more than or equal to
            #One the User will be asked if they wish to continue the game or if they wish to
            #Quit the game they should input 'xxx'
            if number_of_questions_answered >= 1:
                print()
                game_loop = continue_game("Press <Enter> if you wish to continue the game, if you wish to quit type 'xxx': ")
                print()

            #If the User inputs 'xxx' when they are asked if they want to continue the game or not
            #The Game Loop will end
            if game_loop == "xxx":
                break


        #Game Mode 4. Division
        elif game_mode == 4:

            #Displays to the User the Question Number
            statement_generator(heading, "#")

            #Number 1 that is in the first position before
            #The division is a random integer between 0 and 12
            number_1 = random.randint(0,12)
            #Number 2 that is in the first position before
            #The division is a random integer between 0 and 12
            number_2 = random.randint(0,12)
            #The Product answer is Number 1 x Number 2
            product_answer = number_1 * number_2
            #The answer is equal to Number 2 beacuse that is what
            #The Product answer / Number 1 is equal to
            answer = number_2

            #The question asked to the User is what is the Product answer / Number 1
            response = input_checker("What is {} / {}? ".format(product_answer, number_1))

            #If the User's response is equal to the answer (Product answer / Number 1 = Number 2)
            #The User gets the question 'Correct'
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                number_of_questions_answered += 1
                questions_answered_correct += 1

            #If the User's response is not equal to the answer (Product answer / Number 1 = Number 2)
            #The User gets the question 'Incorrect'
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                number_of_questions_answered += 1
                questions_answered_incorrect += 1

            #The question outcome of question is outputed to the User
            print(question_outcome)

            #End game if the number of rounds has been played
            #The number of questions answered is reset back to 0
            if number_of_questions_answered == user_choice_of_questions:
                number_of_questions_answered = 0
                break

            #If the number of rounds played is more than or equal to
            #One the User will be asked if they wish to continue the game or if they wish to
            #Quit the game they should input 'xxx'
            if number_of_questions_answered >= 1:
                print()
                game_loop = continue_game("Press <Enter> if you wish to continue the game, if you wish to quit type 'xxx': ")
                print()

            #If the User inputs 'xxx' when they are asked if they want to continue the game or not
            #The Game Loop will end
            if game_loop == "xxx":
                break

    #The User will be asked if they wish to play the game again (<ENTER>) or if they wish to not
    #play the game again ('xxx')
    game_loop = continue_game("If you wish to play the game again press <ENTER>, if you do not want to play the game again type 'xxx': ")
    print()

#Thanks the User for playing the game
print("Thank You for playing the Quiz Quest Game")
