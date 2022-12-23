from tkinter import *
import numpy as np
import time
import scipy.stats as st
from scipy.stats import t

#hi bro
#проверяю апдейт чужого проекта

class Conf_Inter:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1000x1000")
        self.info = Label(self.window, text="Введите выборку через пробел")
        self.enter1 = Entry(self.window)
        self.info.grid(row=1, column=1)
        self.enter1.grid(row=1, column=2)


class Conf_Inter_Without_Reliability(Conf_Inter):
    def __init__(self):
        super().__init__()
        self.confirm = Button(self.window, text="Потвердить", command=self.count)
        self.confirm.grid(row=1, column=3)
        self.window.title("Доверительный интервал без надежности")

    def count(self):
        list_values = self.enter1.get().split()
        list_values = list(map(int, list_values))
        list_values = np.array(list_values)

        mean = list_values.mean()
        mean_l = Label(self.window, text=f"Среднее арифметическое {mean}")
        mean_l.grid(row=2, column=1)

        median = np.median(list_values)
        median_l = Label(self.window, text=f"Медиана {median}")
        median_l.grid(row=3, column=1)

        razmax = np.max(list_values) - np.min(list_values)
        razmax_l = Label(self.window, text=f"Размах {razmax}")
        razmax_l.grid(row=4, column=1)

        dispersya = np.var(list_values)
        dispersya_l = Label(self.window, text=f"Дисперсия {dispersya}")
        dispersya_l.grid(row=5, column=1)

        srednie_kvadr = np.std(list_values)
        srednie_kvadr_l = Label(self.window, text=f"Cреднеквадратичное отклонение {srednie_kvadr}")
        srednie_kvadr_l.grid(row=6, column=1)
        print(srednie_kvadr)

        variation = srednie_kvadr / mean
        variation_l = Label(self.window, text=f"Коэффициент вариации {variation}")
        variation_l.grid(row=7, column=1)

        oscillation = razmax / mean
        oscillation_l = Label(self.window, text=f"Коэффициент осцилляции {oscillation}")
        oscillation_l.grid(row=8, column=1)

        conf_inter_l = Label(self.window,
                             text=f"Доверительный интервал: ({median - srednie_kvadr} ; {median + srednie_kvadr})")
        conf_inter_l.grid(row=9, column=1)


class Conf_Inter_Reliability(Conf_Inter_Without_Reliability):
    def __init__(self):
        super().__init__()
        print(1111)
        self.info1 = Label(self.window, text="Введите надежность ")
        self.info1.grid(row=1, column=4)
        self.entry2 = Entry(self.window)
        self.entry2.grid(row=1, column=5)
        self.window.title("Доверительный интервал c надежностью")
        self.window.mainloop()

    def count(self):
        list_values = self.enter1.get().split()
        alpha = float(self.entry2.get())
        list_values = list(map(int, list_values))
        list_values = np.array(list_values)

        mean = list_values.mean()
        mean_l = Label(self.window, text=f"Среднее арифметическое {mean}")
        mean_l.grid(row=2, column=1)

        median = np.median(list_values)
        median_l = Label(self.window, text=f"Медиана {median}")
        median_l.grid(row=3, column=1)

        razmax = np.max(list_values) - np.min(list_values)
        razmax_l = Label(self.window, text=f"Размах {razmax}")
        razmax_l.grid(row=4, column=1)

        dispersya = np.var(list_values)
        dispersya_l = Label(self.window, text=f"Дисперсия {dispersya}")
        dispersya_l.grid(row=5, column=1)

        srednie_kvadr = np.std(list_values)
        srednie_kvadr_l = Label(self.window, text=f"Cреднеквадратичное отклонение {srednie_kvadr}")
        srednie_kvadr_l.grid(row=6, column=1)
        print(srednie_kvadr)

        variation = srednie_kvadr / mean
        variation_l = Label(self.window, text=f"Коэффициент вариации {variation}")
        variation_l.grid(row=7, column=1)

        oscillation = razmax / mean
        oscillation_l = Label(self.window, text=f"Коэффициент осцилляции {oscillation}")
        oscillation_l.grid(row=8, column=1)

        t_crit = np.abs(t.ppf((1 - alpha) / 2, (len(list_values) - 1)))

        conf_inter_l = Label(self.window,
                             text=f"Доверительный интервал: ({mean - srednie_kvadr * t_crit / np.sqrt(len(list_values))} ; {mean + srednie_kvadr * t_crit / np.sqrt(len(list_values))})")
        conf_inter_l.grid(row=9, column=1)


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
    def remove_button(args):
        for button in args:
            button.destroy()

    def create_сonf_inter(self):
        dover1 = Button(text="Доверительный интервал без надежности ", width=50,
                        command=lambda: Conf_Inter_Without_Reliability())
        dover2 = Button(text="Доверительный интервал c надежности ", width=50,
                        command=lambda: Conf_Inter_Reliability())
        dover1.grid(row=1, column=2)
        dover2.grid(row=2, column=2)
        dover_exit = Button(text="Доверительный интервал", width=50, command=lambda: self.remove_button(list_buttons))
        list_buttons = [dover1, dover2, dover_exit]
        dover_exit.grid(row=1, column=1)

    def dover_(self):
        pass


# download_icon = tk.PhotoImage(file='./assets/download.png')

program = MainMenu()
