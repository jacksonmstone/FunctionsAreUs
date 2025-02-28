#main functions page, where all of the functions are combined to make the program
from functionOne import intro, playorno
from Function3 import printTeams, getNumber
from function4 import results, winloss
from Function2 import second, gamesplayed
from function5 import func5

UserName = intro()

run = playorno(UserName)

play = second(UserName)
games= gamesplayed(play)

while play == 1:
        
    teams = []
    teams = ["BYU Cougars", "University of Utah Utes", "Utah State Aggies", "Weber State Wildcats", "UVU Wolverines", "Utah Tech"]
    if run == True:
        #print out all the teams on my list
        
        print("\nHere are all the women's soccer teams for the 2025 season!")
        printTeams(teams)

        #get the number team we are looking at
        print("What team are we looking at this season?")
        teamNum = getNumber(teams)
        myTeam = teams[teamNum] #save our team name
        teams.pop(teamNum) #need to adjust our list to take out the team we selected
        print("\n")

        awayTeams = [] 
        count = 0
        numWins = 0

        while games > 0:
            
            #print out all the remaining teams
            printTeams(teams)
            #get the number team we want to play
            print("What team would you like to play this season?")
            teamNum = getNumber(teams)
            oppTeam = teams[teamNum] 
            myscore, awayscore = results(myTeam, oppTeam)
            job = winloss(myscore,awayscore)
            if job == "W":
                numWins = numWins + 1
            
            teams.pop(teamNum)
            games = games - 1
            count = count + 1
            print('\n')
        
        print(func5(myTeam,numWins))
        play = second(UserName)
