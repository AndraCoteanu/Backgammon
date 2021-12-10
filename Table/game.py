from tkinter import *


class Game:
    win = "nimeni"

    def __init__(self, board, color_path, canvas):
        self.board_1 = board[0]
        self.board_2 = board[1]
        self.color = color_path
        self.image = [PhotoImage(file=self.color[0]), PhotoImage(file=self.color[1])]
        self.canvas = canvas

    def show_player_board(self, id, color, board):
        poz = [[65, -65], [-65, 65]]

        for i in range(0, len(board)):  # nr de coloane
            for j in range(0, len(board[i][0])):  # elementele din fiecare coloana
                btn = Button(text="", image=self.image[id-1], relief=FLAT, borderwidth=0)
                if i <= 11:
                    button_window = self.canvas.create_window(board[i][1], board[i][2] + poz[id - 1][0] * j,
                                                              window=btn)
                elif i > 11:
                    button_window = self.canvas.create_window(board[i][1], board[i][2] + poz[id - 1][1] * j,
                                                              window=btn)

    def show_board(self):
        self.show_player_board(1, self.color[0], self.board_1)
        self.show_player_board(2, self.color[1], self.board_2)


    def joc(self):
        turn = 1
        while self.win == "nimeni":
            if turn == 1:
                turn = 2
            else:
                turn = 1
