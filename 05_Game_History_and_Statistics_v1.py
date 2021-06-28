#Game History

game_summary = []

questions_answered_correct = 0
questions_answered_incorrect = 0
question_answered = 5

for item in range(0, 5):
    result = input("Question Result: ")

    outcome = "Question {}: {}".format(item, result)

    if result == "incorrect":
        questions_answered_incorrect += 1

    elif result == "correct":
        questions_answered_correct += 1

    game_summary.append(outcome)

print()
print("*****Game History*****")
for game in game_summary:
    print(game)

print()
