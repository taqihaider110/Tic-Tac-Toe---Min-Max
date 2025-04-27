class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            return True
        return False

    def winner(self, square, letter):
        """
        Check if current move leads to a win (based on last move position).
        Used during actual game moves.
        """
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
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        
        return False

    def check_winner(self, letter):
        """
        Check if a given player has won by scanning the full board.
        Used during Minimax simulation (no 'last move' available).
        """
        # Check rows
        for i in range(3):
            if all([self.board[j] == letter for j in range(i*3, (i+1)*3)]):
                return True
        
        # Check columns
        for i in range(3):
            if all([self.board[i+j*3] == letter for j in range(3)]):
                return True

        # Check diagonals
        if all([self.board[i] == letter for i in [0, 4, 8]]):
            return True
        if all([self.board[i] == letter for i in [2, 4, 6]]):
            return True

        return False
