from tkinter import *

WINDOW = Tk()
WINDOW.title("Backgammon!!")
WINDOW.configure(width=1200, height=700)

BACKGROUND = PhotoImage(file="E:\\[FII] Facultate\\Anul 3 - Semestrul 1\\[PP] Python\\lab\\Table\\assets\\background.png")
LABEL_BACKGROUND = Label(WINDOW, image=BACKGROUND)
LABEL_BACKGROUND.place(x=-5, y=-2)

WINDOW.mainloop()