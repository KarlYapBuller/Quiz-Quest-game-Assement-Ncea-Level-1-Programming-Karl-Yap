#Question generation and User Choice component version 1
#Float input is added to the code instead of the int (integer) input for when the
#User answers the question because if the question is What is 1 + 1? Which is 2 the
#User can answer 2 or 2.0 because they are the same number
#In the Question generation and User Choice component version 2 if the
#User would have in this theoritacl situation inputed 2.0 the
#Game <Error> message will have appeared which it should not have.

#Question Checker function
def question_checker(question):

    while True:
        try:
            response = float(input(question))

            #If the User response is equal to the question given
            #User gets the question correct
            if response == question_given:
                print("Correct")
                print()
                continue

            #If the User response is not equal to the question given
            #User gets the question wrong
            elif response != question_given:
                print("Incorrect")
                print()
                continue

            return response

        #If the User inputs a string or an unexpected vale
        #The User will be displayed an <Error> message to please input an integer
        except ValueError:
            print("<Error> please input an integer")
            print()
            continue

#Question given
#1 + 1 = 2
question_given = 1 + 1

#Game loop
#Set for testing purposes
game_loop = ""
while game_loop == "":

    #Question asked to the User
    #The Question is 'What is 1 + 1?'
    question_asked = question_checker("What is 1 + 1 equal to? (Please input an integer) ")
