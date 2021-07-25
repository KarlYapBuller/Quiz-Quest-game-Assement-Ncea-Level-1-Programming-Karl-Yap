#Round looping component version 3
#The Game Statistics and History was added to the code

import random

def check_how_many_questions(question):
    while True:
        #Ask the User how many questions they want to answer if they want to play the
        #option where they can choose how many questions they want
        #to answer of if they want to play the continuous question option
        response = input(question)

        how_many_questions_error = "Please input either an integer that is more than 0 or <ENTER>."
#If ifinite mode is not chosen, check response is an integer more than 0
        if response != "":
            try:
                response = int(response)

#If response is too low, go back to the start of the loop and display an error message to help user
                if response < 1:
                    print(how_many_questions_error)
                    continue

            except ValueError:
                print(how_many_questions_error)
                continue

        return response

#Game Mode Input Checker Function
def game_mode_input_checker(question):
    while True:

        #Error message
        error_message = "Error please input an Integer between 1 and 4 (1. Addition 2. Subtraction 3. Multiplication 4. Division)"

        try:
            #It is an float input in the case the User inpurs a valid input but just with a .0
            response = float(input(question))

            #If User's response is 1 return the response
            if response == 1:
                return response

            #If User's response is 2 return the response
            elif response == 2:
                return response

            #If User's response is 3 return the response
            elif response == 3:
                return response

            #If User's response is 3 return the response
            elif response == 4:
                return response

            #If User's response is not 1,2,3,4 print the <ERROR> message
            else:
                print(error_message)
                print()
                continue

        #If the User inputs an invalid value print the <ERROR> message
        except ValueError:
            print(error_message)
            print()

#Input Checker
def input_checker(question):
    while True:
        try:
            #It is an float input in the case the User inputs a calid input but just with a .0
            response = float(input(question))
            return response
        # Error message will be printed out to the User
        except ValueError:
            print("<ERROR> Please enter an Integer\n")
            continue

#Continue the game function
def continue_game(question):
    valid = False
    while not valid:
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

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

#Main routine goes here

#Game Summary
game_summary = []

#Questions answered correct
questions_answered_correct = 0

#Questions answered incorrect
questions_answered_incorrect = 0

#Number of question answered
number_of_questions_answered = 0

game_loop = ""
while game_loop == "":

    user_choice_of_questions = check_how_many_questions("How many questions do you want to answer: ")

    #Asks the User what game mode they want to play (1. Addition 2. Subtraction 3. Multiplication 4. Division)
    game_mode = game_mode_input_checker("What game mode do you want to play (1. Addition 2. Subtraction 3. Multiplication 4. Division)? ")

    while number_of_questions_answered < user_choice_of_questions:

        #If the User's Choice is <ENTER> the User has decided to answer the Continuous Question's option
        if user_choice_of_questions == "":
            heading = "Continuous Question: Question {}".format(number_of_questions_answered + 1)

        #If the User's Choice is not <ENTER> the User has decided to play the User Question number choose option
        else:
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
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                #Puts the question outcome in the game summary list
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_correct += 1


            #If the User's response is not equal to the answer (Number 1 + Number 2) the User gets the question 'Incorrect'
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                #Puts the question outcome in the game summary list
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_incorrect += 1



            print(question_outcome)

            #End game if the number of rounds has been played
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
            #The number of questions the User answered will be reset to 0
            if game_loop == "xxx":
                number_of_questions_answered = 0
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
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                #Puts the question outcome in the game summary list
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_correct += 1

                #If the User's response is not equal to the answer (Number 1 - Number 2/Number 2 - Number 1)
                #The User gets the question 'Incorrect'
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                #Puts the question outcome in the game summary list
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_incorrect += 1

            print(question_outcome)

            #End game if the number of rounds has been played
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
            #The number of questions the User answered will be reset to 0
            if game_loop == "xxx":
                number_of_questions_answered = 0
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
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                #Puts the question outcome in the game summary list
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_correct += 1

            #If the User's response is not equal to the answer (Number 1 x Number 2)
            #The User gets the question 'Incorrect'
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                #Puts the question outcome in the game summary list
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_incorrect += 1

            print(question_outcome)

            #End game if the number of rounds has been played
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
            #The number of questions the User answered will be reset to 0
            if game_loop == "xxx":
                number_of_questions_answered = 0
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
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                #Puts the question outcome in the game summary list
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_correct += 1

            #If the User's response is not equal to the answer (Product answer / Number 1 = Number 2)
            #The User gets the question 'Incorrect'
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                #Puts the question outcome in the game summary list
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_incorrect += 1

            print(question_outcome)

            #End game if the number of rounds has been played
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
            #The number of questions the User answered will be reset to 0
            if game_loop == "xxx":
                number_of_questions_answered = 0
                break

    game_loop = continue_game("If you wish to play the game again press <ENTER>, if you do not want to play the game again type 'xxx': ")

#The game summary is displayed to the User
#The game sumary includes the Question number and the question answered result
#The number of questions answered correct and incorrect is displayed to the User
#The percentage of how many questions the User has answered correct and how many questions they have answered incorrect
print()
print("*****Game History*****")
for game in game_summary:
    print(game)

print("Thank You for playing the Quiz Quest Game")
