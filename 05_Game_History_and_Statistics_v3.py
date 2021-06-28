#Game History and Statistics component version 3
#This piece of code is the same as version 2 but displays to the User
#The percentage of how many questions they have answered correct and how many questions they have answered incorrect

#Game summary list for the questions answered results
game_summary = []

#Questions answered correct
questions_answered_correct = 0

#Questions answered incorrect
questions_answered_incorrect = 0

#The number of question answered
number_of_questions_answered = 5

#Loop of 5 questions
for question_number in range(0, 5):
    #Input the Question Result
    question_result = input("Question Result: ")

    #Question number and question answered result
    question_outcome = "Question {}: {}".format(question_number, question_result)

    #If the question result is incorrect
    #The questions answered incorrect increases by 1
    if question_result == "incorrect":
        questions_answered_incorrect += 1

    #If the question result is correct
    #The questions_answered_correct increases by 1
    elif question_result == "correct":
        questions_answered_correct += 1

    #Puts the question outcome in the game summary list
    game_summary.append(question_outcome)

#Calculate Game Statistics
percent_correct = questions_answered_correct / number_of_questions_answered * 100
percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

#The game summary is displayed to the User
#The game sumary includes the Question number and the question answered result
#The number of questions answered correct and incorrect is displayed to the User
#The percentage of how many questions the User has answered correct and how many questions they have answered incorrect
print()
print("*****Game History*****")
for game in game_summary:
    print(game)

print()

print("Questions Answered Correct: {} ({:.0f}%) \t|\t Questions Answered Incorrectly: {} ({:.0f}%) \t".format(questions_answered_correct,
                                                                                                              percent_correct,
                                                                                                              questions_answered_incorrect,
                                                                                                              percent_incorrect))
