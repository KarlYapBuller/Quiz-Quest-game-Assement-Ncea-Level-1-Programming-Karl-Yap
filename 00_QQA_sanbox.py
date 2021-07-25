#Question generation and User Choice Component 4

import random

def game_mode_input_checker(question):
    while True:

        error_message = "Error please input an Integer between 1 and 4 (1. Addition 2. Subtraction 3. Multiplication 4. Division)"

        try:
            response = float(input(question))

            if response == 1:
                return response

            elif response == 2:
                return response

            elif response == 3:
                return response

            elif response == 4:
                return response

            else:
                print(error_message)
                continue

        except ValueError:
            print(error_message)

def check_how_many_questions():
    while True:
        #Ask the User how many questions they want to answer if they want to play the
        #option where they can choose how many questions they want
        #to answer of if they want to play the continuous question option
        response = input("How many questions do you want to answer: ")

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

game_loop = ""
while game_loop == "":

    game_summary = []

    number_of_questions_answered = 0

    user_choice_of_questions = check_how_many_questions()

    game_mode = game_mode_input_checker("What game mode do you want to play (1. Addition 2. Subtraction 3. Multiplication 4. Division)? ")

    NUMBER_1 = random.randint(0,20)
    NUMBER_2 = random.randint(0,20)
    ERROR_MESSAGE = "Please Enter an Integer! "
    RESULT_CORRECT = "Correct! "
    RESULT_INCORRECT = "Incorrect! "

    while number_of_questions_answered < user_choice_of_questions:

        #If the User's Choice is <ENTER> the User has decided to answer the Continuous Question's option
        if user_choice_of_questions == "":
            heading = "Continuous Question: Question {}".format(number_of_questions_answered + 1)

        #If the User's Choice is not <ENTER> the User has decided to play the User Question number choose option
        else:
            heading = "Question {} of {}".format(number_of_questions_answered + 1, user_choice_of_questions)

        if game_mode == 1:
            #Displays round and game information
            statement_generator(heading, "+")

            answer = NUMBER_1 + NUMBER_2

            try:
                response = float(input("What is {} + {}?  ".format(NUMBER_1, NUMBER_2)))

                if response == answer:
                    question_outcome = "Result: {} | Your Answer: {} | Correct Answer: {}".format(RESULT_CORRECT, response, answer)
                    number_of_questions_answered += 1

                else:
                    question_outcome = "Result: {} | Your Answer: {} | Correct Answer: {}".format(RESULT_INCORRECT, response, answer)
                    number_of_questions_answered += 1

            except ValueError:
                print(ERROR_MESSAGE)

            #End game if the number of rounds has been played
            if number_of_questions_answered == user_choice_of_questions:
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

            game_summary.append(question_outcome)



        elif game_mode == 2:
            #Displays round and game information
            statement_generator(heading, "-")

            answer = NUMBER_1 - NUMBER_2

            if NUMBER_1 > NUMBER_2:
                answer = NUMBER_2 - NUMBER_1

            error_message = "Please input an Integer"

            try:
                if answer == NUMBER_1 - NUMBER_2:
                    response = float(input("What is {} - {}? ".format(NUMBER_1, NUMBER_2)))

                else:
                    response = float(input("What is {} - {}? ".format(NUMBER_2, NUMBER_1)))

                if response == answer:
                    result = "Correct"
                    print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                    number_of_questions_answered += 1

                else:
                    result = "Incorrect"
                    print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                    number_of_questions_answered += 1

            except ValueError:
                print(ERROR_MESSAGE)

            #End game if the number of rounds has been played
            if number_of_questions_answered == user_choice_of_questions:
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

        elif game_mode == 3:
            #Displays round and game information
            statement_generator(heading, "x")

            answer = NUMBER_1 * NUMBER_2

            error_message = "Please input an Integer"

            try:
                response = float(input("What is {} x {}? ".format(NUMBER_1, NUMBER_2)))

                if response == answer:
                    result = "Correct"
                    print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                    number_of_questions_answered += 1

                else:
                    result = "Incorrect"
                    print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                    number_of_questions_answered += 1

            except ValueError:
                print(ERROR_MESSAGE)

            #End game if the number of rounds has been played
            if number_of_questions_answered == user_choice_of_questions:
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

        elif game_mode == 4:
            #Displays round and game information
            statement_generator(heading, "/")

            product_answer = NUMBER_1 * NUMBER_2
            answer = NUMBER_2

            error_message = "Please input an Integer"

            try:
                response = float(input("What is {} / {}? ".format(product_answer, NUMBER_2)))

                if response == answer:
                    result = "Correct"
                    print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                    number_of_questions_answered += 1

                else:
                    result = "Incorrect"
                    print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                    number_of_questions_answered += 1

            except ValueError:
                print(ERROR_MESSAGE)

            #End game if the number of rounds has been played
            if number_of_questions_answered == user_choice_of_questions:
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


    #If the number of rounds played is more than or equal to
    #One the User will be asked if they wish to continue the game or if they wish to
    #Quit the game they should input 'xxx'
    if number_of_questions_answered >= 1:
        print()
        game_loop = continue_game("If you want to play the game again press <Enter>, if you wish to quit playing the game 'xxx': ")
        print()

for game in game_summary:
    print(game)

print("Thank You for playing the Quiz Quest Game")

