from roundRobin import *
    
        
def createNewTournament():
    playerArray = []
    playerCount = int(input("How many players are playing? "))
        
    for i in range(playerCount):
        playerName = input("What is player " + str(i + 1) + "'s name? ")         
        playerArray.append(playerName)
    gamesArray = generateGameCount(playerArray)
    for i in range(len(gamesArray)):
        print(gamesArray[i][0] + " vs " + gamesArray[i][1])
        winner = input("Who won? ")
        while winner != gamesArray[i][0] and winner != gamesArray[i][1]:
            winner = input("Please enter a valid player name. Who won? ")
        if winner == gamesArray[i][0]:
            exit()
        elif winner == gamesArray[i][1]:
            exit()



tournamentChoice = input("Create a new tournament or load an existing one? (new/load) " )
if tournamentChoice == "new":
    createNewTournament()
elif tournamentChoice == "load":
    exit()