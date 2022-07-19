from tkinter import Tk, StringVar
from tkinter.ttk import *
import tkinter as tk
from tkinter import font as tkfont
from tkinter import filedialog
import tkinter.messagebox as msb
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import scipy.special as ssp
import matplotlib.pyplot as plt
import scipy.stats as ss
import pandas as pd
from okna_GUI import *
import sys


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine, PageTen, PageEleven, PageTwelve):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # główne okno
        self.frame = Frame(self)
        self.frame.grid(row=0, column=0, padx=10, pady=5)

        # lewe okno
        self.data_choose_label = Label(self.frame, text="Wybierz szereg czasowy", font=("Times New Roman", 20),
                                       background='yellow')
        self.data_choose_label.grid(row=0, column=0, padx=10, pady=5)
        self.data = None
        self.button = Button(self.frame, text="Otwórz plik", command=self.openFile)
        self.button.grid(row=1, column=0, padx=20)

        self.fig2 = Figure(figsize=(4, 3), dpi=100)
        self.canvas2 = FigureCanvasTkAgg(self.fig2, self.frame)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().grid(row=1, rowspan=10, column=0, padx=10, pady=5)

        self.statistics = Label(self.frame, text="Podstawowe\nstatystyki", font=("Times New Roman", 15),
                                background='yellow')
        self.statistics.grid(row=0, column=1, padx=10, pady=5)

        self.length_ = StringVar()
        self.length_.set("Ilość\nobserwacji:")
        self.length = Label(self.frame, textvariable=self.length_)
        self.length.grid(row=1, column=1, padx=10, pady=5)

        self.mean_ = StringVar()
        self.mean_.set("Średnia:")
        self.mean = Label(self.frame, textvariable=self.mean_)
        self.mean.grid(row=3, column=1, padx=10, pady=5)

        self.var_ = StringVar()
        self.var_.set("Wariancja:")
        self.var = Label(self.frame, textvariable=self.var_)
        self.var.grid(row=5, column=1, padx=10, pady=5)

        self.distance_ = StringVar()
        self.distance_.set("Rostęp:")
        self.distance = Label(self.frame, textvariable=self.distance_)
        self.distance.grid(row=7, column=1, padx=10, pady=5)

        # środkowe okno
        self.choose_method_label = Label(self.frame, text="Wybierz estymator", font=("Times New Roman", 20),
                                       background='yellow')
        self.choose_method_label.grid(row=0, column=2, columnspan=2,padx=10, pady=5)

        self.autocorr_label = StringVar()
        self.autocorr = Checkbutton(self.frame, text="Autocorr", variable=self.autocorr_label,
                                    offvalue="autocorr-off", onvalue="autocorr-on")
        self.autocorr.grid(row=1, column=2)
        self.autocorr_label.set("autocorr-off")

        self.autocorr1_label = StringVar()
        self.autocorr1 = Checkbutton(self.frame, text="Autocorr1", variable=self.autocorr1_label,
                                    offvalue="autocorr1-off", onvalue="autocorr1-on")
        self.autocorr1.grid(row=2, column=2)
        self.autocorr1_label.set("autocorr1-off")

        self.autocorr2_label = StringVar()
        self.autocorr2 = Checkbutton(self.frame, text="Autocorr2", variable=self.autocorr2_label,
                                     offvalue="autocorr2-off", onvalue="autocorr2-on")
        self.autocorr2.grid(row=3, column=2)
        self.autocorr2_label.set("autocorr2-off")

        self.autocorr3_label = StringVar()
        self.autocorr3 = Checkbutton(self.frame, text="Autocorr3", variable=self.autocorr3_label,
                                     offvalue="autocorr3-off", onvalue="autocorr3-on")
        self.autocorr3.grid(row=4, column=2)
        self.autocorr3_label.set("autocorr3-off")

        self.autocorr4_label = StringVar()
        self.autocorr4 = Checkbutton(self.frame, text="Autocorr4", variable=self.autocorr4_label,
                                     offvalue="autocorr4-off", onvalue="autocorr4-on")
        self.autocorr4.grid(row=5, column=2)
        self.autocorr4_label.set("autocorr4-off")

        self.autocorr5_label = StringVar()
        self.autocorr5 = Checkbutton(self.frame, text="Autocorr5", variable=self.autocorr5_label,
                                     offvalue="autocorr5-off", onvalue="autocorr5-on")
        self.autocorr5.grid(row=6, column=2)
        self.autocorr5_label.set("autocorr5-off")

        self.autocorr6_label = StringVar()
        self.autocorr6 = Checkbutton(self.frame, text="Autocorr6", variable=self.autocorr6_label,
                                     offvalue="autocorr6-off", onvalue="autocorr6-on")
        self.autocorr6.grid(row=7, column=2)
        self.autocorr6_label.set("autocorr6-off")

        self.autocorr7_label = StringVar()
        self.autocorr7 = Checkbutton(self.frame, text="Autocorr7", variable=self.autocorr7_label,
                                     offvalue="autocorr7-off", onvalue="autocorr7-on")
        self.autocorr7.grid(row=8, column=2)
        self.autocorr7_label.set("autocorr7-off")

        self.autocorr8_label = StringVar()
        self.autocorr8 = Checkbutton(self.frame, text="Autocorr8", variable=self.autocorr8_label,
                                     offvalue="autocorr8-off", onvalue="autocorr8-on")
        self.autocorr8.grid(row=9, column=2)
        self.autocorr8_label.set("autocorr8-off")

        self.autocorr9_label = StringVar()
        self.autocorr9 = Checkbutton(self.frame, text="Autocorr9", variable=self.autocorr9_label,
                                     offvalue="autocorr9-off", onvalue="autocorr9-on")
        self.autocorr9.grid(row=10, column=2)
        self.autocorr9_label.set("autocorr9-off")

        self.autocorr10_label = StringVar()
        self.autocorr10 = Checkbutton(self.frame, text="Autocorr10", variable=self.autocorr10_label,
                                     offvalue="autocorr10-off", onvalue="autocorr10-on")
        self.autocorr10.grid(row=11, column=2)
        self.autocorr10_label.set("autocorr10-off")

        self.details = Button(self.frame, text="Szczegóły", command=lambda: controller.show_frame("PageTwo"))
        self.details.grid(row=1, column=3)

        self.details1 = Button(self.frame, text="Szczegóły", command=lambda: controller.show_frame("PageThree"))
        self.details1.grid(row=2, column=3)

        self.details2 = Button(self.frame, text="Szczegóły", command=lambda: controller.show_frame("PageFour"))
        self.details2.grid(row=3, column=3)

        self.details3 = Button(self.frame, text="Szczegóły", command=lambda: controller.show_frame("PageFive"))
        self.details3.grid(row=4, column=3)

        self.details4 = Button(self.frame, text="Szczegóły", command=lambda: controller.show_frame("PageSix"))
        self.details4.grid(row=5, column=3)

        self.details5 = Button(self.frame, text="Szczegóły", command=lambda: controller.show_frame("PageSeven"))
        self.details5.grid(row=6, column=3)

        self.details6 = Button(self.frame, text="Szczegóły", command=lambda: controller.show_frame("PageEight"))
        self.details6.grid(row=7, column=3)

        self.details7 = Button(self.frame, text="Szczegóły", command=lambda: controller.show_frame("PageNine"))
        self.details7.grid(row=8, column=3)

        self.details8 = Button(self.frame, text="Szczegóły", command=lambda: controller.show_frame("PageTen"))
        self.details8.grid(row=9, column=3)

        self.details9 = Button(self.frame, text="Szczegóły", command=lambda: controller.show_frame("PageEleven"))
        self.details9.grid(row=10, column=3)

        self.details10 = Button(self.frame, text="Szczegóły", command=lambda: controller.show_frame("PageTwelve"))
        self.details10.grid(row=11, column=3)

        # środkowe okno

        self.tools_label = Label(self.frame, text="Narzędzia", font=("Times New Roman", 20),
                                background='yellow')
        self.tools_label.grid(row=0, column=4, padx=10, pady=5)
        self.draw_button = Button(self.frame, text="Rysuj wykres", command=self.draw_graph)
        self.draw_button.grid(row=1, column=4, padx=10, pady=5)

        self.lag_label = Label(self.frame, text="Końcowy numer\nopóźnienia")
        self.lag_label.grid(row=2, column=4, padx=10, pady=5)

        self.lag_entry = Entry(self.frame, width=5)
        self.lag_entry.grid(row=3, column=4, padx=10, pady=5)

        self.counting_ = StringVar()
        self.counting_.set("")
        self.counting = Label(self.frame, textvariable=self.counting_)
        self.counting.grid(row=5, column=4, padx=10, pady=5)

        self.exit = Button(self.frame, text="Zakończ", command=sys.exit)
        self.exit.grid(row=11, column=4, padx=10, pady=5)


        # prawe okno
        self.plot_label = Label(self.frame, text="Wykres autokorelacji", font=("Times New Roman", 20),
                                background='yellow')
        self.plot_label.grid(row=0, column=5, padx=10, pady=5)
        self.fig = Figure(figsize=(6, 4.4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, rowspan=11, column=5, padx=10, pady=5)

        # inne zmienne
        self.X = None
        self.lag = [0, 5]
        self.autocov = None
        self.autocorr = None
        self.autocov1 = None
        self.autocorr1 = None
        self.autocov2 = None
        self.autocorr2 = None
        self.autocorr4 = None
        self.autocorr3 = None
        self.autocorr5 = None
        self.autocorr6 = None
        self.autocorr7 = None
        self.autocorr8 = None
        self.autocorr9 = None
        self.autocorr10 = None

    def openFile(self):
        try:
            self.tf = filedialog.askopenfilename(
                initialdir="C:/Users/MainFrame/Desktop/",
                title="Open Text file",
                filetypes=(("Text Files", "*.txt"),)
            )
            self.tf = open(self.tf)  # or tf = open(tf, 'r')
            self.data = self.tf.read()
            self.tf.close()
            self.data_processing()
            self.draw_time_series()
            self.length_.set(f"Ilość\nobserwacji:\n{round(len(self.X), 5)}")
            self.mean_.set(f"Średnia:\n{round(np.mean(self.X), 5)}")
            self.var_.set(f"Wariancja:\n{round(np.var(self.X), 5)}")
            self.distance_.set(f"Rostęp:\n{round(max(self.X) - min(self.X), 5)}")
        except:
            pass

    def data_processing(self):
        self.X = [float(i) for i in self.data.split("\n")]

    def draw_time_series(self):
        self.fig2 = Figure(figsize=(4, 3), dpi=100)
        self.figure2 = self.fig2.add_subplot()
        self.figure2.grid(True)
        self.figure2.plot(self.X)
        self.figure2.set_title("Szereg czasowy")
        self.canvas2 = FigureCanvasTkAgg(self.fig2, self.frame)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().grid(row=2, rowspan=11, column=0, padx=10, pady=5)

    def fautocov(self, X, lag):
        self.autocov = [1 / len(X) * (np.sum((np.array(X[:len(X) - i]) - np.mean(X)) * \
                        (np.array(X[i:]) - np.mean(X)))) for i in range(lag[0], lag[1] + 1)]
        return self.autocov

    def fautocorr(self, X, lag):
        self.fautocov(self.X, self.lag)
        self.autocorr = [i / self.fautocov(X, [0, 1])[0] for i in self.fautocov(X, lag)]

    def Q(self, X, k=2.2191):
        values = [abs(X[j] - X[i]) for i in range(len(X)) for j in range(i)]
        values = sorted(values)
        return k * values[int(np.floor((ssp.binom(len(X), 2) + 2) / 4))]

    def autocov1(self, X, lag, k):
        acvf = []
        for h in range(lag[0], lag[1] + 1):
            if h == 0:
                u = np.array(X)
            else:
                u = np.array(X[:-h])
            v = np.array(X[h:])
            acvf.append(1 / 4 * ((self.Q(u + v, k)) ** 2 - (self.Q(u - v, k)) ** 2))
        return acvf

    def fautocorr1(self, X, lag, k=2.2191):
        self.autocorr1 = []
        for h in range(lag[0], lag[1] + 1):
            if h == 0:
                u = np.array(X)
            else:
                u = np.array(X[:-h])
            v = np.array(X[h:])
            self.autocorr1.append(((self.Q(u + v, k)) ** 2 - (self.Q(u - v, k)) ** 2) / ((self.Q(u + v, k)) ** 2 + (self.Q(u - v, k)) ** 2))

    def g(self, n, alfa=0.015):
        return int(np.floor(n * alfa))

    def L(self, X, t, alfa):
        Y = sorted(X)
        n = len(X)
        _g = self.g(n, alfa)
        if Y[_g] < X[t] and X[t] < Y[n - _g]:
            return 1
        return 0

    def mean_X(self, X, alfa=0.015):
        suma1 = sum([self.L(X, i, alfa) for i in range(len(X))])
        suma2 = sum([X[i] * self.L(X, i, alfa) for i in range(len(X))])
        return 1 / suma1 * suma2

    def fautocov2(self, X, lag, alfa=0.015):
        n = len(X)
        L_vector = [self.L(X, i, alfa) for i in range(n)]
        acvf = []
        for h in range(lag[0], lag[1] + 1):
            if h == 0:
                suma1 = sum(L_vector)
                suma2 = sum(np.array(X) ** 2 * np.array(L_vector))
            else:
                suma1 = sum(np.array(L_vector[:-h]) * np.array(L_vector[h:]))
                suma2 = sum(np.array(np.array(X[:-h]) - self.mean_X(X, alfa)) * np.array(np.array(X[h:]) - self.mean_X(X, alfa)) * np.array(L_vector[:-h]) * np.array(L_vector[h:]))
            acvf.append(suma2 / suma1)
        return acvf

    def fautocorr2(self, X, lag, alfa=0.015):
        acvf = self.fautocov2(X, lag, alfa)[0]
        self.autocorr2 = [i / acvf for i in self.fautocov2(X, lag, alfa)]

    def fautocorr4(self, X, lag):
        X = np.array(X) - np.mean(X)
        self.autocorr4 = [1.0]
        denominator = np.median([i**2 for i in X])
        for h in range(lag[0] + 1, lag[1] + 1):
            self.autocorr4.append(np.median(np.array(X[:-h]) * np.array(X[h:]))/denominator)

    def J(self, x):
        return ss.norm.ppf(x)

    def c(self, X):
        n = len(X)
        R = sorted(X)
        return 1 / np.sum([(self.J((list(X).index(R[i]) + 1) / (n + 1)))**2 for i in range(n)])

    def fautocorr3(self, X, lag):
        self.autocorr3 = []
        n = len(X)
        R = sorted(X)
        for h in range(lag[0], lag[1] + 1):
            suma = 0
            for i in range(n-h):
                suma += self.J((R.index(list(X)[i]) + 1)/ (n+1)) * self.J((R.index(list(X)[i + h]) + 1)/ (n+1))
            self.autocorr3.append(self.c(X) * suma)

    def fautocorr5(self, X, lag):
        n = len(X)
        self.autocorr5 = [2/((n - h)*(n - h - 1)) * np.sum([np.sign((X[i] - X[j]) * (X[i + h] - X[j + h]))
                            for i in range(n - h) for j in range(i)]) for h in range(lag[0], lag[1] + 1)]

    def fautocorr6(self, X, lag):
        n = len(X)
        mediana = np.median(X)
        acf = [1/(n - h) * np.sum(np.sign((np.array(X[:-h]) - mediana) *
                                      (np.array(X[h:]) - mediana))) for h in range(lag[0] + 1, lag[1] + 1)]
        self.autocorr6 = [1, *acf]

    def zmatrix(self, X, k):
        n = len(X)
        return np.matrix([[*[0 for i in range(j)], *[X[i] for i in range(n)], *[0 for i in range(k - j)]] for j in range(k+1)])

    def gamma_k(self, X, k):
        z_matr = self.zmatrix(X, k)
        return (z_matr * z_matr.transpose())/len(X)

    def Xi(self, X, k, i, j):
        gamm = self.gamma_k(X, k)
        return gamm[i - 1, j - 1]/np.sqrt(gamm[i - 1, i - 1] * gamm[j - 1, j - 1])

    def fautocorr7(self, X, lag):
        k = lag[1]
        self.autocorr7 = [1/(k - h + 1)*sum([self.Xi(X, k, i, i + h) for i in range(1, k - h + 2)]) for h in range(lag[0], lag[1] + 1)]

    def fautocorr8(self, X, lag):
        X = np.array(X)
        self.autocorr8 = [(np.var(X+X) - np.var(X - X))/(np.var(X+X) + np.var(X - X)) if h == 0 else
                (np.var(X[h:]+X[:-h]) - np.var(X[h:] - X[:-h]))/(np.var(X[h:]+X[:-h]) + np.var(X[h:] - X[:-h]))
                for h in range(lag[0], lag[1] + 1)]

    def MAD2(self, X, const=1.4826):
        return (const * np.median([abs(i - np.median(X)) for i in X]))**2

    def IQR2(self, X, const=0.7413):
        return (const * (np.quantile(X, 0.75) - np.quantile(X, 0.25)))**2

    def fautocorr9(self, X, lag):
        X = np.array(X)
        self.autocorr9 = [(self.MAD2(X+X) - self.MAD2(X - X))/(self.MAD2(X+X) + self.MAD2(X - X)) if h == 0 else
                (self.MAD2(X[h:]+X[:-h]) - self.MAD2(X[h:] - X[:-h]))/(self.MAD2(X[h:]+X[:-h]) + self.MAD2(X[h:] - X[:-h]))
                for h in range(lag[0], lag[1] + 1)]

    def fautocorr10(self, X, lag):
        X = np.array(X)
        self.autocorr10 = [(self.IQR2(X+X) - self.IQR2(X - X))/(self.IQR2(X+X) + self.IQR2(X - X)) if h == 0 else
                (self.IQR2(X[h:]+X[:-h]) - self.IQR2(X[h:] - X[:-h]))/(self.IQR2(X[h:]+X[:-h]) + self.IQR2(X[h:] - X[:-h]))
                for h in range(lag[0], lag[1] + 1)]


    def draw_graph(self):
        if self.X == None:
            msb.showerror("Brak danych", "Wybierz dane")
            return
        self.counting_.set("Obliczanie...")
        self.update()
        self.lag = self.lag_entry.get()
        if self.lag == "":
            self.lag_entry.insert(0, "5")
            self.lag = self.lag_entry.get()
        try:
            self.lag =[0, int(self.lag)]
        except:
            msb.showinfo("Błędny numer opóźnienia", "Wprowadzono błędny numer opóźnienia\nNależy wpisać liczbę naturalną\nalbo zostawić puste pole")
            return
        acorrs = []
        labels = []
        self.fig = Figure(figsize=(6, 4.4), dpi=100)
        self.figure = self.fig.add_subplot()
        self.figure.grid(True)
        if self.autocorr_label.get() == "autocorr-on":
            acorrs.append("a")
            self.fautocorr(self.X, self.lag)
            for i in range(len(self.autocorr)):
                labels.append(self.figure.scatter(i, self.autocorr[i], c="blue"))
        if self.autocorr1_label.get() == "autocorr1-on":
            acorrs.append("a1")
            self.fautocorr1(self.X, self.lag)
            for i in range(len(self.autocorr1)):
                labels.append(self.figure.scatter(i, self.autocorr1[i], c="orange"))
        if self.autocorr2_label.get() == "autocorr2-on":
            acorrs.append("a2")
            self.fautocorr2(self.X, self.lag)
            for i in range(len(self.autocorr2)):
                labels.append(self.figure.scatter(i, self.autocorr2[i], c="green"))
        if self.autocorr3_label.get() == "autocorr3-on":
            acorrs.append("a3")
            self.fautocorr3(self.X, self.lag)
            for i in range(len(self.autocorr3)):
                labels.append(self.figure.scatter(i, self.autocorr3[i], c="red"))
        if self.autocorr4_label.get() == "autocorr4-on":
            acorrs.append("a4")
            self.fautocorr4(self.X, self.lag)
            for i in range(len(self.autocorr4)):
                labels.append(self.figure.scatter(i, self.autocorr4[i], c="purple"))
        if self.autocorr5_label.get() == "autocorr5-on":
            acorrs.append("a5")
            self.fautocorr5(self.X, self.lag)
            for i in range(len(self.autocorr5)):
                labels.append(self.figure.scatter(i, self.autocorr5[i], c="brown"))
        if self.autocorr6_label.get() == "autocorr6-on":
            acorrs.append("a6")
            self.fautocorr6(self.X, self.lag)
            for i in range(len(self.autocorr6)):
                labels.append(self.figure.scatter(i, self.autocorr6[i], c="pink"))
        if self.autocorr7_label.get() == "autocorr7-on":
            acorrs.append("a7")
            self.fautocorr7(self.X, self.lag)
            for i in range(len(self.autocorr7)):
                labels.append(self.figure.scatter(i, self.autocorr7[i], c="gray"))
        if self.autocorr8_label.get() == "autocorr8-on":
            acorrs.append("a8")
            self.fautocorr8(self.X, self.lag)
            for i in range(len(self.autocorr8)):
                labels.append(self.figure.scatter(i, self.autocorr8[i], c="black"))
        if self.autocorr9_label.get() == "autocorr9-on":
            acorrs.append("a9")
            self.fautocorr9(self.X, self.lag)
            for i in range(len(self.autocorr9)):
                labels.append(self.figure.scatter(i, self.autocorr9[i], c="cyan"))
        if self.autocorr10_label.get() == "autocorr10-on":
            acorrs.append("a10")
            self.fautocorr10(self.X, self.lag)
            for i in range(len(self.autocorr10)):
                labels.append(self.figure.scatter(i, self.autocorr10[i], c="magenta"))
        self.figure.legend([labels[i] for i in range(0, len(labels), self.lag[1] + 1)] ,(acorrs))
        if self.autocorr_label.get() == "autocorr-on":
            for i in range(len(self.autocorr)):
                self.figure.plot([i, i], [0, self.autocorr[i]], "blue")
        if self.autocorr1_label.get() == "autocorr1-on":
            for i in range(len(self.autocorr1)):
                self.figure.plot([i, i], [0, self.autocorr1[i]], "orange")
        if self.autocorr2_label.get() == "autocorr2-on":
            for i in range(len(self.autocorr2)):
                self.figure.plot([i, i], [0, self.autocorr2[i]], "green")
        if self.autocorr3_label.get() == "autocorr3-on":
            for i in range(len(self.autocorr3)):
                self.figure.plot([i, i], [0, self.autocorr3[i]], "red")
        if self.autocorr4_label.get() == "autocorr4-on":
            for i in range(len(self.autocorr4)):
                self.figure.plot([i, i], [0, self.autocorr4[i]], "purple")
        if self.autocorr5_label.get() == "autocorr5-on":
            for i in range(len(self.autocorr5)):
                self.figure.plot([i, i], [0, self.autocorr5[i]], "brown")
        if self.autocorr6_label.get() == "autocorr6-on":
            for i in range(len(self.autocorr6)):
                self.figure.plot([i, i], [0, self.autocorr6[i]], "pink")
        if self.autocorr7_label.get() == "autocorr7-on":
            for i in range(len(self.autocorr7)):
                self.figure.plot([i, i], [0, self.autocorr7[i]], "gray")
        if self.autocorr8_label.get() == "autocorr8-on":
            for i in range(len(self.autocorr8)):
                self.figure.plot([i, i], [0, self.autocorr8[i]], "black")
        if self.autocorr9_label.get() == "autocorr9-on":
            for i in range(len(self.autocorr9)):
                self.figure.plot([i, i], [0, self.autocorr9[i]], "cyan")
        if self.autocorr10_label.get() == "autocorr10-on":
            for i in range(len(self.autocorr10)):
                self.figure.plot([i, i], [0, self.autocorr10[i]], "magenta")

        self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, rowspan=11, column=5)
        self.counting_.set("")



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()