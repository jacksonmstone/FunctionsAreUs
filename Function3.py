#This is completing Function 3 
#Created by Seth Gould

# 3. Display list of all teams and allow the user to choose a team using a menu. 
# Call the function again to let the user choose the opponent but do not display the team they chose previously. 
# Remove that team from the list. Allow the user to select an opponent, and return team name. 
# This function should receive a parameter but give it a default value if none is passed. 
# You can use this function for both choosing the home team and the opponent team.


#function to print teams
def printTeams(teamList):
    count = 0
    while count < len(teamList):
        print(f"{count+1}  {teamList[count]}")
        count = count +1

def getNumber(teamList = 0):
    cont = True
    while cont == True:
        try:
            teamNum = int(input("Enter the number for the team: "))-1
            if teamNum >= 0 and teamNum < len(teamList):
                cont = False
            else:
                print("Error. Bad input.")
        except ValueError:
            print("Error. Bad input.")
    return teamNum






# teams = []
# teams = ["BYU Cougars", "University of Utah Utes", "Utah State Aggies", "Weber State Wildcats", "UVU Wolverines"]



# #print out all the teams on my list
# print("Here are all the women's soccer teams for the 2025 season!")
# printTeams(teams)


# #get the number team we are looking at
# print("What team are we looking at this season?")
# teamNum = getNumber(teams)
# myTeam = teams[teamNum] #save our team name
# teams.pop(teamNum) #need to adjust our list to take out the team we selected


# #print out all the remaining teams
# printTeams(teams)


# #get the number team we want to play
# print("What team would you like to play this season?")
# teamNum = getNumber(teams)
# oppTeam = teams[teamNum] 


# #print the teams we selected
# print(f"My team: {myTeam}")
# print(f"Opposing team: {oppTeam}")
