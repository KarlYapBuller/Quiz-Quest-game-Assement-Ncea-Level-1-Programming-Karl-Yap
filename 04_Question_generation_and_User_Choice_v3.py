#Question generation and User Choice component version 3

import random

#Number of question answered
number_of_questions_answered = 0

for item in range(0,10):

    #Prints out the Question Number
    print("*****Question {}*****".format(number_of_questions_answered +1))

    number_1 = random.randint(0,20)
    number_2 = random.randint(0,20)
    answer = number_1 + number_2

    error_message = "<ERROR> Please input an Integer"

    try:
        response = float(input("What is {} + {}?  ".format(number_1, number_2)))

        if response == answer:
            result = "Correct"
            print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
            print()
            number_of_questions_answered += 1

        else:
            result = "Incorrect"
            print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
            print()
            number_of_questions_answered += 1

    except ValueError:
        print(error_message)
