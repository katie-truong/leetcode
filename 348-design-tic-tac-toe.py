class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antiDiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        val = 1 if player == 1 else -1
        
        self.rows[row] += val
        self.cols[col] += val
        
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n:
            return player
        
        if row == col:
            self.diagonal += val
            if abs(self.diagonal) == self.n:
                return player
            
        if (self.n - 1 - row) == col:
            self.antiDiagonal += val
            if abs(self.antiDiagonal) == self.n:
                return player

        return 0
