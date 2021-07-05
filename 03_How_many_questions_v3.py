#Functions used to check input is valid

def check_rounds():
    while True:
        response = input("How many Questions would you like to answer (Press <ENTER> for continous question)? ")

        round_error = "Please type either <enter> or an integer that is more than 0"
#If ifinite mode is not chosen, check response is an integer more than 0
        if response != "":
            try:
                response = int(response)

#If response is too low, go back to the start of the loop and display an error message to help user
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response

#Main routine goes here

rounds_played = 0
#Ask user for number of rounds they want to play or if they want to play infinite mode they press <enter>

rounds = check_rounds()

if rounds == "":
    heading = "Continuous Mode: Round {}".format(rounds_played + 1)

else:
    heading = "Question {} of {}".format(rounds_played + 1, rounds)

    print(heading)
