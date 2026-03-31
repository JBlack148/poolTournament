import json

# saves the current state of the tournament to a json file
def saveState(elo, games_to_play, games, gamesPerRound):
    state = {
        'elo': elo,
        'games_to_play': games_to_play,
        'games': games,
        'games_per_round': gamesPerRound
    }
    with open('tournament_state.json', 'w') as f:
        json.dump(state, f)

# loads the tournament state from a json file
def loadState():
    with open('tournament_state.json', 'r') as f:
        state = json.load(f)
    return state['elo'], state['games_to_play'], state['games'], state['games_per_round']