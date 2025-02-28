# Jackson Stone
# This program is the second function of A2

# Display of menu and return choice. Store in variable and use this value to determine which function to call next.
def second(playername):
    print(f' Ok, {playername}, What would you like to do? (Input 1 or 2)')
    bContinue = True
    
    while True:
        try :
            userInput = int(input("1) Start building your season \n2) Quit program\nInput here: "))
            if userInput in [1, 2]:
                bContinue = False
                return userInput
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid Input. Please enter again")
            return userInput


def gamesplayed(userinput):
    
    if userinput == 1:
        int(input("how many games will you play this season? "))
        gameon  = True
    else:
        print("your team did not play any games this season")
        gameon = False
    return gameon





