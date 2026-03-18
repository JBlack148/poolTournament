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
        # if user wants to save and exit, save the current state and exit the program
        if choice == 'y':
            saveState(eloDict, i + 1, gamesArray)
            return
        winner = input("Who won? ")
        while winner != gamesArray[i][0] and winner != gamesArray[i][1]:
            winner = input("Please enter a valid player name. Who won? ")
        if winner == gamesArray[i][0]:
            eloDict = updateElo(gamesArray[i][0], gamesArray[i][1], eloDict)
        elif winner == gamesArray[i][1]:
            eloDict = updateElo(gamesArray[i][1], gamesArray[i][0], eloDict)
    tournamentFinished(eloDict)

def loadTournament():
    eloDict, currentRound, gamesArray = loadState()
    for i in range(currentRound - 1, len(gamesArray)):
        print(gamesArray[i][0] + " vs " + gamesArray[i][1])
        choice = input("Do you want to save and exit? (y/n) ")
        # if user wants to save and exit, save the current state and exit the program
        if choice == 'y':
            saveState(eloDict, i + 1, gamesArray)
            return
        winner = input("Who won? ")
        while winner != gamesArray[i][0] and winner != gamesArray[i][1]:
            winner = input("Please enter a valid player name. Who won? ")
        if winner == gamesArray[i][0]:
            eloDict = updateElo(gamesArray[i][0], gamesArray[i][1], eloDict)
        elif winner == gamesArray[i][1]:
            eloDict = updateElo(gamesArray[i][1], gamesArray[i][0], eloDict)
    tournamentFinished(eloDict)

def tournamentFinished(eloDict):
    print("Tournament finished! The winner is " 
          + max(eloDict, key=eloDict.get) 
          + " with an Elo rating of " 
          + str(round(max(eloDict.values()))) + ".")
    print("Final Elo ratings:")
    sortedElo = sorted(eloDict.items(), key=lambda item: item[1], reverse=True)
    for player, elo in sortedElo:
        print(player + ": " + str(round(elo)))



# main program
tournamentChoice = input("Create a new tournament or load an existing one? (new/load) " )
if tournamentChoice == "new":
    # create a new tournament
    createNewTournament()
elif tournamentChoice == "load":
    loadTournament()