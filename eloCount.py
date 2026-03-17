# elo constants
BASE_ELO = 1000
K = 32

def baseElo(Players):
    # initialize elo for all players
    eloDict = {}
    for player in Players:
        eloDict[player] = BASE_ELO
    return eloDict

def updateElo(winner, loser, eloDict):
    # update elo for winner and loser using a simplified version of the Elo rating system
    winnerElo = eloDict[winner]
    loserElo = eloDict[loser]

    expectedWinner = 1 / (1 + 10 ** ((loserElo - winnerElo) / 400))
    expectedLoser = 1 / (1 + 10 ** ((winnerElo - loserElo) / 400))

    eloDict[winner] = winnerElo + K * (1 - expectedWinner)
    eloDict[loser] = loserElo + K * (0 - expectedLoser)

    return eloDict