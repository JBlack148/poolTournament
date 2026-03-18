import json

def saveState(elo, current_round, games):
    state = {
        'elo': elo,
        'current_round': current_round,
        'games': games
    }
    with open('tournament_state.json', 'w') as f:
        json.dump(state, f)

def loadState():
    with open('tournament_state.json', 'r') as f:
        state = json.load(f)
    return state['elo'], state['current_round'], state['games']