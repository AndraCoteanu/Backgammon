import random
import webbrowser
from tkinter import *
from tkinter import font


def main_menu():
    window = Tk()
    window.title("Backgammon!!")
    window.configure(width=1200, height=700)
    window.resizable(False, False)

    icon = PhotoImage(file="assets/icon.png")
    window.iconphoto(False, icon)

    main_screen = Frame(window, width=1200, height=700)
    main_screen.pack(side="top", expand=False, fill="both")

    background = PhotoImage(
        file="E:\\[FII] Facultate\\Anul 3 - Semestrul 1\\[PP] Python\\lab\\Table\\assets\\background.png")
    label_background = Label(main_screen, image=background)
    label_background.place(x=-5, y=-2)

    text_font = font.Font(size=20)
    btn_help = Button(main_screen, text="Instructiuni", bg="#c2fcdd", fg="#002e1d", font=text_font,
                      command=help_callback)
    btn_help.place(x=530, y=260)

    btn_player = Button(main_screen, text="Player vs player", bg="#c2fcdd", fg="#002e1d", font=text_font,
                        command=lambda: player_callback(main_screen))
    btn_player.place(x=500, y=340)

    btn_pc = Button(main_screen, text="Player vs PC", bg="#c2fcdd", fg="#002e1d", font=text_font,
                    command=lambda: pc_callback(main_screen))
    btn_pc.place(x=520, y=420)

    # SOUND_ON = True
    # for some reason python stops working when trying to run playsound
    # playsound.playsound("assets/music.mp3")
    # SOUND = PhotoImage(file="assets/sound-on.png")
    # BUTTON_SOUND = Button(window, text="", image=SOUND, bg="#c2fcdd", command=sound_callback)
    # BUTTON_SOUND.place(x=10, y=10)

    window.mainloop()


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


def help_callback():
    webbrowser.open("https://en.wikipedia.org/wiki/Backgammon")


def player_callback(frame):
    clear_frame(frame)


def pc_callback(frame):
    clear_frame(frame)


def color_coosing():
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


if __name__ == '__main__':
    main_menu()
