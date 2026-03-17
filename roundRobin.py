def generateGameCount(players):
    # generate all possible games for a round robin tournament
    gamesArray = []
    for i in range(len(players)):
        for j in range(len(players)):
            if i != j and (players[j], players[i]) not in gamesArray:
                gamesArray.append((players[i], players[j]))
    return gamesArray
