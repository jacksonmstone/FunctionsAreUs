#this is the functions page
#David Medina 2/26/25
#Function Five, Display Games
def display_record(gamecount, allgames, hometeam) :
    for icount in range(gamecount):
        print (f"{allgames[icount]['AwayTeam']}'s score:{allgames[icount]['Score']} {hometeam}'s score:{allgames[icount]['HomeScore']} {allgames[icount]['winorloss']} ")