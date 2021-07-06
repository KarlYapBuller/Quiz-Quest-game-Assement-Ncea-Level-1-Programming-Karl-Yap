#How many questions component version 3
#This piece of code gives the User two options of how many questions they want to answer either the
#User can choose how many questions they want to answer with the minimum number of questions the
#User has to input they want to answer being 1 and there is
#no maximum number for how many questions they want to answer and the other option
#the User can choose is the Continuous questions where the User will be asked the continuous number of questions.


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

#Main routine goes here

number_of_questions_answered = 0

user_choice_of_questions = check_how_many_questions("How many Questions would you like to answer (Press <ENTER> for continous question)? ")

#If the User's Choice is <ENTER> the User has decided to answer the Continuous Question's option
if user_choice_of_questions == "":
    heading = "Continuous Question: Question {}".format(number_of_questions_answered + 1)

#If the User's Choice is not <ENTER> the User has decided to play the User Question number choose option
else:
    heading = "Question {} of {}".format(number_of_questions_answered + 1, user_choice_of_questions)

print(heading)
