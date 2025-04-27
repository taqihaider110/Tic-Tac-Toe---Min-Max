import math

def minimax(board, player, maximizing_player):
    max_player = 'X'
    other_player = 'O' if player == 'X' else 'X'

    # ✅ Correct checking using full-board check_winner, not by index!
    if board.check_winner(max_player):
        return {'position': None, 'score': 1}  # Maximizing player wins
    elif board.check_winner(other_player):
        return {'position': None, 'score': -1}  # Minimizing player wins
    elif not board.empty_squares():
        return {'position': None, 'score': 0}  # Draw

    if player == maximizing_player:
        best = {'position': None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}

    for possible_move in board.available_moves():
        board.make_move(possible_move, player)
        sim_score = minimax(board, other_player, maximizing_player)

        board.board[possible_move] = ' '  # Undo move
        sim_score['position'] = possible_move

        if player == maximizing_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score

    return best

def minimax_alpha_beta(board, player, maximizing_player, alpha=-math.inf, beta=math.inf):
    max_player = 'X'
    other_player = 'O' if player == 'X' else 'X'

    # ✅ Correct checking using full-board check_winner, not by index!
    if board.check_winner(max_player):
        return {'position': None, 'score': 1}
    elif board.check_winner(other_player):
        return {'position': None, 'score': -1}
    elif not board.empty_squares():
        return {'position': None, 'score': 0}

    if player == maximizing_player:
        best = {'position': None, 'score': -math.inf}
        for possible_move in board.available_moves():
            board.make_move(possible_move, player)
            sim_score = minimax_alpha_beta(board, other_player, maximizing_player, alpha, beta)

            board.board[possible_move] = ' '  # Undo move
            sim_score['position'] = possible_move

            if sim_score['score'] > best['score']:
                best = sim_score

            alpha = max(alpha, sim_score['score'])
            if beta <= alpha:
                break
    else:
        best = {'position': None, 'score': math.inf}
        for possible_move in board.available_moves():
            board.make_move(possible_move, player)
            sim_score = minimax_alpha_beta(board, other_player, maximizing_player, alpha, beta)

            board.board[possible_move] = ' '  # Undo move
            sim_score['position'] = possible_move

            if sim_score['score'] < best['score']:
                best = sim_score

            beta = min(beta, sim_score['score'])
            if beta <= alpha:
                break

    return best
