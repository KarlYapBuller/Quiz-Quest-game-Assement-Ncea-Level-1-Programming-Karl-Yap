#set for testing purposes
questions_wanted_to_answer = 5

questions_answered = 0

question_1 = 1 + 1

#.lower is used just in case user types in exit code, 'xxx' in uppercase
play_again = input("Press <Enter> to play").lower()
while play_again == "":

    #Increase #rounds played
    questions_answered += 1

    #Print number of rounds played
    print("*****Round#{}*****".format(questions_answered))

    question_asked = input(int("What is 1 + 1 (Please input an integer)? "))

    if question_asked == 2:
        feedback = "Correct"

    elif question_asked != 2:
        feedback = "Wrong"

    print("You got the question {}".format(feedback))

#If balance is less than one program displays sorry you have run out of money
#User can choose if they want to continue the game or quit the game
    if questions_answered == questions_wanted_to_answer:
        play_again = "xxx"

    if play_again == "xxx":
        break

    else:
        play_again = input("Press <Enter> to play again or 'xxx' to quit game")
        print()
