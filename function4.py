# Sarah Gastelum
#4. Play the game receiving both team names. Generate random scores without ties. Return W or L.

import random
def results (hometeam, awayteam):

    ihomescore = 0
    iawayscore = 0
    ihomescore = random.randint(0,11)
    iawayscore = random.randint(0,11)

    while ihomescore == iawayscore:
        ihomescore = random.randint(0,11)
        iawayscore = random.randint(0,11)

    if ihomescore > iawayscore:
        sresults = "W"

    elif ihomescore < iawayscore:
        sresults = "L"

    return sresults
        
