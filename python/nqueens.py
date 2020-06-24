
class nqueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for i in range (0, n+1)]
        # tuples of placed queen pieces (row, col)
        self.currentRow = 0
        self.colPlacements = set()
        self.solution = set()
    # recursive backtracking approach

    def validate(self, guess):
        for placed in self.colPlacements:
            diff = abs(guess[1] - placed[1])
            # same column or on same diagonal
            if (diff == 0 or diff == (abs(placed[0]-self.currentRow))):
                return False
        return True

    def solve(self):
        if (len(self.colPlacements) == self.n):
            # done placing n queens
            self.solution = set(self.colPlacements)
            return
        else: 
            # try placement
            for c in range (0, self.n):
                guess = (self.currentRow, c)
                if self.validate(guess):
                    self.colPlacements.add(guess)
                    self.currentRow += 1
                    self.solve()
                    self.colPlacements.remove(guess)
                    self.currentRow -= 1
            return

game = nqueens(12)
game.solve()
print(game.solution)
