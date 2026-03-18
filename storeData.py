import json

def save_state(elo, current_round, games):
    state = {
        'elo': elo,
        'current_round': current_round,
        'games': games
    }
    with open('tournament_state.json', 'w') as f:
        json.dump(state, f)

def load_state():
    with open('tournament_state.json', 'r') as f:
        state = json.load(f)
    return state['elo'], state['current_round'], state['games']