from tkinter.ttk import *
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from GUI2 import *


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.estimator_label = Label(self.frame, text="Klasyczny estymator", font=("Times New Roman", 20),
                                     background='yellow')
        self.estimator_label.grid(row=0, column=0, padx=10, pady=5)

        self.fig = Figure(figsize=(12, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.label = Label(self.frame)
        self.label.grid(row=1, column=0, padx=10, pady=5)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)
        self.canvas._tkcanvas.grid(row=1, column=0, padx=10, pady=5)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.text = "$\hat{\gamma}(h)=\\frac{1}{n}{\sum_{i=1}^{n-h}{\left(X_t-\overline{X}\\right)\left(X_{t+h}-\overline{X}\\right)}}, \quad h\in\mathbb{N}$\n\
Prosty estymator autokorelacji: $\hat{\\rho}(h)=\\frac{\hat{\gamma}(h)}{\hat{\gamma}(0)}, \quad h\in\mathbb{N}$"
        self.wx.clear()
        self.wx.text(0.25, 0.25, self.text, fontsize=15)
        self.canvas.draw()
        self.back = Button(self.frame, text="Wróć", command=lambda: controller.show_frame("StartPage"))
        self.back.grid(row=2, column=0, padx=10, pady=5)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.estimator_label = Label(self.frame, text="Estymator oparty na statystyce Q", font=("Times New Roman", 20),
                                     background='yellow')
        self.estimator_label.grid(row=0, column=0, padx=10, pady=5)

        self.fig = Figure(figsize=(12, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.label = Label(self.frame)
        self.label.grid(row=1, column=0, padx=10, pady=5)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)
        self.canvas._tkcanvas.grid(row=1, column=0, padx=10, pady=5)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.text = "Statystyka $Q$.\n\
$Q_n(x)=\kappa\\times\{|x_j-x_k|; j<k\}_{(\\tau)}$\n\
$\hat{\gamma}_{Q_N}(h)=\\frac{1}{4}\left[Q_{N-h}^2(\mathbb{u} + \mathbb{v}) - Q_{N-h}^2{(\mathbb{u}-\mathbb{v}})\\right]$,\n\
gdzie wektory $u$ i $v$ to odpowiednio początkowe $N-h$\ni końcowe $N-h$ wartości wektora $X$.\n\
$\hat{\\rho}_{Q_N}(h)=\\frac{Q_{N-h}^2(\mathbb{u} + \mathbb{v}) - Q_{N-h}^2{(\mathbb{u}-\mathbb{v}})}{Q_{N-h}^2(\mathbb{u} + \mathbb{v}) + Q_{N-h}^2{(\mathbb{u}-\mathbb{v}})}$"
        self.wx.clear()
        self.wx.text(0.1, 0.25, self.text, fontsize=15)
        self.canvas.draw()
        self.back = Button(self.frame, text="Wróć", command=lambda: controller.show_frame("StartPage"))
        self.back.grid(row=2, column=0, padx=10, pady=5)

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.estimator_label = Label(self.frame, text="Estymator oparty na podstawie\nprzekształeń jednowymiarowych", font=("Times New Roman", 20),
                                     background='yellow')
        self.estimator_label.grid(row=0, column=0, padx=10, pady=5)

        self.fig = Figure(figsize=(12, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.label = Label(self.frame)
        self.label.grid(row=1, column=0, padx=10, pady=5)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)
        self.canvas._tkcanvas.grid(row=1, column=0, padx=10, pady=5)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.text = "$\hat{\gamma}_{Q_n}=\\frac{1}{\sum_{t=1}^{n-h}{L_t^{(\\alpha)}L_{t+h}^{(\\alpha)}}}\left\{\sum_{t=1}^{n-h}\left(X_t-\overline{X}^{(\\alpha)}\\right)\left(X_{t+h}-\overline{X}^{(\\alpha)}\\right)L_t^{(\\alpha)}L_{t+h}^{(\\alpha)}\\right\}$" \
                    "\ngdzie:" \
                    "\n$\overline{X}^{(\\alpha)}=\\frac{1}{\sum_{t=1}^nL_t^{(\\alpha)}}\sum_{t=1}^n{X_tL_t^{(\\alpha)}}$" \
                    "\n$L_t^{(\\alpha)}=1,\quad iff\quadX_{(g)} < X_t < X_{(n-g+1)}, \quad 0\quad$ poza tym"
        self.wx.clear()
        self.wx.text(0.1, 0.2, self.text, fontsize=15)
        self.canvas.draw()
        self.back = Button(self.frame, text="Wróć", command=lambda: controller.show_frame("StartPage"))
        self.back.grid(row=2, column=0, padx=10, pady=5)

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.estimator_label = Label(self.frame, text="Estymator oparty na\nscentralizowanym szeregu czasowym", font=("Times New Roman", 20),
                                     background='yellow')
        self.estimator_label.grid(row=0, column=0, padx=10, pady=5)

        self.fig = Figure(figsize=(12, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.label = Label(self.frame)
        self.label.grid(row=1, column=0, padx=10, pady=5)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)
        self.canvas._tkcanvas.grid(row=1, column=0, padx=10, pady=5)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.text = "$\hat{\\rho}(h)=c\sum_{i=1}^{n-h}J\left(\\frac{R_i}{n+1}\\right)\cdot J\left(\\frac{R_{i+h}}{n+1}\\right)}\,\quad$\ngdzie:" \
                    "\n$c=\\frac{1}{\sum_{i=1}^nJ\left(\\frac{R_i}{n+1}\\right)^2}$," \
                    "\n$J(x) = \Phi^{-1}(x), x\in(0, 1)$"
        self.wx.clear()
        self.wx.text(0.3, 0.25, self.text, fontsize=15)
        self.canvas.draw()
        self.back = Button(self.frame, text="Wróć", command=lambda: controller.show_frame("StartPage"))
        self.back.grid(row=2, column=0, padx=10, pady=5)

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.estimator_label = Label(self.frame, text="Estymator oparty na szacowaniu\nznaków i rang", font=("Times New Roman", 20),
                                     background='yellow')
        self.estimator_label.grid(row=0, column=0, padx=10, pady=5)

        self.fig = Figure(figsize=(12, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.label = Label(self.frame)
        self.label.grid(row=1, column=0, padx=10, pady=5)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)
        self.canvas._tkcanvas.grid(row=1, column=0, padx=10, pady=5)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.text = "$\hat{\\rho}(h)=\\frac{med{\left(\\tilde{X_i}\\tilde{X}_{1+h},\dots, \\tilde{X}_{n-h}\\tilde{X_n}\\right)}}{med{\left(\\tilde{X_1^2},\dots, \\tilde{X_n^2}\\right)}}$"
        self.wx.clear()
        self.wx.text(0.2, 0.6, self.text, fontsize=15)
        self.canvas.draw()
        self.back = Button(self.frame, text="Wróć", command=lambda: controller.show_frame("StartPage"))
        self.back.grid(row=2, column=0, padx=10, pady=5)

class PageSeven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.estimator_label = Label(self.frame, text="Estymator oparty na znakach", font=("Times New Roman", 20),
                                     background='yellow')
        self.estimator_label.grid(row=0, column=0, padx=10, pady=5)

        self.fig = Figure(figsize=(12, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.label = Label(self.frame)
        self.label.grid(row=1, column=0, padx=10, pady=5)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)
        self.canvas._tkcanvas.grid(row=1, column=0, padx=10, pady=5)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.text = "$\hat{\\rho}(h)=\\frac{1}{(n-h)(n-h-1)}\sum_{i>j}sign((X_i-X_j)(X_{i+h}-X_{j+h}))$"
        self.wx.clear()
        self.wx.text(0.2, 0.6, self.text, fontsize=15)
        self.canvas.draw()
        self.back = Button(self.frame, text="Wróć", command=lambda: controller.show_frame("StartPage"))
        self.back.grid(row=2, column=0, padx=10, pady=5)

class PageEight(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.estimator_label = Label(self.frame, text="Estymator oparty na znakach", font=("Times New Roman", 20),
                                     background='yellow')
        self.estimator_label.grid(row=0, column=0, padx=10, pady=5)

        self.fig = Figure(figsize=(12, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.label = Label(self.frame)
        self.label.grid(row=1, column=0, padx=10, pady=5)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)
        self.canvas._tkcanvas.grid(row=1, column=0, padx=10, pady=5)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.text = "$\hat{\\rho}(h)=\\frac{1}{n-h}\sum_{i=1}^{n-h}sign((X_i-\hat\mu)(X_{i+h} - \hat\mu))$" \
                    "\n gdzie: $\hat\mu$ to mediana szeregu $X$"
        self.wx.clear()
        self.wx.text(0.3, 0.3, self.text, fontsize=15)
        self.canvas.draw()
        self.back = Button(self.frame, text="Wróć", command=lambda: controller.show_frame("StartPage"))
        self.back.grid(row=2, column=0, padx=10, pady=5)


class PageNine(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.estimator_label = Label(self.frame, text="Estymator oparty na korelacji wielowymiarowej", font=("Times New Roman", 20),
                                     background='yellow')
        self.estimator_label.grid(row=0, column=0, padx=10, pady=5)

        self.fig = Figure(figsize=(12, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.label = Label(self.frame)
        self.label.grid(row=1, column=0, padx=10, pady=5)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)
        self.canvas._tkcanvas.grid(row=1, column=0, padx=10, pady=5)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.text = "$\Xi_{i, j}^{(k)}=\\frac{\Gamma_{i, j}^{(k)}}{\sqrt{\Gamma_{i, i}^{(k)}\cdot\Gamma_{j, j}^{(k)}}}$" \
                    "\n$\Gamma^{(k)}=\\frac{Z_k'Z_k}{n}$" \
                    "\n gdzie $Z_k$ to pewna macierz" \
                    "\n$\hat\\rho(h)=\\frac{1}{k-h+1}\sum_{i=1}^{k-h+1}\hat\Xi^{(k)}_{i, i+h}$"
        self.wx.clear()
        self.wx.text(0.2, 0.3, self.text, fontsize=15)
        self.canvas.draw()
        self.back = Button(self.frame, text="Wróć", command=lambda: controller.show_frame("StartPage"))
        self.back.grid(row=2, column=0, padx=10, pady=5)


class PageTen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.estimator_label = Label(self.frame, text="Estymator oparty na wariancjach", font=("Times New Roman", 20),
                                     background='yellow')
        self.estimator_label.grid(row=0, column=0, padx=10, pady=5)

        self.fig = Figure(figsize=(12, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.label = Label(self.frame)
        self.label.grid(row=1, column=0, padx=10, pady=5)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)
        self.canvas._tkcanvas.grid(row=1, column=0, padx=10, pady=5)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.text = "$\\rho(h)=\\frac{Var(X_{t+h}+X_t) - Var(X_{t+h}-X_t)}{Var(X_{t+h}+X_t) + Var(X_{t+h}-X_t)}$"
        self.wx.clear()
        self.wx.text(0.2, 0.6, self.text, fontsize=15)
        self.canvas.draw()
        self.back = Button(self.frame, text="Wróć", command=lambda: controller.show_frame("StartPage"))
        self.back.grid(row=2, column=0, padx=10, pady=5)


class PageEleven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.estimator_label = Label(self.frame, text="Estymator oparty na MAD\n(median absolute deviance)", font=("Times New Roman", 20),
                                     background='yellow')
        self.estimator_label.grid(row=0, column=0, padx=10, pady=5)

        self.fig = Figure(figsize=(12, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.label = Label(self.frame)
        self.label.grid(row=1, column=0, padx=10, pady=5)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)
        self.canvas._tkcanvas.grid(row=1, column=0, padx=10, pady=5)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.text = "$MAD=1.4826\cdot med\{|x_i-x_{med}|;i=1,\dots,n\}$" \
                    "\n$\\rho(h)=\\frac{MAD(X_{t+h}+X_t) - MAD(X_{t+h}-X_t)}{MAD(X_{t+h}+X_t) + MAD(X_{t+h}-X_t)}$"
        self.wx.clear()
        self.wx.text(0.2, 0.6, self.text, fontsize=15)
        self.canvas.draw()
        self.back = Button(self.frame, text="Wróć", command=lambda: controller.show_frame("StartPage"))
        self.back.grid(row=2, column=0, padx=10, pady=5)

class PageTwelve(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")
        self.estimator_label = Label(self.frame, text="Estymator oparty na IQR", font=("Times New Roman", 20),
                                     background='yellow')
        self.estimator_label.grid(row=0, column=0, padx=10, pady=5)

        self.fig = Figure(figsize=(12, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.label = Label(self.frame)
        self.label.grid(row=1, column=0, padx=10, pady=5)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)
        self.canvas._tkcanvas.grid(row=1, column=0, padx=10, pady=5)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.text = "$IQR=0.7413\cdot(Q_3-Q_1)$" \
                    "\n$\\rho(h)=\\frac{IQR(X_{t+h}+X_t) - IQR(X_{t+h}-X_t)}{IQR(X_{t+h}+X_t) + IQR(X_{t+h}-X_t)}$"
        self.wx.clear()
        self.wx.text(0.2, 0.6, self.text, fontsize=15)
        self.canvas.draw()
        self.back = Button(self.frame, text="Wróć", command=lambda: controller.show_frame("StartPage"))
        self.back.grid(row=2, column=0, padx=10, pady=5)