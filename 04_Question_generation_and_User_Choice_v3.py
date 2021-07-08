#Question generation and User Choice component version 3
#This piece of code use rando number for the addition question unlike version 1 and version 2

import random

#Number of question answered
number_of_questions_answered = 0

game_loop = ""
while game_loop == "":

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

    #Error message that is outputed to the User if they input an invalid value
    error_message = "<ERROR> Please input an Integer"

    try:
        #The question asked to the User
        #It is an float input in case the User input the correct answer but just with a .0
        response = float(input("What is {} + {}?  ".format(number_1, number_2)))

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

    #The Error message is printed out to the User
    except ValueError:
        print(error_message)
