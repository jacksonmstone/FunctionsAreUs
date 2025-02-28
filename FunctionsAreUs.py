#main functions page, where all of the functions are combined to make the program
teams = []
teams = ["BYU Cougars", "University of Utah Utes", "Utah State Aggies", "Weber State Wildcats", "UVU Wolverines"]

from functionOne import intro, playorno
from Function3 import printTeams, getNumber
from function4 import results, winloss


UserName = intro()

run = playorno(UserName)

for icount in range ():
    if run == True:
        #print out all the teams on my list
        print("Here are all the women's soccer teams for the 2025 season!")
        printTeams(teams)


        #get the number team we are looking at
        print("What team are we looking at this season?")
        teamNum = getNumber(teams)
        myTeam = teams[teamNum] #save our team name
        teams.pop(teamNum) #need to adjust our list to take out the team we selected

        print("\n")
        #print out all the remaining teams
        printTeams(teams)


        #get the number team we want to play
        print("What team would you like to play this season?")
        teamNum = getNumber(teams)
        oppTeam = teams[teamNum] 


        #print the teams we selected

        myscore, awayscore = results(myTeam, oppTeam)
        job = winloss(myscore,awayscore)
        
        print(f"My team: {myTeam} {myscore}")
        print(f"Opposing team: {oppTeam} {awayscore}")
        print(f"your team came back with a {job}")


