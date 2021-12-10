from tkinter import *


class Game:
    win = "nimeni"

    def __init__(self, board, color_path, canvas):
        self.board_1 = board[0]
        self.board_2 = board[1]
        self.color = color_path
        self.canvas = canvas

    def show_board(self):
        self.image_1 = PhotoImage(file=self.color[0])
        for i in range(0, len(self.board_1)):  # nr de coloane
            print(len(self.board_1[i][0]))
            for j in range(0, len(self.board_1[i][0])):  # elementele din fiecare coloana
                btn = Button(text="", image=self.image_1, relief=FLAT, borderwidth=0)
                if i <= 11:
                    button1_window = self.canvas.create_window(self.board_1[i][1], self.board_1[i][2] + 65 * j,
                                                               window=btn)
                elif i > 11:
                    button1_window = self.canvas.create_window(self.board_1[i][1], self.board_1[i][2] - 65 * j,
                                                               window=btn)

        self.image_2 = PhotoImage(file=self.color[1])
        for i in range(0, len(self.board_2)):  # nr de coloane
            print(len(self.board_2[i][0]))
            for j in range(0, len(self.board_2[i][0])):  # elementele din fiecare coloana
                btn = Button(text="", image=self.image_2, relief=FLAT, borderwidth=0)
                if i <= 11:
                    button2_window = self.canvas.create_window(self.board_2[i][1], self.board_2[i][2] - 65 * j,
                                                               window=btn)
                elif i > 11:
                    button2_window = self.canvas.create_window(self.board_2[i][1], self.board_2[i][2] + 65 * j,
                                                               window=btn)

    def joc(self):
        turn = 1
        while self.win == "nimeni":
            if turn == 1:
                turn = 2
            else:
                turn = 1
