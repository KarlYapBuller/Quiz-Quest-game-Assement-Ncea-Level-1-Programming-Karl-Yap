#Question generation and User Choice component version 1

#Question Checker function
def question_checker(question):

    while True:
        try:
            response = int(input(question))

            #If the User response is equal to the question given
            #User gets the question correct
            if response == question_given:
                print("Correct")
                continue

            #If the User response is not equal to the question given
            #User gets the question wrong
            elif response != question_given:
                print("Wrong")
                continue

            return response

        #If the User inputs a string or an unexpected vale
        #The User will be displayed an <Error> message to please input an integer
        except ValueError:
            print("<Error> please input an integer")
            continue

#Question given
#! + 1 = 2
question_given = 1 + 1

#Game loop
#Set for testing purposes
game_loop = ""
while game_loop == "":

    #Question asked to the User
    #The Question is 'What is 1 + 1?'
    question_asked = question_checker("What is 1 + 1? ")
