# Maddie Parsons Team 6
# The purpose of this program is to create function 1. 

# 1. Display an introduction to the game explaining rules and prompt for their name 
# and display that in the welcome message. 
# Return the name to the main program and store it in variable 
# so it can be used throughout the program.

# Creates a function that greets the user, asks for their name, and asks them if they would like to play.
def intro() :
    print("Hello!")
    sUserName = input("Please enter your name: ").capitalize()
    print(f"Welcome to the women's soccer game, {sUserName}")
    return sUserName




def playorno(Name):
    sUserAnswer = input("Would you like to play? Yes, or No ").upper()

    # For readability
    print("\n")
    
    # Creates an if loop and shares the rules based on the user input. 
    if sUserAnswer == "YES":
        play = True
        print("Great! The rules of the game are simple.") 
        print("\n")
        print("You will select a team to play as. You will also select your opponent, so choose wisely!")
        print("\n")
        print(f'Good luck {Name}!')
    else :
        print("Have a nice day!")
        play = False
    # Returns the user name. 
    return play

# Stores the user name in a variable. 



