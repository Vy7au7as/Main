class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None

    def print_board(self):
        for row in self.board:
            print("|".join(row))

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.check_win(row, col):
                self.winner = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self, row, col):
        row_vals = [self.board[row][c] for c in range(3)]
        col_vals = [self.board[r][col] for r in range(3)]
        diag1_vals = [self.board[i][i] for i in range(3)]
        diag2_vals = [self.board[i][2-i] for i in range(3)]
        all_vals = [row_vals, col_vals, diag1_vals, diag2_vals]
        return any([all(v == self.current_player for v in vals) for vals in all_vals])

    def play_game(self):
        while not self.winner:
            print(f"Žaidėjas {self.current_player}, įveskite eilutės ir stulpelio nr.nuo 1 iki 3 (su tarpu tarp sk.pvz.: 2 2):")
            try:
                row, col = [int(x) - 1 for x in input().split()]
            except ValueError:
                print("Įveskite du skaičius, su tarpu (space) tarp sk.")
                continue
            self.make_move(row, col)
            self.print_board()

        print(f"Žaidėjas {self.winner} laimėjo žaidimą!")


game = TicTacToe()
game.play_game()

my_list = [1, 2, 3]
index = 3

if index < len(my_list):
    print(my_list[index - 1])
else:
    print("Žaidimo pabaiga")
