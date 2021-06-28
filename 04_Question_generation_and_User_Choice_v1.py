#Question generation and User Choice component version 1

#Question Checker function
def question_checker(question):

    while True:
        try:
            response = int(input(question))

            if response == question_given:
                print("Correct")
                continue

            elif response != question_given:
                print("Wrong")
                continue

            return response

        except ValueError:
            print("<Error> please input an integer")
            continue


question_given = 1 + 1

game_loop = ""
while game_loop == "":

    question_asked = question_checker("What is 1 + 1? ")
