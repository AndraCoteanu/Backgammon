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


if __name__ == '__main__':
    main_menu()
