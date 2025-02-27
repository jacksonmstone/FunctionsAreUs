# Jackson Stone
# This program is the second function of A2

# Display of menu and return choice. Store in variable and use this value to determine which function to call next.
def second():
    print(f' Ok, {player_name}, What would you like to do? (Input 1, 2, or 3)')
    bContinue = True
    
    while True:
        try :
            userInput = int(input("1) Pick your team to play as \n2) Pick the team to play against \n3) Quit program\nInput here: "))
            if userInput in [1, 2, 3]:
                bContinue = False
                return userInput
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid Input. Please enter again")

user_choice = second()
