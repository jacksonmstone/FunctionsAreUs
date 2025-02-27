#this is the source code of the soccer app

import random
#stat it off with a list
allgames = []
hometeam = input("what is the Home Team name? ").upper()
valid = False
while valid == False:
    try:
        gamecount= int(input("How many games did they play this season? "))
        if gamecount <= 0:
            print("\nPlease enter a non-negative, non-zero number.")
        else:
            valid = True
        # Exit loop if input is valid
    except ValueError:
        print("\nPlease enter a valid number.")

dictteam= {}
#initialize score 
wincount = 0 
losscount = 0 

#collect the info of each game, and inject it into the list
#each game should be its own dictionary with the opposing team as the key

for icount in range(gamecount):
    #away team name
    awayteam = input(f"What was the Away Team's Name for game {icount + 1}?  ").upper()

    #generate score for the game
    awayscore = random.randrange(0, 10)
    homescore = random.randrange(0, 10)

    #prevent ties
    while homescore == awayscore:
        awayscore = random.randrange(0, 10)

    #decide winner and loser and add to total win loss count
    if homescore > awayscore:
        wincount += 1
        winorloss = "WIN"
    elif homescore < awayscore:
        losscount += 1 
        winorloss = "LOSS"


    #store the info of the game into dictionary
    dictteam[awayteam] = {"AwayTeam": awayteam, "Score": awayscore, "HomeScore": homescore, "winorloss": winorloss}

    #add the dictionaries to the game list
    allgames.append(dictteam[awayteam])


#print the seasons game results
print('\n\n')
for icount in range(gamecount):
    print (f"{allgames[icount]['AwayTeam']}'s score:{allgames[icount]['Score']} {hometeam}'s score:{allgames[icount]['HomeScore']} {allgames[icount]['winorloss']} ")

#print season total results
print(f'\nThe final season record was {wincount} - {losscount}')

#decide wether it was a good season
if losscount == 0:
    print("You qualified for the NCAA Womens Tournament with a perfect season")
    
# if the 0 count is not a concern
if losscount > 0:
    winratio = wincount / losscount
    if winratio >= 0.75:
        print("You qualified for the NCAA Womens Tournament")
    elif winratio >= 0.5:
        print("You had a good season!")
    else:
        print("Your Team needs practice!")

