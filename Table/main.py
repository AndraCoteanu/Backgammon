import random
import time
import webbrowser
import tkinter as tk
from tkinter import font, CENTER, messagebox
from typing import List

# TO DO: adauga comentarii si ctrl+alt+l

# 0 = jucator 1; 1 = jucator 2 / pc
turn = 0
dice = []
piece_image = []
list_btn_option = []
stats_label_list = []
dice_image = []
global label_mini_list
global roll_button


class Player:
    def __init__(self, window, main_frame, jucator1, jucator2) -> None:
        self.clicked = []
        self.window = window
        self.main_frame = main_frame
        self.name = [jucator1, jucator2]
        self.stats = [[0, 0], [0, 0]]
        self.color = self.color_choosing()
        self.label_list = self.show_player_info(main_frame, self.name, self.color)
        self.show_player_stats(main_frame, self.stats)
        self.board = self.init_board(main_frame, self.color)

    def show_player_info(self, main_frame, player, color):
        label_id = 0
        global label_mini_list
        label_mini_list = []

        text_font = font.Font(size=17)

        label_mini_list.append(tk.Label(main_frame, text=player[0], fg='#80ff80', bg='#655f6a', font=text_font))
        label_mini_list[label_id].place(x=15, y=50)
        label_id += 1

        label_mini_list.append(tk.Label(main_frame, text=player[1], fg='white', bg='#3c353b', font=text_font))
        if player[1] == "player 2":
            label_mini_list[label_id].place(x=1100, y=50)
        else:
            label_mini_list[label_id].place(x=1130, y=50)
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

        global piece_image
        piece_image = [image1, image2]

        return label_mini_list

    def show_player_stats(self, main_frame, player_stats):
        global stats_label_list
        stats_label_id = 0

        n = len(stats_label_list)
        if n > 0:
            for label in stats_label_list:
                label.destroy()
            for index in range(0, len(stats_label_list)):
                stats_label_list.pop()

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

    def init_board_player(self, main_frame, piece, coord_a, coord_b, poz, jucator):
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

        board_player[5][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 5, 0)))
        board_player[5][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 5, 1)))
        board_player[5][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 5, 2)))
        board_player[5][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 5, 3)))
        board_player[5][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 5, 4)))

        board_player[7][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 7, 0)))
        board_player[7][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 7, 1)))
        board_player[7][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 7, 2)))

        board_player[12][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 12, 0)))
        board_player[12][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 12, 1)))
        board_player[12][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 12, 2)))
        board_player[12][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 12, 3)))
        board_player[12][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 12, 4)))

        board_player[23][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 23, 0)))
        board_player[23][0].append(tk.Button(main_frame, image=piece, command=lambda: self.move(jucator, 23, 1)))

        for i in range(0, len(board_player)):  # nr de coloane
            for j in range(0, len(board_player[i][0])):  # elementele din fiecare coloana
                if i <= 11:
                    board_player[i][0][j].place(x=board_player[i][1], y=(board_player[i][2] + poz[0] * j))
                elif i > 11:
                    board_player[i][0][j].place(x=board_player[i][1], y=(board_player[i][2] + poz[1] * j))

        return board_player

    def init_board(self, main_frame, color):
        global piece_1
        piece_1 = tk.PhotoImage(file=color[0])
        global piece_2
        piece_2 = tk.PhotoImage(file=color[1])

        board_1 = self.init_board_player(main_frame, piece_image[0], 15, 730, [65, -65], jucator=0)
        board_2 = self.init_board_player(main_frame, piece_image[1], 730, 15, [-65, 65], jucator=1)

        board = []
        board.append(board_1)
        board.append(board_2)
        return board

    def replace_piece(self, coloana, id_coloana, type):
        global turn
        if type == 0:
            if turn == 1:
                poz_id = [-1, 1]
            else:
                poz_id = [1, -1]

            dist = 350 / len(coloana[0])

            poz_id[0] *= dist
            poz_id[1] *= dist

            print("REARANJEZ")

            for index in range(0, len(coloana[0])):
                if id_coloana <= 11:
                    coloana[0][index].place(x=coloana[1], y=(coloana[2] + poz_id[0] * index))
                elif id_coloana > 11:
                    coloana[0][index].place(x=coloana[1], y=(coloana[2] + poz_id[1] * index))
        elif type == 1:
            if turn == 1:
                poz_id = [-65, 65]
            else:
                poz_id = [65, -65]
            print("REARANJEZ")

            for index in range(0, len(coloana[0])):
                if id_coloana <= 11:
                    coloana[0][index].place(x=coloana[1], y=(coloana[2] + poz_id[0] * index))
                elif id_coloana > 11:
                    coloana[0][index].place(x=coloana[1], y=(coloana[2] + poz_id[1] * index))

    def exist_move(self, jucator):
        print("sunt deci exist")
        if jucator == 1:
            oponent = 0
        else:
            oponent =1
        count = 0
        if self.all_in_house(jucator) == False:
            if len(dice) > 0:
                count = 0
                for zar in dice:
                    for index in range(0, 24):
                        if len(self.board[jucator][index][0]) > 0:
                            coloana = index-zar
                            if coloana>=0 and coloana<24 and len(self.board[oponent][23-coloana][0]) < 2:
                                count += 1
                                break
                    if count != 0:
                        break
        else:
            if len(dice) > 0:
                count = 0
                for index in range(0, len(self.board[jucator])):
                    pos = self.end_piece_life(jucator, index, 0)
                    if len(pos) > 0:
                        count += 1

        if count == 0:
            return False
        else:
            return True

    def all_in_house(self, jucator):
        count = 0
        if self.stats[jucator][0] == 0:
            for column in range(6, 24):
                count += len(self.board[jucator][column][0])
        if count == 0:
            return True
        else:
            return False

    def end_piece_life(self, jucator, x, y):
        next_pos = []
        if jucator == 0:
            if len(dice) == 2:
                for index in range(0, len(dice)):
                    column = x - dice[index]
                    if column < 12:
                        coord_y = 15
                    else:
                        coord_y = 730

                    coord = 23 - column
                    if coord >= 0 and coord <= 23:
                        if len(self.board[1][coord][0]) < 2 and column >= 0:
                            next_pos.append([column, coord_y])
                    elif column < 0:
                        verif_last_column = 1
                        if column == -1:
                            next_pos.append([-5, 0])
                        else:
                            for i in range(0, 6):
                                if len(self.board[jucator][i][0]) > 0:
                                    dist = i - dice[index]
                                    if dist < 0 and dist > column:
                                        verif_last_column = 0
                                    elif dist >= 0:
                                        verif_last_column = 0

                            if verif_last_column == 1:
                                next_pos.append([-5, 0])
            else:
                column = x - dice[0]
                if column < 12:
                    coord_y = 15
                else:
                    coord_y = 730

                coord = 23 - column
                if coord >= 0 and coord <= 23:
                    if len(self.board[1][coord][0]) < 2 and column >= 0:
                        next_pos.append([column, coord_y])
                elif column < 0:
                    verif_last_column = 1
                    if column == -1:
                        next_pos.append([-5, 0])
                    else:
                        for i in range(0, 6):
                            if len(self.board[jucator][i][0]) > 0:
                                dist = i - dice[0]
                                if dist < 0 and dist > column:
                                    verif_last_column = 0
                                elif dist >= 0:
                                    verif_last_column = 0

                        if verif_last_column == 1:
                            next_pos.append([-5, 0])
        else:
            if len(dice) == 2:
                for index in range(0, len(dice)):
                    column = x - dice[index]
                    if column < 12:
                        coord_y = 730
                    else:
                        coord_y = 15

                    coord = 23 - column
                    if coord >= 0 and coord <= 23:
                        if len(self.board[0][coord][0]) < 2 and column >= 0:
                            next_pos.append([column, coord_y])
                    elif column < 0:
                        verif_last_column = 1
                        if column == -1:
                            next_pos.append([-5, 0])
                        else:
                            for i in range(0, 6):
                                if len(self.board[jucator][i][0]) > 0:
                                    dist = i - dice[index]
                                    if dist < 0 and dist > column:
                                        verif_last_column = 0
                                    elif dist >= 0:
                                        verif_last_column = 0

                            if verif_last_column == 1:
                                next_pos.append([-5, 0])

            else:
                column = x - dice[0]
                if column < 12:
                    coord_y = 730
                else:
                    coord_y = 15

                coord = 23 - column
                if coord >= 0 and coord <= 23:
                    if len(self.board[0][coord][0]) < 2 and column >= 0:
                        next_pos.append([column, coord_y])
                elif column < 0:
                    verif_last_column = 1
                    if column == -1:
                        next_pos.append([-5, 0])
                    else:
                        for i in range(0, 6):
                            if len(self.board[jucator][i][0]) > 0:
                                dist = i - dice[0]
                                if dist < 0 and dist > column:
                                    verif_last_column = 0
                                elif dist >= 0:
                                    verif_last_column = 0

                        if verif_last_column == 1:
                            next_pos.append([-5, 0])

        if len(next_pos) == 0 and y > 0 and self.name[jucator] != "PC":
            messagebox.showerror("Backgammon!!", "You don't have where to move this piece")

        return next_pos

    def piece_next_place(self, jucator, x, y):
        next_pos = []
        if jucator == 0:
            if len(dice) == 2:
                for index in range(0, len(dice)):
                    column = x - dice[index]
                    if column < 12:
                        coord_y = 15
                    else:
                        coord_y = 730

                    coord = 23 - column
                    if coord >= 0 and coord <= 23:
                        if len(self.board[1][coord][0]) < 2 and column >= 0:
                            next_pos.append([column, coord_y])

            else:
                column = x - dice[0]
                if column < 12:
                    coord_y = 15
                else:
                    coord_y = 730

                coord = 23 - column
                if coord >= 0 and coord <= 23:
                    if len(self.board[1][coord][0]) < 2 and column >= 0:
                        next_pos.append([column, coord_y])

        else:
            if len(dice) == 2:
                for index in range(0, len(dice)):
                    column = x - dice[index]
                    if column < 12:
                        coord_y = 730
                    else:
                        coord_y = 15

                    coord = 23 - column
                    if coord >= 0 and coord <= 23:
                        if len(self.board[0][coord][0]) < 2 and column >= 0:
                            next_pos.append([column, coord_y])

            else:
                column = x - dice[0]
                if column < 12:
                    coord_y = 730
                else:
                    coord_y = 15

                coord = 23 - column
                if coord >= 0 and coord <= 23:
                    if len(self.board[0][coord][0]) < 2 and column >= 0:
                        next_pos.append([column, coord_y])

        if len(next_pos) == 0 and y > 0 and self.name[jucator] != "PC":
            messagebox.showerror("Backgammon!!", "You don't have where to move this piece")

        return next_pos

    def update_board(self, jucator, coloana_luat, coloana_pus):
        if jucator == 1:
            oponent = 0
            poz_id = [-65, 65]
        else:
            oponent = 1
            poz_id = [65, -65]

        if coloana_luat != -5:
            self.board[jucator][coloana_luat][0][-1].destroy()
            self.board[jucator][coloana_luat][0].pop()
            if len(self.board[jucator][coloana_luat][0]) > 5:
                self.replace_piece(self.board[jucator][coloana_luat], coloana_luat, 0)
            else:
                self.replace_piece(self.board[jucator][coloana_luat], coloana_luat, 1)

            poz = len(self.board[jucator][coloana_pus][0]) + 1
            self.board[jucator][coloana_pus][0].append(tk.Button(self.main_frame, image=piece_image[jucator],
                                                                 command=lambda: self.move(jucator, coloana_pus, poz)))

            if coloana_pus <= 11:
                self.board[jucator][coloana_pus][0][-1].place(x=self.board[jucator][coloana_pus][1],
                                                              y=(self.board[jucator][coloana_pus][2] + poz_id[0] * (
                                                                      len(self.board[jucator][coloana_pus][0]) - 1)))
                if len(self.board[jucator][coloana_pus][0]) > 5:
                    self.replace_piece(self.board[jucator][coloana_pus], coloana_pus, 0)
                else:
                    self.replace_piece(self.board[jucator][coloana_pus], coloana_pus, 1)
            elif coloana_pus > 11:
                self.board[jucator][coloana_pus][0][-1].place(x=self.board[jucator][coloana_pus][1],
                                                              y=(self.board[jucator][coloana_pus][2] + poz_id[1] * (
                                                                      len(self.board[jucator][coloana_pus][0]) - 1)))
                if len(self.board[jucator][coloana_pus][0]) > 5:
                    self.replace_piece(self.board[jucator][coloana_pus], coloana_pus, 0)
                else:
                    self.replace_piece(self.board[jucator][coloana_pus], coloana_pus, 1)

            coloana_oponent = 23 - coloana_pus

        else:

            poz = len(self.board[jucator][23 - coloana_pus][0]) + 1
            self.board[jucator][23 - coloana_pus][0].append(tk.Button(self.main_frame, image=piece_image[jucator],
                                                                      command=lambda: self.move(jucator,
                                                                                                23 - coloana_pus, poz)))

            if coloana_pus <= 11:
                self.board[jucator][23 - coloana_pus][0][-1].place(x=self.board[jucator][23 - coloana_pus][1],
                                                                   y=(self.board[jucator][23 - coloana_pus][2] + poz_id[
                                                                       0] * (-1) * (
                                                                              len(self.board[jucator][23 - coloana_pus][
                                                                                      0]) - 1)))
                if len(self.board[jucator][23 - coloana_pus][0]) > 5:
                    self.replace_piece(self.board[jucator][23 - coloana_pus], 23 - coloana_pus, 0)
                else:
                    self.replace_piece(self.board[jucator][23 - coloana_pus], 23 - coloana_pus, 1)

            coloana_oponent = coloana_pus

        if coloana_oponent >= 0 and coloana_oponent <= 23 and len(self.board[oponent][coloana_oponent][0]) == 1:
            self.board[oponent][coloana_oponent][0][-1].destroy()
            self.board[oponent][coloana_oponent][0].pop()
            self.stats[oponent][0] += 1
            print("eliminate::", self.stats[oponent][0])
            self.show_player_stats(self.main_frame, self.stats)

    def move_piece(self, jucator, coloana, luat):
        print("am dat click pe:", coloana, luat)
        global list_btn_option
        for btn in list_btn_option:
            btn.destroy()
        list_btn_option = []

        self.update_board(jucator, luat, coloana)

        if luat != -5:
            val_zar = luat - coloana
            print(val_zar)
            dice.remove(val_zar)
        else:
            val_zar = coloana + 1
            print(val_zar)
            dice.remove(val_zar)
            self.stats[jucator][0] -= 1
            self.show_player_stats(self.main_frame, self.stats)
            if self.stats[jucator][0] > 0 and len(dice) > 0:
                self.revive(jucator)

        global turn
        if len(dice) == 0:
            if turn == 0:
                turn = 1
                label_mini_list[0].config(fg="white")
                label_mini_list[1].config(fg="#80ff80")
                if turn == 1 and self.name[1] == "PC":
                    self.pc_play()
            else:
                turn = 0
                label_mini_list[1].config(fg="white")
                label_mini_list[0].config(fg="#80ff80")
            roll_button.config(state="normal")

    def options(self, jucator, x, y):
        global list_btn_option
        if len(list_btn_option) > 0:
            messagebox.showinfo("Backgammon!!", "The piece selected previously will be deselected")
            for btn in list_btn_option:
                btn.destroy()
            list_btn_option = []

        if self.all_in_house(jucator) == False:
            next_pos = self.piece_next_place(jucator, x, y)
            for i in range(0, len(next_pos)):
                if next_pos[i][1] == 15:
                    list_btn_option.append(tk.Button(self.main_frame, text=" ^ "))
                    list_btn_option[i].place(x=(17 + self.board[jucator][next_pos[i][0]][1]), y=350)
                else:
                    list_btn_option.append(tk.Button(self.main_frame, text=" v "))
                    list_btn_option[i].place(x=(17 + self.board[jucator][next_pos[i][0]][1]), y=430)

            if len(list_btn_option) > 0:
                list_btn_option[0].config(command=lambda: self.move_piece(jucator, next_pos[0][0], x))
                if len(list_btn_option) == 2:
                    list_btn_option[1].config(command=lambda: self.move_piece(jucator, next_pos[1][0], x))
        else:
            next_pos = self.end_piece_life(jucator, x, y)
            for i in range(0, len(next_pos)):
                if next_pos[i][1] == 15:
                    list_btn_option.append(tk.Button(self.main_frame, text=" ^ "))
                    list_btn_option[i].place(x=(17 + self.board[jucator][next_pos[i][0]][1]), y=350)
                elif next_pos[i][1] == 730:
                    list_btn_option.append(tk.Button(self.main_frame, text=" v "))
                    list_btn_option[i].place(x=(17 + self.board[jucator][next_pos[i][0]][1]), y=430)
                else:
                    list_btn_option.append(tk.Button(self.main_frame, text="Scoate"))
                    if jucator == 0:
                        list_btn_option[i].place(x=12, y=560)
                    else:
                        list_btn_option[i].place(x=1133, y=560)

            if len(list_btn_option) > 0:
                if list_btn_option[0]["text"] == "Scoate":
                    list_btn_option[0].config(command=lambda: self.remove_piece(jucator, x))
                else:
                    list_btn_option[0].config(command=lambda: self.move_piece(jucator, next_pos[0][0], x))

                if len(list_btn_option) == 2:
                    if list_btn_option[1]["text"] == "Scoate":
                        list_btn_option[1].config(command=lambda: self.remove_piece(jucator, x))
                    else:
                        list_btn_option[1].config(command=lambda: self.move_piece(jucator, next_pos[1][0], x))

    def remove_piece(self, jucator, coloana):
        self.board[jucator][coloana][0][-1].destroy()
        self.board[jucator][coloana][0].pop()
        self.stats[jucator][1] += 1

        verif_scos = 0
        for index in range(0, len(dice)):
            if coloana + 1 == dice[index]:
                print("AICI", coloana)
                dice.remove(coloana + 1)
                verif_scos = 1
                break;

        if verif_scos == 0:
            print("atunci, aici", coloana)
            okay = 0
            for i in range(1, 6):
                if okay == 0:
                    for index in range(0, len(dice)):
                        if i + coloana == dice[index]:
                            dice.remove(dice[index])
                            okay = 1
                            break

        global list_btn_option, roll_button
        for index in list_btn_option:
            index.destroy()
        for index in range(0, len(list_btn_option)):
            list_btn_option.pop()

        self.show_player_stats(self.main_frame, self.stats)

        winner = who_won(self)
        if winner > 0:
            show_winner(self.window, winner, self, roll_button)

        if len(dice) == 0:
            global turn
            roll_button.config(state="normal")
            if jucator == 0:
                turn = 1
                label_mini_list[0].config(fg="white")
                label_mini_list[1].config(fg="#80ff80")
                if turn == 1 and self.name[1] == "PC":
                    self.pc_play()
            else:
                turn = 0
                label_mini_list[1].config(fg="white")
                label_mini_list[0].config(fg="#80ff80")

    def revive(self, jucator):
        if jucator == 1:
            other_player = 0
            coord_y = 15
        else:
            other_player = 1
            coord_y = 730

        posible_position = []
        global dice, turn

        if len(dice) == 2:
            for zar in dice:
                if len(self.board[other_player][zar - 1][0]) < 2:
                    posible_position.append([zar - 1, coord_y])
        else:
            if len(self.board[other_player][dice[0] - 1][0]) < 2:
                posible_position.append([dice[0] - 1, coord_y])

        if len(posible_position) == 0:
            roll_button.config(state="normal")
            dice = []
        else:
            global list_btn_option

            for i in range(0, len(posible_position)):
                if posible_position[i][1] == 15:
                    list_btn_option.append(tk.Button(self.main_frame, text=" ^ "))
                    list_btn_option[i].place(x=(17 + self.board[jucator][posible_position[i][0]][1]), y=350)
                else:
                    list_btn_option.append(tk.Button(self.main_frame, text=" v "))
                    list_btn_option[i].place(x=(17 + self.board[jucator][posible_position[i][0]][1]), y=430)

            if len(list_btn_option) > 0:
                list_btn_option[0].config(command=lambda: self.move_piece(jucator, posible_position[0][0], -5))
                if len(list_btn_option) == 2:
                    list_btn_option[1].config(command=lambda: self.move_piece(jucator, posible_position[1][0], -5))

            if self.name[jucator] == "PC":
                alegere = random.randrange(0,len(list_btn_option))
                list_btn_option[alegere].invoke()

    def move(self, jucator, x, y):
        global turn, dice

        if turn == 0 and len(dice) > 0:
            if jucator == 1:
                messagebox.showerror("Backgammon!!", "Not your piece")
            else:
                if self.stats[jucator][0] == 0:
                    self.options(jucator, x, y)
                else:
                    messagebox.showinfo("Backgammon!!",
                                        "You can't move pieces.\nYou have to get the eliminated ones on the board first.")

                if len(dice) == 0 or self.exist_move(jucator) == False:
                    roll_button.config(state="normal")
                    turn = 1
                    label_mini_list[0].config(fg="white")
                    label_mini_list[1].config(fg="#80ff80")
                    if turn == 1 and self.name[1] == "PC":
                        self.pc_play()
                    dice = []

        elif turn == 1 and len(dice) > 0:
            if jucator == 0:
                messagebox.showerror("Backgammon!!", "Not your piece")
            else:
                if self.stats[jucator][0] == 0:
                    self.options(jucator, x, y)
                else:
                    messagebox.showinfo("Backgammon!!",
                                        "You can't move pieces.\nYou have to get the eliminated ones on the board first.")

                if len(dice) == 0 or self.exist_move(jucator) == False:
                    roll_button.config(state="normal")
                    turn = 0
                    label_mini_list[1].config(fg="white")
                    label_mini_list[0].config(fg="#80ff80")
                    dice = []

        else:
            messagebox.showerror("Backgammon!!", "You must roll the dice first")

    def pc_move(self):
        print("PC:: move")
        global turn, dice, roll_button
        if turn == 1 and self.name[turn] == "PC" and len(dice) > 0:
            if self.stats[1][0] == 0 and self.exist_move(1) == True:
                global list_btn_option
                if len(list_btn_option) > 0:
                    for btn in list_btn_option:
                        btn.destroy()
                    list_btn_option = []

                print("PC:: aleg piesa")
                valabile = []
                for i in range(0, 24):
                    print("PC:: inca aleg ....")
                    if len(self.board[1][i][0]) > 0:
                        valabile.append(i)

                print("PC:: aleg din:", valabile)
                print("PC:: verific alegerea ....")
                id = random.randrange(0, len(valabile))
                x = valabile[id]
                while len(self.board[0][23-x][0]) > 1 or len(self.board[1][x][0]) == 0 or x<0 or x>23:
                    id = random.randrange(0, len(valabile))
                    x = valabile[id]

                print("PC:: am ales piesa")

                if x <= 11:
                    y = 730
                else:
                    y = 15

                if self.all_in_house(1) == False:
                    next_pos = self.piece_next_place(1, x, y)
                    for i in range(0, len(next_pos)):
                        if next_pos[i][1] == 15:
                            list_btn_option.append(tk.Button(self.main_frame, text=" ^ "))
                            list_btn_option[i].place(x=(17 + self.board[1][next_pos[i][0]][1]), y=350)
                        else:
                            list_btn_option.append(tk.Button(self.main_frame, text=" v "))
                            list_btn_option[i].place(x=(17 + self.board[1][next_pos[i][0]][1]), y=430)

                    if len(list_btn_option) > 0:
                        list_btn_option[0].config(command=lambda: self.move_piece(1, next_pos[0][0], x))
                        if len(list_btn_option) == 2:
                            list_btn_option[1].config(command=lambda: self.move_piece(1, next_pos[1][0], x))

                        if self.name[1] == "PC":
                            move = random.randrange(0, len(list_btn_option))
                            list_btn_option[move].invoke()

                        print("PC:: am mutat")

                else:
                    next_pos = self.end_piece_life(1, x, y)
                    for i in range(0, len(next_pos)):
                        if next_pos[i][1] == 15:
                            list_btn_option.append(tk.Button(self.main_frame, text=" ^ "))
                            list_btn_option[i].place(x=(17 + self.board[1][next_pos[i][0]][1]), y=350)
                        elif next_pos[i][1] == 730:
                            list_btn_option.append(tk.Button(self.main_frame, text=" v "))
                            list_btn_option[i].place(x=(17 + self.board[1][next_pos[i][0]][1]), y=430)
                        else:
                            list_btn_option.append(tk.Button(self.main_frame, text="Scoate"))
                            if turn == 0:
                                list_btn_option[i].place(x=12, y=560)
                            else:
                                list_btn_option[i].place(x=1133, y=560)

                    if len(list_btn_option) > 0:
                        if list_btn_option[0]["text"] == "Scoate":
                            list_btn_option[0].config(command=lambda: self.remove_piece(1, x))
                        else:
                            list_btn_option[0].config(command=lambda: self.move_piece(1, next_pos[0][0], x))

                        if len(list_btn_option) == 2:
                            if list_btn_option[1]["text"] == "Scoate":
                                list_btn_option[1].config(command=lambda: self.remove_piece(1, x))
                            else:
                                list_btn_option[1].config(command=lambda: self.move_piece(1, next_pos[1][0], x))

                        if self.name[1] == "PC":
                            move = random.randrange(0, len(list_btn_option))
                            list_btn_option[move].invoke()

                        print("PC:: am scos piesa")


        if len(dice) > 0:
            self.pc_move()
        elif self.exist_move(1) == False:
            dice = []
            self.pc_move()
        else:
            dice = []
            roll_button.config(state="normal")
            turn = 0
            label_mini_list[1].config(fg="white")
            label_mini_list[0].config(fg="#80ff80")


    def pc_play(self):
        label_mini_list[0].config(fg="white")
        label_mini_list[1].config(fg="#80ff80")

        print("SUNT PC")
        global turn, dice, roll_button, dice_image
        dice = []
        roll_dice(self.main_frame, dice_image, self)
        print("PC::", dice)

        self.pc_move()

        # apelez functia care imi arata optiunile
        # aleg random una din ele
        # mut, elimin zarul
        # daca dice nu e null repet

        dice = []
        roll_button.config(state="normal")
        turn = 0
        label_mini_list[1].config(fg="white")
        label_mini_list[0].config(fg="#80ff80")


# END CLASS


def who_won(player):
    if player.stats[0][1] == 15:
        return 1
    elif player.stats[1][1] == 15:
        return 2
    else:
        return 0


def roll_dice(main_frame, dice_image, player):
    time.sleep(0.5)
    global dice
    zar1 = random.randrange(1, 7)
    zar2 = random.randrange(1, 7)
    if zar1 == zar2:
        dice.append(zar1)
        dice.append(zar1)
        dice.append(zar1)
        dice.append(zar1)
    else:
        dice.append(zar1)
        dice.append(zar2)

    global image, turn
    img1 = tk.PhotoImage(file="assets/dice1.png")
    img2 = tk.PhotoImage(file="assets/dice2.png")
    img3 = tk.PhotoImage(file="assets/dice3.png")
    img4 = tk.PhotoImage(file="assets/dice4.png")
    img5 = tk.PhotoImage(file="assets/dice5.png")
    img6 = tk.PhotoImage(file="assets/dice6.png")
    image = [img1, img2, img3, img4, img5, img6]

    if len(dice_image) <= 0:
        dice_image.append(tk.Label(main_frame, image=image[zar1 - 1]))
        dice_image[0].place(x=780, y=380)

        dice_image.append(tk.Label(main_frame, image=image[zar2 - 1]))
        dice_image[1].place(x=830, y=380)
    else:
        dice_image[0].configure(image=image[zar1 - 1])
        dice_image[0].place(x=780, y=380)

        dice_image[1].configure(image=image[zar2 - 1])
        dice_image[1].place(x=830, y=380)

    roll_button.config(state="disabled")
    if player.stats[turn][0] > 0:
        player.revive(turn)
        if len(dice) == 0:
            if turn == 0:
                turn = 1
                label_mini_list[0].config(fg="white")
                label_mini_list[1].config(fg="#80ff80")
                if turn == 1 and player.name[1] == "PC":
                    player.pc_play()
            else:
                turn = 0
                label_mini_list[1].config(fg="white")
                label_mini_list[0].config(fg="#80ff80")

    if player.exist_move(turn) == False:
        roll_button.config(state="normal")


def show_winner(window, id, player, roll_button):
    roll_button.config(state="disabled")
    time.sleep(1)
    if id == 1:
        text = player.name[0]
    else:
        text = player.name[1]

    canvas = tk.Canvas(window, width=600, height=400, bg="#000000")
    canvas.place(x=600, y=400, anchor=CENTER)

    color_codes = ["#fb1239", "#aa40ff", "#f0851b", "#0033cc", "#ffa97e", "#FFE133", "#64FF33", "#FF0D0D", "#0DB7FF",
                   "#FF2DB6"]
    max_artificii = random.randrange(10, 15)
    for i in range(0, max_artificii):
        x = random.randrange(0, 600)
        y = random.randrange(0, 400)
        color = random.randrange(0, 9)
        dim = random.randrange(75, 225)
        canvas.create_oval(x, y, x + dim, y + dim, fill=color_codes[color])

    canvas.create_oval(200, 100, 400, 300, fill=color_codes[color])
    text = text + " won!!"
    text_font = font.Font(size=20)
    label_winner = tk.Label(canvas, text=text, fg="#000000", bg=color_codes[color], font=text_font)
    canvas.create_window(300, 200, window=label_winner)

    window.mainloop


def player_gui_init(window):
    main_frame = tk.Frame(window, width=1200, height=800)
    main_frame.pack(side="top", expand=False, fill="both")

    global background
    background = tk.PhotoImage(file="assets/board2.png")
    label_background = tk.Label(main_frame, image=background)
    label_background.place(x=-3, y=-2)

    global player
    player = Player(window, main_frame, "player 1", "player 2")

    global dice_image
    dice_image = []
    text_font = font.Font(size=14)
    global roll_button
    roll_button = tk.Button(main_frame, text="Roll", font=text_font, bg='#4e555f', fg='white', border=2,
                            command=lambda: roll_dice(main_frame, dice_image, player))
    roll_button.place(x=360, y=380)

    # TO DO: init game, start game
    # HOW TO START GAME: 2 ture: player 1, player 2; while pana nu a castigat cnv; in while se afiseaza statusul, in functie de tura joaca jucatorul x, dupa mutare se reinitializeaza statusurile


def pc_gui_init(window):
    main_frame = tk.Frame(window, width=1200, height=800)
    main_frame.pack(side="top", expand=False, fill="both")

    global background
    background = tk.PhotoImage(file="assets/board2.png")
    label_background = tk.Label(main_frame, image=background)
    label_background.place(x=-3, y=-2)

    global player
    player = Player(window, main_frame, "player 1", "PC")

    global dice_image
    dice_image = []
    text_font = font.Font(size=14)
    global roll_button
    roll_button = tk.Button(main_frame, text="Roll", font=text_font, bg='#4e555f', fg='white', border=2,
                            command=lambda: roll_dice(main_frame, dice_image, player))
    roll_button.place(x=360, y=380)


def main_menu(window):
    main_frame = tk.Frame(window, width=1200, height=800)
    main_frame.pack(side="top", expand=False, fill="both")

    global background
    background = tk.PhotoImage(file="assets/background.png")
    label_background = tk.Label(main_frame, image=background)
    label_background.place(x=-5, y=-2)

    button_list: List[tk.Button] = []
    button_id = 0
    text_font = font.Font(size=15)

    def help_callback():
        webbrowser.open("https://en.wikipedia.org/wiki/Backgammon")

    # buton cu instructiuni
    button_list.append(tk.Button(main_frame, text="Instructiuni", bg="#c2fcdd", fg="#002e1d", font=text_font,
                                 command=lambda: help_callback()))
    button_list[button_id].place(x=530, y=340)
    button_id += 1

    def player_callback(window):
        window.destroy()
        window = create_window()

        # TO DO: initializeaza jocul
        player_gui_init(window)

    # buton pentru jocul dintre 2 jucatori
    button_list.append(tk.Button(main_frame, text="Player vs player", bg="#c2fcdd", fg="#002e1d", font=text_font,
                                 command=lambda: player_callback(window)))
    button_list[button_id].place(x=505, y=400)
    button_id += 1

    def pc_callback(window):
        window.destroy()
        window = create_window()

        # TO DO: initializeaza jocul
        pc_gui_init(window)

    # buton pentru jocul dintre jucator si pc
    button_list.append(tk.Button(main_frame, text="Player vs PC", bg="#c2fcdd", fg="#002e1d", font=text_font,
                                 command=lambda: pc_callback(window)))
    button_list[button_id].place(x=520, y=460)
    button_id += 1

    window.mainloop()


def create_window():
    """
    Here we will create the window for the game with the proper name and icon.
    :return: window
    """
    window = tk.Tk()
    window.title("Backgammon!!")

    window.configure(width=1200, height=800)
    window.resizable(False, False)

    icon = tk.PhotoImage(file="assets/icon.png")
    window.iconphoto(False, icon)

    window.eval('tk::PlaceWindow . center')
    return window


def main():
    window = create_window()
    main_menu(window)
    window.mainloop()


if __name__ == '__main__':
    main()
