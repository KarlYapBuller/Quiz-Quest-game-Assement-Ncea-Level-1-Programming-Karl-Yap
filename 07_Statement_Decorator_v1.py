#Statement Decorator component version 1

#Statement generator
#The statement generator funcrion decorates the statements in the Quiz Quest Game
def statement_generator(statement, decoration):

    #The sides of the statement on each side is three of the decorations
    sides = decoration * 3

    #The sides of the statement will have three of the chosen decoration on each side
    statement = "{} {} {}".format(sides, statement, sides)

    #The top and bottom of the statement is decorated
    #The length of the statement is the length that the
    #Decoration goes for on the top and bottom of the statement
    top_bottom = decoration * len(statement)

    #The statement that is decorated is displayed to the User
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

#Main routine goes here
statement_generator("Welcome to the Quiz Quest Game","*")
print()
statement_generator("Thank You for playing the Quiz Quest Game", "-")
