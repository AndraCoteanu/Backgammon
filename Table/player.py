import random
from typing import List
import tkinter as tk
from tkinter import font


class Player:
    def __init__(self, main_frame, jucator1, jucator2) -> None:
        self.name = [jucator1, jucator2]
        self.stats = [[0, 0], [0, 10]]
        self.color = self.color_choosing()
        self.label_list = self.show_player_info(main_frame, self.name, self.color)
        self.show_player_stats(main_frame, self.stats)
        self.board = self.init_board(main_frame, self.color)

    def show_player_info(self, main_frame, player, color):
        label_id = 0
        label_mini_list: List[tk.Label] = []

        text_font = font.Font(size=17)

        label_mini_list.append(tk.Label(main_frame, text=player[0], fg='white', bg='#655f6a', font=text_font))
        label_mini_list[label_id].place(x=15, y=50)
        label_id += 1

        label_mini_list.append(tk.Label(main_frame, text=player[1], fg='white', bg='#3c353b', font=text_font))
        label_mini_list[label_id].place(x=1100, y=50)
        label_id += 1

        text_font = font.Font(size=11)

        label_mini_list.append(
            tk.Label(main_frame, text='# piese\neliminate', fg='white', bg='#655f6a', font=text_font))
        label_mini_list[label_id].place(x=5, y=300)
        label_id += 1

        label_mini_list.append(tk.Label(main_frame, text='# piese\nscoase', fg='white', bg='#655f6a', font=text_font))
        label_mini_list[label_id].place(x=10, y=500)
        label_id += 1

        label_mini_list.append(
            tk.Label(main_frame, text='# piese\neliminate', fg='white', bg='#3c353b', font=text_font))
        label_mini_list[label_id].place(x=1125, y=300)
        label_id += 1

        label_mini_list.append(tk.Label(main_frame, text='# piese\nscoase', fg='white', bg='#3c353b', font=text_font))
        label_mini_list[label_id].place(x=1125, y=500)
        label_id += 1

        global image1
        image1 = tk.PhotoImage(file=color[0])
        label_mini_list.append(tk.Label(main_frame, image=image1, bg=None))
        label_mini_list[label_id].place(x=25, y=700)
        label_id += 1

        global image2
        image2 = tk.PhotoImage(file=color[1])
        label_mini_list.append(tk.Label(main_frame, image=image2, bg=None))
        label_mini_list[label_id].place(x=1110, y=700)
        label_id += 1

        return label_mini_list

    def show_player_stats(self, main_frame, player_stats):
        stats_label_list: List[tk.Label] = []
        stats_label_id = 0

        n = len(stats_label_list)
        if n > 0:
            for index in range(0, n + 1):
                stats_label_list[index].destroy()

        text_font = font.Font(size=14)

        # pentru player 1:

        stats_label_list.append(tk.Label(main_frame, text=player_stats[0][0], fg='white', bg='#655f6a',
                                         font=text_font))
        stats_label_list[stats_label_id].place(x=30, y=250)
        stats_label_id += 1

        stats_label_list.append(tk.Label(main_frame, text=player_stats[0][1], fg='white', bg='#655f6a',
                                         font=text_font))
        stats_label_list[stats_label_id].place(x=30, y=450)
        stats_label_id += 1

        # pentru player 2:

        stats_label_list.append(tk.Label(main_frame, text=player_stats[1][0], fg='white', bg='#3c353b',
                                         font=text_font))
        stats_label_list[stats_label_id].place(x=1150, y=250)
        stats_label_id += 1

        stats_label_list.append(tk.Label(main_frame, text=player_stats[1][1], fg='white', bg='#3c353b',
                                         font=text_font))
        stats_label_list[stats_label_id].place(x=1150, y=450)
        stats_label_id += 1

    def color_choosing(self):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        while b == a or (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
            b = random.randint(1, 9)

        if a == 1:
            path_a = "assets/blue.png"
        elif a == 2:
            path_a = "assets/light-blue.png"
        elif a == 3:
            path_a = "assets/grey.png"
        elif a == 4:
            path_a = "assets/black.png"
        elif a == 5:
            path_a = "assets/brown.png"
        elif a == 6:
            path_a = "assets/green.png"
        elif a == 7:
            path_a = "assets/purple.png"
        elif a == 8:
            path_a = "assets/red.png"
        else:
            path_a = "assets/white.png"

        if b == 1:
            path_b = "assets/blue.png"
        elif b == 2:
            path_b = "assets/light-blue.png"
        elif b == 3:
            path_b = "assets/grey.png"
        elif b == 4:
            path_b = "assets/black.png"
        elif b == 5:
            path_b = "assets/brown.png"
        elif b == 6:
            path_b = "assets/green.png"
        elif b == 7:
            path_b = "assets/purple.png"
        elif b == 8:
            path_b = "assets/red.png"
        else:
            path_b = "assets/white.png"

        color_path = [path_a, path_b]
        return color_path

    def init_board_player(self, main_frame, piece, coord_a, coord_b, poz):
        # de retinut !! maxim 350 pixeli dimensiunea pentru o coloana
        board_player = []
        # un element din board = o coloana pe tabla, o coloana are lista de elemente, coord x si coord y pentru primul element
        # as fi putut sa fac o clasa pentru tabla si init_board() sa fie defapt constructorul, dar am vrut sa fie ceva mai unic =))
        coloana = [[], 970, coord_a]
        board_player.append(coloana)
        coloana = [[], 900, coord_a]
        board_player.append(coloana)
        coloana = [[], 830, coord_a]
        board_player.append(coloana)
        coloana = [[], 760, coord_a]
        board_player.append(coloana)
        coloana = [[], 690, coord_a]
        board_player.append(coloana)
        coloana = [[], 620, coord_a]
        board_player.append(coloana)
        coloana = [[], 525, coord_a]
        board_player.append(coloana)
        coloana = [[], 455, coord_a]
        board_player.append(coloana)
        coloana = [[], 385, coord_a]
        board_player.append(coloana)
        coloana = [[], 315, coord_a]
        board_player.append(coloana)
        coloana = [[], 245, coord_a]
        board_player.append(coloana)
        coloana = [[], 170, coord_a]
        board_player.append(coloana)
        coloana = [[], 170, coord_b]
        board_player.append(coloana)
        coloana = [[], 245, coord_b]
        board_player.append(coloana)
        coloana = [[], 315, coord_b]
        board_player.append(coloana)
        coloana = [[], 385, coord_b]
        board_player.append(coloana)
        coloana = [[], 455, coord_b]
        board_player.append(coloana)
        coloana = [[], 525, coord_b]
        board_player.append(coloana)
        coloana = [[], 620, coord_b]
        board_player.append(coloana)
        coloana = [[], 690, coord_b]
        board_player.append(coloana)
        coloana = [[], 760, coord_b]
        board_player.append(coloana)
        coloana = [[], 830, coord_b]
        board_player.append(coloana)
        coloana = [[], 900, coord_b]
        board_player.append(coloana)
        coloana = [[], 970, coord_b]
        board_player.append(coloana)

        board_player[5][0].append(tk.Button(main_frame, image=piece))
        board_player[5][0].append(tk.Button(main_frame, image=piece))
        board_player[5][0].append(tk.Button(main_frame, image=piece))
        board_player[5][0].append(tk.Button(main_frame, image=piece))
        board_player[5][0].append(tk.Button(main_frame, image=piece))

        board_player[7][0].append(tk.Button(main_frame, image=piece))
        board_player[7][0].append(tk.Button(main_frame, image=piece))
        board_player[7][0].append(tk.Button(main_frame, image=piece))

        board_player[12][0].append(tk.Button(main_frame, image=piece))
        board_player[12][0].append(tk.Button(main_frame, image=piece))
        board_player[12][0].append(tk.Button(main_frame, image=piece))
        board_player[12][0].append(tk.Button(main_frame, image=piece))
        board_player[12][0].append(tk.Button(main_frame, image=piece))

        board_player[23][0].append(tk.Button(main_frame, image=piece))
        board_player[23][0].append(tk.Button(main_frame, image=piece))

        for i in range(0, len(board_player)):  # nr de coloane
            for j in range(0, len(board_player[i][0])):  # elementele din fiecare coloana
                if i <= 11:
                    board_player[i][0][j].place(x=board_player[i][1], y=(board_player[i][2] + poz[0] * j))
                elif i > 11:
                    board_player[i][0][j].place(x=board_player[i][1], y=(board_player[i][2] + poz[1] * j))

    def init_board(self, main_frame, color):
        global piece_1
        piece_1 = tk.PhotoImage(file=color[0])
        global piece_2
        piece_2 = tk.PhotoImage(file=color[1])

        board_1 = self.init_board_player(main_frame, piece_1, 15, 730, [65, -65])
        board_2 = self.init_board_player(main_frame, piece_2, 730, 15, [-65, 65])

        board = [board_1, board_2]
        return board
