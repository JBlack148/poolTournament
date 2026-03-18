from roundRobin import *
from eloCount import *
from storeData import *

def createNewTournament():
    playerArray = []

    # get player count
    playerCount = int(input("How many players are playing? "))
    
    #populate player array with player names
    for i in range(playerCount):
        playerName = input("What is player " + str(i + 1) + "'s name? ")         
        playerArray.append(playerName)

    # generate games to play and initialize elo for all players
    gamesArray = generateGameCount(playerArray)
    eloDict = baseElo(playerArray)

    # loop through games and update elo after each game
    for i in range(len(gamesArray)):
        print(gamesArray[i][0] + " vs " + gamesArray[i][1])
        choice = input("Do you want to save and exit? (y/n) ")
        if choice == 'y':
            save_state(eloDict, i + 1, gamesArray)
            return
        winner = input("Who won? ")
        while winner != gamesArray[i][0] and winner != gamesArray[i][1]:
            winner = input("Please enter a valid player name. Who won? ")
        if winner == gamesArray[i][0]:
            eloDict = updateElo(gamesArray[i][0], gamesArray[i][1], eloDict)
        elif winner == gamesArray[i][1]:
            eloDict = updateElo(gamesArray[i][1], gamesArray[i][0], eloDict)



# main program
tournamentChoice = input("Create a new tournament or load an existing one? (new/load) " )
if tournamentChoice == "new":
    createNewTournament()
elif tournamentChoice == "load":
    eloDict, currentRound, gamesArray = load_state()
    for i in range(currentRound - 1, len(gamesArray)):
        print(gamesArray[i][0] + " vs " + gamesArray[i][1])
        winner = input("Who won? ")
        while winner != gamesArray[i][0] and winner != gamesArray[i][1]:
            winner = input("Please enter a valid player name. Who won? ")
        if winner == gamesArray[i][0]:
            eloDict = updateElo(gamesArray[i][0], gamesArray[i][1], eloDict)
        elif winner == gamesArray[i][1]:
            eloDict = updateElo(gamesArray[i][1], gamesArray[i][0], eloDict)
        save_state(eloDict, i + 1, gamesArray)