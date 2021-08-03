#Quiz Quest
#Quiz Quest Assesment version 2
#Base Component After the Usability testing
#Things that have been fixed include better spacing of the lines outputed, the instructions are more clearer for the User,
#the questions asked to the User are more clearer, titles were added for important sections
#to catch the User attention for what that section is about
#Things that have been added include Constants for
#the reoccuring Error messsages and the comments in the code is more descriptive
#The .format has been changed to f"{}" in the code as it outputs
#the same outcome but it is more redable in the program code
#Emojis in approproate areas have also been added to make the game more visually pleasing
#'Welcome to the Quiz Quest Game' has beeen added to welcome the User to the game

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

#Function that contains the information of how to play the Quiz Quest Game
def game_information():
    statement_generator("Game Information", "#")
    print("The Quiz Quest Game is a mathematics game where you answer either addition, subtraction, multiplication or division questions\n"
    "As soon as the game starts you will be asked how many questions you want to answer where you choose the number of questions you want to answer or\n"
    "you can press <ENTER> to answer a continuos number of questions. You then will have the option to choose one of the\n"
    "four Game Modes (addition, subtraction, multiplication or division)\n"
    "previosly mentioned. After each given question you will be asked if you want to continue playing the game or not.\n" 
    "To continue playing you press <ENTER> and to stop answering questions you input 'xxx'.\n"
    "This is a lot to take in but the game is very intuitive and there should be clear instructions for you to play\n"
    "OK Good Luck! Go have some fun! Let the Game begin!\n")
    return""


#Function to check how many questions the User wants to play
#User has a choice of how many questions they want to answer or they can choose the
#Continous question option
def check_how_many_questions(question):
    while True:
        #The User will input a response to the given question
        response = input(question)

        #Error message
        how_many_questions_error = "Please input either an integer that is more than 0 or <ENTER>."
        #If ifinite mode is not chosen, check response is an integer more than 0
        if response != "":
            try:
                response = int(response)

                #If response is too low, go back to the start of the loop and display an error message to help user
                if response < 1:
                    print(how_many_questions_error)
                    continue

            #If the User inputs an invalid value, Error message is displayed
            except ValueError:
                print(how_many_questions_error)
                continue

        return response

#Function to check what Game Mode the User wants to play
def game_mode_input_checker(question):
    while True:

        #Error message
        game_mode_error_message = "Error please input an Integer between 1 and 4 (1. Addition 2. Subtraction 3. Multiplication 4. Division)"

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
                print(game_mode_error_message)
                print()
                continue

        #If the User inputs an invalid value print the ERROR message
        except ValueError:
            print(game_mode_error_message)
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
#This functions purpose is to ask the User after each question or if they quit playing the
#game if they wish to continue or quit playing the game, 'xxx'
def continue_game(question):
    valid = False
    while not valid:
        #The User will input a response to the given question
        #The User response will be lowercased
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

def game_history_and_statistics():

    #The game summary is displayed to the User
    #The game summary includes the Question number and the question answered result
    #The number of questions answered correct and incorrect is displayed to the User
    #The percentage of how many questions the User has answered correct and how many questions they have answered incorrect
    #The User will be asked if they want to see their Game History and Statistics in the final Base Component
    #This will be integrated with the yes_no function
    #Calculate Game Statistics
    print()
    print("*****Game History*****")
    for game in game_summary:
        print(game)

    print()

    print("Questions Answered Correct: {} ({:.0f}%) \t|\t Questions Answered Incorrectly: {} ({:.0f}%) \t".format(questions_answered_correct,
                                                                                                                  percent_correct,
                                                                                                                  questions_answered_incorrect,
                                                                                                                  percent_incorrect))
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

#Welcomes the User to the Quiz Quest Game
statement_generator("Welcome to the Quiz Quest Game", "#")
print()

#Heading for 'ask the User if they have played before'
#This heading is used to draw the User attention to the given question and to get the
#User to realise that this is an important part of the game and that they need to input an answer
statement_generator("Played Before", "#")
print()

#Asks the User if they have played the Game before
#If the User answers Yes the Game Continues
#If the User answers No the Game Instructions are outputed to the User
#If the User answers an invalid input an Error message will be outputed to
#the User instructing the User to input the valid value
played_before = yes_no_checker("Have you played this game before (Y/N)? ")
print()

#If the User answers No the Game Instructions are outputed to the User
if played_before == "no":
    game_information()
    print()

#Game loop
game_loop = ""
while game_loop == "":

    #Game Summary
    #This open list is used to store the User's
    #Game History of the questions they have
    #answered in the given question set
    game_summary = []

    #Questions answered correct
    #This is used to calculate the number of questions
    #the User answered correct
    questions_answered_correct = 0

    #Questions answered incorrect
    #This is used to calculate the number of questions
    #the User answered incorrect
    questions_answered_incorrect = 0

    #Number of question answered
    #This is used to calculate the number of questions
    #the User has answered
    number_of_questions_answered = 0

    #Heading for 'How many questions'
    #This heading is used to draw the User attention to the given question and to get the
    #User to realise that this is an important part of the game and that they need to input an answer
    statement_generator("How many questions", "#")

    #Ask the User how many questions they want to answer if they want to play the
    #option where they can choose how many questions they want
    #to answer of if they want to play the continuous question option
    user_choice_of_questions = check_how_many_questions("There are two options you can choose from,\n"
                                                        "for your choice of how many question you can answer.\n"
                                                        "The first is where you choose how many question you want to answer.\n"
                                                        "To choose this option just simply input an integer value for the given question.\n"
                                                        "The second option is where a continuous number of questions are asked to you.\n"
                                                        "To choose the second option press <ENTER>\n"
                                                        "\nHow many questions do you want to answer: ")

    #Heading for 'Game Mode'
    #This heading is used to draw the User attention to the given question and to get the
    #User to realise that this is an important part of the game and that they need to input an answer
    statement_generator("Game Mode", "#")
    print()

    #Asks the User what game mode they want to play (1. Addition 2. Subtraction 3. Multiplication 4. Division)
    game_mode = game_mode_input_checker("What game mode do you want to play (1. Addition 2. Subtraction 3. Multiplication 4. Division)? ")
    print()

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
            #Puts the question outcome in the game summary list by means of appending
            #This is used for the Game History
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
            #divided by the number of questions answered times by 100
            #The Percent Corcrect and Percent Incorrect is used to calculate the Game Statisitcs in
            #the Game History and Statistics function
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_correct += 1
                percent_correct = questions_answered_correct / number_of_questions_answered * 100
                percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

            #If the User's response is not equal to the answer (Number 1 + Number 2) the User gets the question 'Incorrect'
            #Puts the question outcome in the game summary list by means of appending
            #This is used for the Game History
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
            #divided by the number of questions answered times by 100
            #The Percent Corcrect and Percent Incorrect is used to calculate the Game Statisitcs in
            #the Game History and Statistics function
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_incorrect += 1
                percent_correct = questions_answered_correct / number_of_questions_answered * 100
                percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

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
            #The number of questions answered is reset back to 0
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
            #Puts the question outcome in the game summary listby means of appending
            #This is used for the Game History
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
            #divided by the number of questions answered times by 100
            #The Percent Corcrect and Percent Incorrect is used to calculate the Game Statisitcs in
            #the Game History and Statistics function
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_correct += 1
                percent_correct = questions_answered_correct / number_of_questions_answered * 100
                percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

            #If the User's response is not equal to the answer (Number 1 - Number 2/Number 2 - Number 1)
            #The User gets the question 'Incorrect'
            #Puts the question outcome in the game summary list by means of appending
            #This is used for the Game History
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
            #divided by the number of questions answered times by 100
            #The Percent Corcrect and Percent Incorrect is used to calculate the Game Statisitcs in
            #the Game History and Statistics function
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_incorrect += 1
                percent_correct = questions_answered_correct / number_of_questions_answered * 100
                percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

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
            #The number of questions answered is reset back to 0
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
            #Puts the question outcome in the game summary list by means of appending
            #This is used for the Game History
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
            #divided by the number of questions answered times by 100
            #The Percent Corcrect and Percent Incorrect is used to calculate the Game Statisitcs in
            #the Game History and Statistics function
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_correct += 1
                percent_correct = questions_answered_correct / number_of_questions_answered * 100
                percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

            #If the User's response is not equal to the answer (Number 1 x Number 2)
            #The User gets the question 'Incorrect'
            #This is used for the Game History
            #Puts the question outcome in the game summary list by means of appending
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
            #divided by the number of questions answered times by 100
            #The Percent Corcrect and Percent Incorrect is used to calculate the Game Statisitcs in
            #the Game History and Statistics function
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_incorrect += 1
                percent_correct = questions_answered_correct / number_of_questions_answered * 100
                percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

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
            #The number of questions answered is reset back to 0
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
            #Puts the question outcome in the game summary list by means of appending
            #This is used for the Game History
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
            #divided by the number of questions answered times by 100
            #The Percent Corcrect and Percent Incorrect is used to calculate the Game Statisitcs in
            #the Game History and Statistics function
            if response == answer:
                result = "Correct"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_correct += 1
                percent_correct = questions_answered_correct / number_of_questions_answered * 100
                percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

            #If the User's response is not equal to the answer (Product answer / Number 1 = Number 2)
            #The User gets the question 'Incorrect'
            #Puts the question outcome in the game summary list by means of appending
            #This is used for the Game History
            #The number of questions answered increases by 1
            #The number of qestions answered correct increases by 1
            #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
            #divided by the number of questions answered times by 100
            #The Percent Corcrect and Percent Incorrect is used to calculate the Game Statisitcs in
            #the Game History and Statistics function
            else:
                result = "Incorrect"
                question_outcome = "Question {} | Result: {} | Your Answer: {} | Correct Answer: {}".format(number_of_questions_answered + 1, result, response, answer)
                print()
                game_summary.append(question_outcome)
                number_of_questions_answered += 1
                questions_answered_incorrect += 1
                percent_correct = questions_answered_correct / number_of_questions_answered * 100
                percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

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
            #The number of questions answered is reset back to 0
            if game_loop == "xxx":
                number_of_questions_answered = 0
                break

    #Ask the User if the want to see their Game History and Statistics
    see_history_and_statistics = yes_no_checker("Do you want to see your Game History and Statistics (Y/N)? ")

    #If the User inputs 'yes' they want to see their Game History and Statistics
    #Their Game History and Statistics will be displayed
    if see_history_and_statistics == "yes":
        game_history_and_statistics()
        print()

    #The User will be asked if they wish to play the game again (<ENTER>) or if they wish to not
    #play the game again ('xxx')
    game_loop = continue_game("If you wish to play the game again press <ENTER>, if you do not want to play the game again type 'xxx': ")
    print()

#Thanks the User for playing the game
print("Thank You for playing the Quiz Quest Game")











