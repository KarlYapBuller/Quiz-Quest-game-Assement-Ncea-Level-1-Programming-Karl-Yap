#Question geeration, User Choice and Game Mode component version 5

#Question generation and User Choice Component 4

import random

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

#Main routine goes here

game_loop = ""
while game_loop == "":

    #Number of question answered
    number_of_questions_answered = 0

    #Asks the User what game mode they want to play (1. Addition 2. Subtraction 3. Multiplication 4. Division)
    game_mode = game_mode_input_checker("What game mode do you want to play (1. Addition 2. Subtraction 3. Multiplication 4. Division)? ")
    print()

    #Game Mode 1. Addition
    if game_mode == 1:

        #Set ten questions for testing purposes
        for item in range(0,10):
            #Prints out the Question Number
            print("*****Question {}*****".format(number_of_questions_answered +1))

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
                print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                print()
                number_of_questions_answered += 1

            #If the User's response is not equal to the answer (Number 1 + Number 2) the User gets the question 'Incorrect'
            else:
                result = "Incorrect"
                print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                print()
                number_of_questions_answered += 1

    #Game Mode 2. Subtraction
    elif game_mode == 2:

        #Set ten questions for testing purposes
        for item in range (0,10):

            #Prints out the Question Number
            print("*****Question {}*****".format(number_of_questions_answered +1))

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
                print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                print()
                number_of_questions_answered += 1

            #If the User's response is not equal to the answer (Number 1 - Number 2/Number 2 - Number 1)
            #The User gets the question 'Incorrect'
            else:
                result = "Incorrect"
                print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                print()
                number_of_questions_answered += 1

    #Game Mode 3. Multiplication
    elif game_mode == 3:

        #Set ten questions for testing purposes
        for item in range(0,10):

            #Prints out the Question Number
            print("*****Question {}*****".format(number_of_questions_answered +1))

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
                print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                print()
                number_of_questions_answered += 1

            #If the User's response is not equal to the answer (Number 1 x Number 2)
            #The User gets the question 'Incorrect'
            else:
                result = "Incorrect"
                print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                print()
                number_of_questions_answered += 1

    #Game Mode 4. Division
    elif game_mode == 4:

        #Set ten questions for testing purposes
        for item in range(0,10):
            #Prints out the Question Number
            print("*****Question {}*****".format(number_of_questions_answered +1))

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
                print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                print()
                number_of_questions_answered += 1

            #If the User's response is not equal to the answer (Product answer / Number 1 = Number 2)
            #The User gets the question 'Incorrect'
            else:
                result = "Incorrect"
                print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                print()
                number_of_questions_answered += 1


