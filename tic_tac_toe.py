import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 0-8
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

def minimax(state, player, maximizing_player):
    max_player = maximizing_player  # AI
    other_player = 'O' if player == 'X' else 'X'

    if state.current_winner == other_player:
        return {'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
    elif not state.empty_squares():
        return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -float('inf')}
    else:
        best = {'position': None, 'score': float('inf')}

    for possible_move in state.available_moves():
        state.make_move(possible_move, player)
        sim_score = minimax(state, other_player, maximizing_player)

        state.board[possible_move] = ' '
        state.current_winner = None
        sim_score['position'] = possible_move

        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score

    return best

def minimax_alpha_beta(state, player, maximizing_player, alpha=-float('inf'), beta=float('inf')):
    max_player = maximizing_player
    other_player = 'O' if player == 'X' else 'X'

    if state.current_winner == other_player:
        return {'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
    elif not state.empty_squares():
        return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -float('inf')}
    else:
        best = {'position': None, 'score': float('inf')}

    for possible_move in state.available_moves():
        state.make_move(possible_move, player)
        sim_score = minimax_alpha_beta(state, other_player, maximizing_player, alpha, beta)

        state.board[possible_move] = ' '
        state.current_winner = None
        sim_score['position'] = possible_move

        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
            alpha = max(alpha, sim_score['score'])
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
            beta = min(beta, sim_score['score'])

        if beta <= alpha:
            break

    return best

def play_game(use_alpha_beta=False):
    game = TicTacToe()
    game.print_board()

    letter = 'X'  # starting letter
    while game.empty_squares():
        if letter == 'O':
            square = int(input('Your move (0-8): '))
            if game.make_move(square, letter):
                if game.current_winner:
                    print(f'{letter} wins!')
                    break
                letter = 'X'
            else:
                print('Invalid move. Try again.')
        else:
            print('AI is thinking...')
            start = time.time()
            if use_alpha_beta:
                move = minimax_alpha_beta(game, 'X', 'X')['position']
            else:
                move = minimax(game, 'X', 'X')['position']
            end = time.time()
            print(f"AI took {end - start:.5f} seconds.")
            game.make_move(move, 'X')
            if game.current_winner:
                print(f'{letter} wins!')
                break
            letter = 'O'

        game.print_board()

    if not game.current_winner:
        print('It\'s a tie!')

if __name__ == '__main__':
    print("Tic-Tac-Toe Game")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8\n")
    mode = input("Use Alpha-Beta Pruning? (y/n): ")
    use_alpha_beta = mode.lower() == 'y'
    play_game(use_alpha_beta)
