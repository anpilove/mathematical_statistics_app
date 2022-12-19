from tkinter import *
import numpy as np


class MainMenu:
    def __init__(self):
        self.conf_inter = 0
        self.window = Tk()
        self.window.title("Темы математической статистики")
        self.window.geometry("1000x1000")
        self.conf = Button(text="Доверительный интервал ", width=50, command=self.create_сonf_inter)
        self.conf.grid(row=1, column=1, sticky=N + S + W + E)
        self.window.mainloop()

    @staticmethod
    def remove_button(button):
        button.destroy()

    def create_сonf_inter(self):
        # if сonf_inter % 2 == 0:
        #     self.remove_button(self.dover1)
        #     self.remove_button(self.dover2)

        dover1 = Button(text="Доверительный интервал без надежности ", width=50)
        dover2 = Button(text="Доверительный интервал c надежности ", width=50)
        dover1.grid(row=1, column=2)
        dover2.grid(row=2, column=2)

    def dover_(self):
        pass


# download_icon = tk.PhotoImage(file='./assets/download.png')

program = MainMenu()

