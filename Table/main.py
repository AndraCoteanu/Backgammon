import random
import webbrowser
import tkinter as tk
from time import sleep
from tkinter import font
from typing import List
from player import Player


# TO DO: adauga comentarii si ctrl+alt+l

def who_won(player):
    if player.stats[0][1] == 15:
        return 1
    elif player.stats[1][1] == 15:
        return 2
    else:
        return 0


def roll_dice(main_frame, dice_image):
    dice = []
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

    global image
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

    return dice


def play(window, main_frame, player, roll_button, turn):
    win = 0
    if turn == 0:
        # joc
        player.stats[1][1] += 1
        print("aici")
        win = who_won(player)
        turn = 1
    else:
        # joc
        win = who_won(player)
        turn = 0


    if win > 0:
        show_winner(window, main_frame, win, player, roll_button)
    else:
        window.after(500, play(window, main_frame, player, roll_button, turn))
        window.mainloop()




def show_winner(window, main_frame, id, player, roll_button):
    roll_button.config(state="disabled")

    sleep(1)

    if id == 1:
        text = player.name[0]
    else:
        text = player.name[1]

    text = text + " won!!"
    text_font = font.Font(size=20)
    label_winner = tk.Label(main_frame, text=text, fg="#ffffff", bg="#000000", font=text_font)
    label_winner.place(x=600, y=350, anchor="center")

    window.mainloop


def player_gui_init(window):
    main_frame = tk.Frame(window, width=1200, height=800)
    main_frame.pack(side="top", expand=False, fill="both")

    global background
    background = tk.PhotoImage(file="assets/board2.png")
    label_background = tk.Label(main_frame, image=background)
    label_background.place(x=-3, y=-2)

    player = Player(main_frame, "player 1", "player 2")

    dice_image = []
    text_font = font.Font(size=14)
    roll_button = tk.Button(main_frame, text="Roll", font=text_font, command=lambda: roll_dice(main_frame, dice_image))
    roll_button.place(x=360, y=380)

    window.after(500, play(window, main_frame, player, roll_button, 0))

    # label = tk.Label(main_frame, text="ahalkdaslkdljslfjlsaakd;s")
    # label.place(x=120, y=120)

    # TO DO: init game, start game
    # HOW TO INIT GAME: lista de playeri, fiecare player va avea o lista de imagini (piese)
    # HOW TO START GAME: 2 ture: player 1, player 2; while pana nu a castigat cnv; in while se afiseaza statusul, in functie de tura joaca jucatorul x, dupa mutare se reinitializeaza statusurile


# TO DO: def pc_gui_init(window):


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
        player_gui_init(window)

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

    # asta cred ca e inutil, da arata bn si aici
    window.mainloop()


if __name__ == '__main__':
    main()
