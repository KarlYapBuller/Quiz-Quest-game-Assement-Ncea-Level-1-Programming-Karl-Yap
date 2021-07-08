#Question generation and User Choice component version 4
#This piece of code fixes the <ERROR> in version 3 of this component as it fixes
#The problem of the same question not being asked again when the
#User inputs an invalid value and the Error message appears to the User

import random

#Input Checker
def input_checker(question):
    while True:
        try:
            #It is an float input in the case the User input the correct answer but just with a .0
            response = float(input(question))
            return response
        #The Error message is printed out to the User
        except ValueError:
            print("<ERROR> Please input an Integer\n")
            continue

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

    #The question asked to the User
    #The Input Checker is a float input in the case the User input the correct answer but just with a .0
    response = input_checker(("What is {} + {}?  ".format(number_1, number_2)))

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
