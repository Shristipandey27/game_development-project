import tkinter as tk
from itertools import cycle

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        
        # Turn label
        self.turn_label = tk.Label(self.root, text=f"Player {self.current_player}'s turn", 
                                  font=("Arial", 16))
        self.turn_label.grid(row=0, column=0, columnspan=3)
        
        # Create buttons grid
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda r=i, c=j: self.make_move(r, c)
                )
                btn.grid(row=i+1, column=j)
                row.append(btn)
            self.buttons.append(row)

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.game_over:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            # Update turn label
            self.turn_label.config(text=f"Player {self.current_player}'s turn")
            
            # Check win condition
            if self.check_win():
                self.highlight_winner()
                self.game_over = True
                self.turn_label.config(text=f"Player {self.current_player} wins!")
            elif all(all(cell != "" for cell in row) for row in self.board):
                # Draw
                self.turn_label.config(text="Game Over - Draw!")
            else:
                # Switch players
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Player {self.current_player}'s turn")

    def check_win(self):
        # Check rows
        for row in self.board:
            if len(set(row)) == 1 and row[0] != "":
                return True
                
        # Check columns
        for col in zip(*self.board):
            if len(set(col)) == 1 and col[0] != "":
                return True
                
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
            
        return False

    def highlight_winner(self):
        # Find winning cells
        win_cells = []
        
        # Check rows
        for i, row in enumerate(self.board):
            if len(set(row)) == 1 and row[0] != "":
                win_cells.extend([(i, j) for j in range(3)])
                
        # Check columns
        for j, col in enumerate(zip(*self.board)):
            if len(set(col)) == 1 and col[0] != "":
                win_cells.extend([(i, j) for i in range(3)])
                
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            win_cells.extend([(0,0), (1,1), (2,2)])
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            win_cells.extend([(0,2), (1,1), (2,0)])
            
        # Highlight cells
        for row, col in win_cells:
            self.buttons[row][col].config(bg="green")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()