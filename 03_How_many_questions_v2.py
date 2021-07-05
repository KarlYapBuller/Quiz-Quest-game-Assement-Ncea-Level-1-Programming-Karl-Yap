#Get and Check User input
#If the situation is "low only" was deleted because it was not needed because
#the low and high variable were defined when asking the question of "How many questions the User wanted to answer"
#The low variable was 1 and the High variable was 20

#Number Checking Function goes here
def integer_check(question, low=None, high=None):

    situation = ""

    #If the low variable is defined and the high variable is defined the situation is "both"
    if low is not None and high is not None:
        situation = "both"

    while True:

        try:
            #User input has to be an integer
            #User had to input the integer to the given question
            response = int(input(question))

            #If the low variable is defined and the high variable is defined the situation is 'both'
            if situation == "both":
                #If the response is less than the defined low variable and the response is higher than the high defined variable
                #The User is asked to input an integer between the defined low and high variables
                if response < low or response > high:
                    print("Please enter an integer between {} and {}".format(low, high))
                    continue

            return response

        #If the User does not input an integer
        except ValueError:
            print("Please enter an integer")
            continue

#Main Routine

#The game is looped so testing for test cases is easier
game_loop = ""
while game_loop == "":
    #The User is asked the question 'How many questions would you like to answer'
    #The minimum number of questions the User can answer is 1 question
    #The maximum number of questions the User can answer is 20 questions
    how_many_questions = integer_check("How many questions would you like to answer (Integer between 1 and 20)? ", 1, 20)
    print("Questions Chosen to Answer: {}".format(how_many_questions))
    print()
