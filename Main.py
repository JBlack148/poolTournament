from roundRobin import *
    
        
def createNewTournament():
    playerArray = []
    playerCount = int(input("How many players are playing? "))
        
    for i in range(playerCount):
        playerName = input("What is player " + str(i + 1) + "'s name? ")         
        playerArray.append(playerName)
    gamesArray = generateGameCount(playerArray)
    print(gamesArray)



tournamentChoice = input("Create a new tournament or load an existing one? (new/load) " )
if tournamentChoice == "new":
    createNewTournament()
elif tournamentChoice == "load":
    exit()