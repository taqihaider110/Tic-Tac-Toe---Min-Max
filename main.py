from game import TicTacToe
from minimax import minimax, minimax_alpha_beta
import time

def play_game(use_alpha_beta):
    game = TicTacToe()
    player_letter = 'O'
    ai_letter = 'X'

    game.print_board()

    while game.empty_squares():
        # Human move
        move = int(input('Enter your move (0-8): '))
        if move not in game.available_moves():
            print('Invalid move. Try again.')
            continue
        game.make_move(move, player_letter)
        game.print_board()

        if game.winner(move, player_letter):
            print('You win!')
            return
        if not game.empty_squares():
            print('It\'s a tie!')
            return

        # AI move
        print('AI is thinking...')
        start = time.time()

        if use_alpha_beta:
            move_data = minimax_alpha_beta(game, ai_letter, ai_letter)
        else:
            move_data = minimax(game, ai_letter, ai_letter)

        end = time.time()

        game.make_move(move_data['position'], ai_letter)
        print(f'AI moved to {move_data["position"]}')
        game.print_board()
        print(f'AI took {end - start:.5f} seconds.')

        if game.winner(move_data['position'], ai_letter):
            print('AI wins!')
            return
        if not game.empty_squares():
            print('It\'s a tie!')
            return

if __name__ == '__main__':
    print('Tic-Tac-Toe Game')
    print('0 | 1 | 2')
    print('3 | 4 | 5')
    print('6 | 7 | 8')
    use_alpha_beta = input('Use Alpha-Beta Pruning? (y/n): ').lower() == 'y'
    play_game(use_alpha_beta)
