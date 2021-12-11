import random
import time
from tkinter import *
from tkinter import font


class Game:
    win = "nimeni"

    def __init__(self, board, color_path, canvas, type):
        self.board_1 = board[0]
        self.board_2 = board[1]
        self.color = color_path
        self.image = [PhotoImage(file=self.color[0]), PhotoImage(file=self.color[1])]
        self.canvas = canvas
        self.dice = []
        self.dice_img = [PhotoImage(), PhotoImage()]
        self.player_stats = [[0, 0], [0, 0]]
        self.player_stats_labels = [Label(), Label(), Label(), Label()]
        self.player1 = "Player 1"
        if type == "pc":
            self.player2 = "PC"
        else:
            self.player2 = "Player 2"

    def player_info(self):
        text_font = font.Font(size=17)

        player1 = Label(self.canvas, text=self.player1, fg='white', bg='#655f6a', font=text_font)
        self.canvas.create_window(60, 60, window=player1)

        player2 = Label(self.canvas, text=self.player2, fg='white', bg='#3c353b', font=text_font)
        self.canvas.create_window(1145, 60, window=player2)

        text_font = font.Font(size=11)

        player1 = Label(self.canvas, text='# piese\neliminate', fg='white', bg='#655f6a', font=text_font)
        self.canvas.create_window(40, 300, window=player1)

        player1 = Label(self.canvas, text='# piese\nscoase', fg='white', bg='#655f6a', font=text_font)
        self.canvas.create_window(40, 500, window=player1)

        player2 = Label(self.canvas, text='# piese\neliminate', fg='white', bg='#3c353b', font=text_font)
        self.canvas.create_window(1165, 300, window=player2)

        player2 = Label(self.canvas, text='# piese\nscoase', fg='white', bg='#3c353b', font=text_font)
        self.canvas.create_window(1165, 500, window=player2)

        self.canvas.create_image(60, 740, image=self.image[0])
        self.canvas.create_image(1145, 740, image=self.image[1])

        self.show_player_stats()

    def show_player_stats(self):
        text_font = font.Font(size=14)

        self.player_stats_labels[0].destroy()
        self.player_stats_labels[1].destroy()
        self.player_stats_labels[2].destroy()
        self.player_stats_labels[3].destroy()

        self.player_stats_labels[0] = Label(self.canvas, text=self.player_stats[0][0], fg='white', bg='#655f6a',
                                            font=text_font)
        self.canvas.create_window(40, 250, window=self.player_stats_labels[0])
        self.player_stats_labels[1] = Label(self.canvas, text=self.player_stats[0][1], fg='white', bg='#655f6a',
                                            font=text_font)
        self.canvas.create_window(40, 450, window=self.player_stats_labels[1])

        self.player_stats_labels[2] = Label(self.canvas, text=self.player_stats[1][0], fg='white', bg='#3c353b',
                                            font=text_font)
        self.canvas.create_window(1165, 250, window=self.player_stats_labels[2])
        self.player_stats_labels[3] = Label(self.canvas, text=self.player_stats[1][1], fg='white', bg='#3c353b',
                                            font=text_font)
        self.canvas.create_window(1165, 450, window=self.player_stats_labels[3])

    def show_player_board(self, id, color, board):
        poz = [[65, -65], [-65, 65]]

        for i in range(0, len(board)):  # nr de coloane
            for j in range(0, len(board[i][0])):  # elementele din fiecare coloana
                btn = Button(text="", image=self.image[id - 1], relief=FLAT, borderwidth=0)
                if i <= 11:
                    button_window = self.canvas.create_window(board[i][1], board[i][2] + poz[id - 1][0] * j,
                                                              window=btn)
                elif i > 11:
                    button_window = self.canvas.create_window(board[i][1], board[i][2] + poz[id - 1][1] * j,
                                                              window=btn)

    def show_board(self):
        self.show_player_board(1, self.color[0], self.board_1)
        self.show_player_board(2, self.color[1], self.board_2)
        self.player_info()
        text_font = font.Font(size=15)
        btn = Button(text="Roll", bg='#4e555f', fg='white', relief=FLAT, borderwidth=1, font=text_font,
                     command=lambda: self.roll_dice())
        button_window = self.canvas.create_window(380, 400, window=btn)

        self.show_player_stats()

    def roll_dice(self):
        zar1 = random.randrange(1, 7)
        zar2 = random.randrange(1, 7)
        self.dice = []
        if zar1 == zar2:
            self.dice.append(zar1)
            self.dice.append(zar1)
            self.dice.append(zar1)
            self.dice.append(zar1)
        else:
            self.dice.append(zar1)
            self.dice.append(zar2)

        self.canvas.delete(self.dice_img[0])
        self.canvas.delete(self.dice_img[1])

        path = "assets/dice" + str(zar1) + ".png"
        self.dice_img[0] = PhotoImage(file=path)
        self.canvas.create_image(800, 400, image=self.dice_img[0])

        path = "assets/dice" + str(zar2) + ".png"
        self.dice_img[1] = PhotoImage(file=path)
        self.canvas.create_image(850, 400, image=self.dice_img[1])

    def joc(self):
        turn = 1
        while self.win == "nimeni":
            if turn == 1:
                self.show_player_stats()
                turn = 2
            else:
                self.show_player_stats()
                turn = 1
