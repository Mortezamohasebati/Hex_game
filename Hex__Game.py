import math

class HexGame:
    def __init__(self, size=11):
        self.size = size
        self.board = [["." for _ in range(size)] for _ in range(size)]
        self.current_player = "X"

    def display_board(self):
        n = self.size

        print("\n      ", end="")
        for col in range(n):
            print(col, end=" ")
        print()

        print("     " + "O " * n)

        for i in range(n):
            print(" " * i, end="")
            print(f"{i} X ", end="")
            for j in range(n):
                print(self.board[i][j], end=" ")
            print("X")

        print(" " * (n + 5) + "O " * n)
        print()

    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.board[x][y] == "."

    def make_move(self, x, y):
        if self.is_valid_move(x, y):
            self.board[x][y] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_winner(self):
        def dfs(x, y, player, visited):
            if (player == "X" and y == self.size - 1) or (player == "O" and x == self.size - 1):
                return True

            visited.add((x, y))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if self.board[nx][ny] == player and (nx, ny) not in visited:
                        if dfs(nx, ny, player, visited):
                            return True
            return False

        for i in range(self.size):
            if self.board[i][0] == "X":
                if dfs(i, 0, "X", set()):
                    return "X"

        for j in range(self.size):
            if self.board[0][j] == "O":
                if dfs(0, j, "O", set()):
                    return "O"

        return None

    def evaluate_board(self, player):
        opponent = "X" if player == "O" else "O"
        player_count = sum(row.count(player) for row in self.board)
        opponent_count = sum(row.count(opponent) for row in self.board)
        return player_count - opponent_count

    def minimax(self, depth, is_maximizing, alpha, beta):
        winner = self.check_winner()
        if winner == "O":
            return 1000
        if winner == "X":
            return -1000
        if all(cell != "." for row in self.board for cell in row):
            return 0

        if depth == 0:
            return self.evaluate_board("O")

        if is_maximizing:
            max_eval = -math.inf
            for x in range(self.size):
                for y in range(self.size):
                    if self.is_valid_move(x, y):
                        self.board[x][y] = "O"
                        eval = self.minimax(depth - 1, False, alpha, beta)
                        self.board[x][y] = "."
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            return max_eval
            return max_eval
        else:
            min_eval = math.inf
            for x in range(self.size):
                for y in range(self.size):
                    if self.is_valid_move(x, y):
                        self.board[x][y] = "X"
                        eval = self.minimax(depth - 1, True, alpha, beta)
                        self.board[x][y] = "."
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            return min_eval
            return min_eval

    def find_best_move(self):
        best_value = -math.inf
        best_move = None
        for x in range(self.size):
            for y in range(self.size):
                if self.is_valid_move(x, y):
                    self.board[x][y] = "O"
                    move_value = self.minimax(3, False, -math.inf, math.inf)
                    self.board[x][y] = "."
                    if move_value > best_value:
                        best_value = move_value
                        best_move = (x, y)
        return best_move

    def play(self):
        print("Welcome to Hex!")
        print("X connects Left to Right")
        print("O connects Top to Bottom")
        self.display_board()

        while True:
            if self.current_player == "X":
                try:
                    x, y = map(int, input("Enter your move (row column): ").split())
                    if self.make_move(x, y):
                        self.display_board()
                        winner = self.check_winner()
                        if winner:
                            print(f"Player {winner} wins!")
                            break
                    else:
                        print("Invalid move.")
                except ValueError:
                    print("Invalid input.")
            else:
                move = self.find_best_move()
                if move:
                    self.make_move(*move)
                    print(f"Computer chose: {move[0]} {move[1]}")
                    self.display_board()
                    winner = self.check_winner()
                    if winner:
                        print(f"Player {winner} wins!")
                        break


if __name__ == "__main__":
    try:
        size = int(input("Enter board size: "))
        game = HexGame(size)
        game.play()
    except ValueError:
        print("Invalid size.")
