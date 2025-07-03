import tkinter as tk
from tkinter import messagebox
import copy

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe - Unbeatable")
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text=" ", font=('normal', 40), width=5, height=2, command=lambda i=i, j=j: self.player_move(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def player_move(self, i, j):
        if self.board[i][j] == " ":
            self.board[i][j] = 'X'
            self.buttons[i][j].config(text='X')
            if self.check_winner(self.board, 'X'):
                messagebox.showinfo("Result", "You won!")
                self.reset_board()
                return
            elif self.is_board_full(self.board):
                messagebox.showinfo("Result", "It's a tie!")
                self.reset_board()
                return
            self.computer_move()

    def computer_move(self):
        move = self.find_best_move()
        if move:
            i, j = move
            self.board[i][j] = 'O'
            self.buttons[i][j].config(text='O')
            if self.check_winner(self.board, 'O'):
                messagebox.showinfo("Result", "Computer won!")
                self.reset_board()
            elif self.is_board_full(self.board):
                messagebox.showinfo("Result", "It's a tie!")
                self.reset_board()

    def check_winner(self, board, player):
        for row in board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_board_full(self, board):
        return all(cell != " " for row in board for cell in row)

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(board, 'O'):
            return 1
        if self.check_winner(board, 'X'):
            return -1
        if self.is_board_full(board):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = " "
                        best_score = min(score, best_score)
            return best_score

    def find_best_move(self):
        best_score = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
