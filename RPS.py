# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_order={}):
    if prev_play:
        opponent_history.append(prev_play)

    
    if len(opponent_history) < 3:
        return "R"


    pattern = "".join(opponent_history[-3:])


    if len(opponent_history) > 3:
        key = "".join(opponent_history[-4:-1])
        next_move = opponent_history[-1]
        if key in play_order:
            if next_move in play_order[key]:
                play_order[key][next_move] += 1
            else:
                play_order[key][next_move] = 1
        else:
            play_order[key] = {next_move: 1}

    guess = "R"
    if pattern in play_order:
        possible_moves = play_order[pattern]
        prediction = max(possible_moves, key=possible_moves.get)

        counter_moves = {"R": "P", "P": "S", "S": "R"}
        guess = counter_moves[prediction]

    return guess
