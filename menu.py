from tkinter import *
from PIL import Image as I
import numpy as np
import time
import scipy.stats as st
from scipy.stats import t
import statistics
import math

#hi bro
#проверяю апдейт чужого проекта

class Conf_Inter:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1920x1080")
        self.info = Label(self.window, text="Введите выборку через пробел")
        self.enter1 = Entry(self.window)
        self.info.grid(row=1, column=1)
        self.enter1.grid(row=1, column=2)
        self.canvas = Canvas(self.window, bg='white', height=800, width=687)
        self.test = PhotoImage(master = self.canvas,file='conf1.png')
        self.testImg = self.canvas.create_image(0, 0, anchor=NW, image=self.test)
        self.canvas.grid(row=11,column=5)



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
        print(t_crit)

        conf_inter_l = Label(self.window,
                             text=f"Доверительный интервал: ({mean - srednie_kvadr * t_crit / np.sqrt(len(list_values))} ; {mean + srednie_kvadr * t_crit / np.sqrt(len(list_values))})")
        conf_inter_l.grid(row=9, column=1)

class Hypothesis:
    def __init__(self):
        self.window = Tk()
        self.window.title("Проверка гипотезы по двум выборкам")
        self.window.geometry("1920x1080")
        self.info1 = Label(self.window, text="Введите первую выборку через пробел")
        self.enter1 = Entry(self.window)
        self.info1.grid(row=1, column=1)
        self.enter1.grid(row=1, column=2)

        self.info2 = Label(self.window, text="Введите вторую выборку через пробел")
        self.enter2 = Entry(self.window)
        self.info2.grid(row=2, column=1)
        self.enter2.grid(row=2, column=2)

        self.confirm = Button(self.window, text="Потвердить", command=self.count)
        self.confirm.grid(row=3, column=2)

        self.info1 = Label(self.window, text="Введите надежность ")
        self.info1.grid(row=1, column=5)

        self.entry3 = Entry(self.window)
        self.entry3.grid(row=1, column=6)

        self.canvas = Canvas(self.window, bg='white', height=500, width=400)
        self.test = PhotoImage(master=self.canvas, file='hyp311.png')
        self.testImg = self.canvas.create_image(0, 0, anchor=NW, image=self.test)
        self.canvas.grid(row=11, column=5)

        self.canvas1 = Canvas(self.window, bg='white', height=500, width=500)
        self.test1 = PhotoImage(master=self.canvas1, file='hyp322.png')
        self.testImg1 = self.canvas1.create_image(0, 0, anchor=NW, image=self.test1)
        self.canvas1.grid(row=11, column=6)





    def count(self):
        list_values1 = self.enter1.get().split()
        list_values1 = list(map(float, list_values1))
        list_values1 = np.array(list_values1)

        list_values2 = self.enter2.get().split()
        list_values2 = list(map(float, list_values2))
        list_values2 = np.array(list_values2)

        alpha = float(self.entry3.get())

        mean1 = list_values1.mean()
        mean1_l = Label(self.window, text=f"Первая выборка: Среднее арифметическое {mean1}")
        mean1_l.grid(row=4, column=1)

        mean2 = list_values2.mean()
        mean2_l = Label(self.window, text=f"Вторая выборка: Среднее арифметическое {mean2}")
        mean2_l.grid(row=5, column=1)

        # median = np.median(list_values1)
        # median_l = Label(self.window, text=f"Медиана {median}")
        # median_l.grid(row=5, column=1)
        #
        # razmax = np.max(list_values) - np.min(list_values)
        # razmax_l = Label(self.window, text=f"Размах {razmax}")
        # razmax_l.grid(row=6, column=1)


        corrected_dispersya1 = statistics.variance(list_values1,mean1)
        corrected_dispersya1_l = Label(self.window,
                                       text=f"Первая выборка: Исправленная дисперсия {corrected_dispersya1}")
        corrected_dispersya1_l.grid(row=6, column=1)

        corrected_dispersya2 = statistics.variance(list_values2, mean2)
        corrected_dispersya2_l = Label(self.window,
                                       text=f"Вторая выборка: Исправленная дисперсия {corrected_dispersya2}")
        corrected_dispersya2_l.grid(row=7, column=1)

        n = len(list_values1)
        l = len(list_values2)

        corrected_dispersya = ((n-1) / (n+l-2))*corrected_dispersya1 + ((l-1) / (n+l-2)) * corrected_dispersya2
        print(corrected_dispersya)
        t1 = (mean1 - mean2) / (math.sqrt(corrected_dispersya) * math.sqrt((1/n)+(1/l)))
        t_l1 = Label(self.window,text=f"T набл {t1}")
        t_l1.grid(row=8,column=1)
        s = t.ppf(1-alpha, len(list_values1)+len(list_values2)-2)
        t_crit = np.abs(s)
        t2 = t_crit
        t_l2 = Label(self.window, text=f"T по фишеру {t2}")
        t_l2.grid(row=9, column=1)
        if t1 < t2:
            ans = Label(self.window, text=f"Гипотеза принимается")
            ans.grid(row=10, column=1)
        else:
            ans = Label(self.window, text=f"Гипотеза отвергается")
            ans.grid(row=10, column=1)




        # print(np.var(list_values1) * (len(list_values1)/ (len(list_values1) - 1)))
        print(statistics.variance(list_values1, mean1))


        # dispersya1_l = Label(self.window, text=f"Дисперсия {dispersya1}")
        # dispersya1_l.grid(row=7, column=1)

        # srednie_kvadr = np.std(list_values)
        # srednie_kvadr_l = Label(self.window, text=f"Cреднеквадратичное отклонение {srednie_kvadr}")
        # srednie_kvadr_l.grid(row=8, column=1)
        # print(srednie_kvadr)

class Intergroup_Variance:
    def __init__(self):
        self.window = Tk()
        self.window.title("Межгрупповая дисперссия")
        self.window.geometry("1000x1000")
        self.info1 = Label(self.window, text="""Пусть некоторая совокупность разбита на две равные по объему группы. 
        Предположим, что в первой группе среднее значение признака 
        x1 = ?, дисперсия σ21 = ?, а во второй группе x2 = ?,σ22 = ?. 
        Найдите среднее значение и дисперсию признака во всей со-
        вокупности.""")
        # self.enter1 = Entry(self.window)
        self.info1.grid(row=1, column=1)
        self.info1.grid(row=1, column=1)

        self.x1 = Label(self.window, text="x1")
        self.x2 = Label(self.window, text="x2")
        self.σ21 = Label(self.window, text="σ21")
        self.σ22 = Label(self.window, text="σ22")

        self.x1.grid(row=2, column=1)
        self.x2.grid(row=3, column=1)
        self.σ21.grid(row=4, column=1)
        self.σ22.grid(row=5, column=1)

        self.enterx1 = Entry(self.window)
        self.enterx2 = Entry(self.window)
        self.enterσ21 = Entry(self.window)
        self.enterσ22 = Entry(self.window)

        self.enterx1.grid(row=2, column=2)
        self.enterx2.grid(row=3, column=2)
        self.enterσ21.grid(row=4, column=2)
        self.enterσ22.grid(row=5, column=2)

        self.confirm = Button(self.window, text="Потвердить", command=self.count)
        self.confirm.grid(row=6, column=2)

        self.canvas1 = Canvas(self.window, bg='white', height=600, width=500)
        self.test1 = PhotoImage(master=self.canvas1, file='inter2.png')
        self.testImg1 = self.canvas1.create_image(0, 0, anchor=NW, image=self.test1)
        self.canvas1.grid(row=10, column=1)
        #
        # self.info2 = Label(self.window, text="Введите вторую выборку через пробел")
        # self.enter2 = Entry(self.window)
        # self.info2.grid(row=2, column=1)
        # self.enter2.grid(row=2, column=2)

    def count(self):
        x1 = float(self.enterx1.get())
        x1_disp = float(self.enterσ21.get())
        x2 = float(self.enterx2.get())
        x2_disp = float(self.enterσ22.get())
        n = 2
        x_mean = x1 * (1 / n) + x2 * (1 / n)
        x_disp = (x1_disp * (1 / n) + x2_disp * (1 / n)) + ((1 / n) * (x1 - x_mean) ** 2 + (1 / n) * (x2 - x_mean) ** 2)
        self.xmean = Label(self.window, text=f"Среднее значение всей совокупности{x_mean}")
        self.xdisp = Label(self.window, text=f"Средняя дисперссия всей совокупности{x_disp}")
        self.xmean.grid(row = 7 , column= 1)
        self.xdisp.grid(row= 8, column=1)

class Non_rep_Samp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Бесповторная выборка")
        self.window.geometry("1000x1000")
        self.info1 = Label(self.window,anchor= W, text="""Признак X(k) задан на множестве Ω = {1, 2, . . . , N}
                Из Ω извлекается случайная бесповторная выборка объема n. Найдите
                математическое ожидание и дисперсию среднего значения X призна-
                ка X в выборке.""")
        self.info1.grid(row=1,column=1)
        self.info2 = Label(self.window, text="Введите множество через пробел")
        self.enter1 = Entry(self.window)
        self.info2.grid(row=2, column=1)
        self.enter1.grid(row=2, column=2)

        self.info3 = Label(self.window, text="n")
        self.enter2 = Entry(self.window)
        self.info3.grid(row=3, column=1)
        self.enter2.grid(row=3, column=2)
        self.confirm = Button(self.window, text="Потвердить", command=self.count)
        self.confirm.grid(row=4, column=2)

        self.canvas1 = Canvas(self.window, bg='white', height=500, width=500)
        self.test1 = PhotoImage(master=self.canvas1, file='sample.png')
        self.testImg1 = self.canvas1.create_image(0, 0, anchor=NW, image=self.test1)
        self.canvas1.grid(row=11, column=1)



    def count(self):

        mas = self.enter1.get().split()
        mas = list(map(int, mas))
        mas = np.array(mas)
        # X_freq = np.unique(mas, return_counts=True)
        n = len(mas)
        nn = float(self.enter2.get())
        x_mean = np.mean(mas)
        x_disp = np.std(mas) ** 2
        d_x = x_disp / nn * (n - nn) / (n - 1)
        self.info4 = Label(self.window,anchor= W, text=f"Математическое ожидание среднего значения {x_mean}")
        self.info5 = Label(self.window,anchor= W, text=f"Дисперсия среднего значения {d_x}")

        self.info4.grid(row=4, column= 1)
        self.info5.grid(row=5, column= 1)

class Rep_Saml(Non_rep_Samp):
    def __init__(self):
        super().__init__()
        self.window.title("Повторная выборка")
        self.info1 = Label(self.window, anchor=W, text="""Признак X(k) задан на множестве Ω = {1, 2, . . . , 10}
        Из Ω извлекается случайная повторная выборка объема n. Найдите
        математическое ожидание и дисперсию среднего значения X призна-
        ка X в выборке.""")
        self.info1.grid(row=1, column=1)
        self.info1.grid(row=1, column=1)
        self.info2 = Label(self.window, text="Введите множество через пробел")
        self.enter1 = Entry(self.window)
        self.info2.grid(row=2, column=1)
        self.enter1.grid(row=2, column=2)

        self.info3 = Label(self.window, text="n")
        self.enter2 = Entry(self.window)
        self.info3.grid(row=3, column=1)
        self.enter2.grid(row=3, column=2)
        self.confirm = Button(self.window, text="Потвердить", command=self.count)
        self.confirm.grid(row=4, column=2)

    def count(self):
        print("""Признак X(k) задан на множестве Ω = {1, 2, . . . , 10}
                следующей таблицей:
                Из Ω извлекается случайная повторная выборка объема n. Найдите
                математическое ожидание и дисперсию среднего значения X призна-
                ка X в выборке.""")

        mas = np.array([3, 3, 3, 3, 1, 3, 3, 2, 1, 2])
        n = 10
        nn = 5
        x1_mean = np.mean(mas)
        x1_disp = round(np.std(mas) ** 2, 3)
        d_x1 = x1_disp / nn
        self.info4 = Label(self.window, anchor=W, text=f"Математическое ожидание среднего значения {x1_mean}")
        self.info5 = Label(self.window, anchor=W, text=f"Дисперсия среднего значения {d_x1}")

        self.info4.grid(row=4, column=1)
        self.info5.grid(row=5, column=1)
        print(x1_mean, x1_disp, d_x1)

class Point_stat_estimates:
    def __init__(self):
        self.window = Tk()
        self.window.title("Точечная оценка")
        self.window.geometry("1000x1000")
        self.info1 = Label(self.window, anchor=W, text="""Даны результаты независимых измерений одной
и той же величины прибором. Найдите несмещенную
оценку дисперсии ошибок измерений, если истинное значение X""")
        self.info1.grid(row=1, column=1)

        self.info2 = Label(self.window, text="Введите множество через пробел")
        self.enter1 = Entry(self.window)
        self.enter1.grid(row=2, column=2)
        self.info2.grid(row=2, column=1)
        self.info3 = Label(self.window, text="Введите истинное значение X")
        self.info3.grid(row=3, column=1)
        self.enter2 = Entry(self.window)
        self.enter2.grid(row=3, column=2)
        self.confirm = Button(self.window, text="Потвердить", command=self.count)
        self.confirm.grid(row=4, column=2)

    def count(self):
        u = float(self.enter2.get())
        mas = self.enter1.get().split()
        mas = list(map(int, mas))
        mas = np.array(mas)
        s1 = 1 / (len(mas))
        summary = 0
        for i in mas:
            summary += (i - u) ** 2
        s1 *= summary
        self.info4 = Label(self.window, text=f"Несмещенная оценка {s1}")
        self.info4.grid(row=5,column=1)

class Sampl_distribution:
    def __init__(self):
        self.window = Tk()
        self.window.title("Точечная оценка")
        self.window.geometry("1000x1000")
        self.info1 = Label(self.window, anchor=W, text="""Пусть X1,X2, .. Xn - выборка из равномерного распредления
        на отрезке [a,b]. F(x) - соответствующая выборчная функция распределения.
        Найдите P(F(P_f1) = F(P_f2))""")
        self.info1.grid(row=1, column=1)
        self.infoa = Label(self.window, text="Нижняя граница a")
        self.infoa.grid(row=2, column=1)
        self.entera = Entry(self.window)
        self.entera.grid(row=2, column=2)

        self.infob = Label(self.window, text="Верхняя граница b")
        self.infob.grid(row=3, column=1)
        self.enterb = Entry(self.window)
        self.enterb.grid(row=3, column=2)

        self.infop1 = Label(self.window, text="Pf-1")
        self.infop1.grid(row=4, column=1)
        self.enterp1 = Entry(self.window)
        self.enterp1.grid(row=4, column=2)

        self.infop2 = Label(self.window, text="Pf-2")
        self.infop2.grid(row=5, column=1)
        self.enterp2 = Entry(self.window)
        self.enterp2.grid(row=5, column=2)

        self.infon = Label(self.window, text="N")
        self.infon.grid(row=6, column=1)
        self.entern = Entry(self.window)
        self.entern.grid(row=6, column=2)




        self.confirm = Button(self.window, text="Потвердить", command=self.count)
        self.confirm.grid(row=7, column=2)

    def count(self):
        a = float(self.entera.get())# нижняя граница отрезка
        b = float(self.enterb.get())  # верхняя граница отрезка
        P_f1 = float(self.enterp1.get())  # P(F() = F())
        P_f2 = float(self.enterp2.get())
        N = float(self.entern.get())  # обьем выборки - количество
        P = (1 - (P_f2 - P_f1) / (b - a)) ** N
        self.infop = Label(self.window, text=f"Вероятность {P}")
        self.infop.grid(row=7, column=1)

class MainMenu:
    def __init__(self):
        self.window = Tk()
        self.window.title("Темы математической статистики")
        self.window.geometry("1000x1000")
        self.conf = Button(text="Доверительный интервал ", width=50, command=self.create_сonf_inter)
        self.conf.grid(row=1, column=1, sticky=N + S + W + E)
        self.hypothesis = Button(text="Проверка гипотез", width=50, command=self.create_hypothesis)
        self.hypothesis.grid(row=2, column=1, sticky=N + S + W + E)

        self.hypothesis = Button(text="Межгрупповая дисперссия", width=50, command=self.create_intergroup_variance)
        self.hypothesis.grid(row=3, column=1, sticky=N + S + W + E)

        self.hypothesis = Button(text="Повторная и бесповторная выборка", width=50, command=self.create_rep_non_rep_samp)
        self.hypothesis.grid(row=4, column=1, sticky=N + S + W + E)

        self.hypothesis = Button(text="Точечные статистические оценки", width=50, command=self.create_point_stat_estimates)
        self.hypothesis.grid(row=5, column=1, sticky=N + S + W + E)

        self.hypothesis = Button(text="Выборки из распределния", width=50,
                                 command=self.create_sampl_distribution)
        self.hypothesis.grid(row=6, column=1, sticky=N + S + W + E)

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

    def create_hypothesis(self):
        hypothesis1 = Button(text="Равенство генеральных средних по двум выборкам", width=50,
                        command=lambda: Hypothesis() )
        
        hypothesis1.grid(row=2, column=2)
        hypothesis_exit = Button(text="Проверка гипотез", width=50, command=lambda: self.remove_button(list_buttons))
        list_buttons = [hypothesis1, hypothesis_exit]
        hypothesis_exit.grid(row=2, column=1)

    def create_intergroup_variance(self):
        hypothesis1 = Button(text="Найдите среднее значение и дисперсию признака во всей совокупности", width=50,
                             command=lambda: Intergroup_Variance())

        hypothesis1.grid(row=3, column=2)
        hypothesis_exit = Button(text="Межгрупповая дисперссия", width=50, command=lambda: self.remove_button(list_buttons))
        list_buttons = [hypothesis1, hypothesis_exit]
        hypothesis_exit.grid(row=3, column=1)

    def create_rep_non_rep_samp(self):
        hypothesis1 = Button(text="(Бесповторная выборка) Мат ожидание и дисперсию среднего значения", width=50,
                             command=lambda: Non_rep_Samp())

        hypothesis1.grid(row=4, column=2)
        hypothesis2 = Button(text="(Повторная выборка) Мат ожидание и дисперсию среднего значения", width=50,
                             command=lambda: Rep_Saml())

        hypothesis2.grid(row=5, column=2)
        hypothesis_exit = Button(text="Повторная и бесповторная выборка", width=50,
                                 command=lambda: self.remove_button(list_buttons))
        list_buttons = [hypothesis1, hypothesis2, hypothesis_exit]
        hypothesis_exit.grid(row=4, column=1)

    def create_point_stat_estimates(self):
        hypothesis1 = Button(text="Найдите несмещенную оценку дисперсии ошибок измерений", width=50,
                             command=lambda: Point_stat_estimates())

        hypothesis1.grid(row=5, column=2)
        hypothesis_exit = Button(text="Точечные статистические оценки", width=50, command=lambda: self.remove_button(list_buttons))
        list_buttons = [hypothesis1, hypothesis_exit]
        hypothesis_exit.grid(row=5, column=1)

    def create_sampl_distribution(self):
        hypothesis1 = Button(text="Вероятность равенства функций", width=50,
                             command=lambda: Sampl_distribution())

        hypothesis1.grid(row=6, column=2)
        hypothesis_exit = Button(text="Выборки из распределния", width=50,
                                 command=lambda: self.remove_button(list_buttons))
        list_buttons = [hypothesis1, hypothesis_exit]
        hypothesis_exit.grid(row=6, column=1)



    def dover_(self):
        pass


# download_icon = tk.PhotoImage(file='./assets/download.png')

program = MainMenu()
