import webbrowser
from tkinter import *
from tkinter import font

import game as game
import utils

window = Tk()
window.title("Backgammon!!")
window.configure(width=1200, height=800)
window.resizable(False, False)

icon = PhotoImage(file="assets/icon.png")
window.iconphoto(False, icon)


def main_menu():
    main_screen = Frame(window, width=1200, height=800)
    main_screen.pack(side="top", expand=False, fill="both")

    background = PhotoImage(
        file="E:\\[FII] Facultate\\Anul 3 - Semestrul 1\\[PP] Python\\lab\\Table\\assets\\background.png")
    label_background = Label(main_screen, image=background)
    label_background.place(x=-5, y=-2)

    text_font = font.Font(size=15)
    btn_help = Button(main_screen, text="Instructiuni", bg="#c2fcdd", fg="#002e1d", font=text_font,
                      command=help_callback)
    btn_help.place(x=530, y=340)

    btn_player = Button(main_screen, text="Player vs player", bg="#c2fcdd", fg="#002e1d", font=text_font,
                        command=lambda: player_callback(main_screen))
    btn_player.place(x=505, y=400)

    btn_pc = Button(main_screen, text="Player vs PC", bg="#c2fcdd", fg="#002e1d", font=text_font,
                    command=lambda: pc_callback(main_screen))
    btn_pc.place(x=520, y=460)

    window.mainloop()


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()
    frame.destroy()


def help_callback():
    webbrowser.open("https://en.wikipedia.org/wiki/Backgammon")


def player_callback(frame):
    clear_frame(frame)
    main_screen = Frame(window, width=1200, height=800)
    main_screen.pack(side="top", expand=False, fill="both")

    canvas = Canvas(main_screen, width=1200, height=800)
    canvas.pack()

    background = PhotoImage(file="assets/board2.png")
    canvas.create_image(0, 0, image=background, anchor=NW)

    # st-dr, sus-jos, img
    # +70
    utile = utils.Utils()
    board = utile.init_board()
    color_path = utile.color_coosing()
    joc = game.Game(board, color_path, canvas)
    joc.show_board()

    window.mainloop()


def pc_callback(frame):
    clear_frame(frame)
    main_screen = Frame(window, width=1200, height=800)
    main_screen.pack(side="top", expand=False, fill="both")

    canvas = Canvas(main_screen, width=1200, height=800)
    canvas.pack()

    background = PhotoImage(file="assets/board2.png")
    canvas.create_image(0, 0, image=background, anchor=NW)

    # st-dr, sus-jos, img
    # +70

    utile = utils.Utils()
    board = utile.init_board()
    color_path = utile.color_coosing()
    joc = game.Game(board, color_path, canvas)
    joc.show_board()

    window.mainloop()


if __name__ == '__main__':
    main_menu()