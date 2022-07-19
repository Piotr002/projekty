from tkinter import Tk, StringVar
from tkinter.ttk import *
import tkinter.messagebox as msb
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import *
import pydoc
import math

matplotlib.use('TkAgg')


class window():
    """Klasa generująca okienko do rysowania wykresów funkcji."""

    def __init__(self, master):
        """Klasa initująca położenie przycisków, pól do wpisywania tekstu, etykiet,
        przycisku kontrolnego oraz płótna do narysowania wykresu na okienku."""
        self.master = master
        # główne okno
        self.frame = Frame(self.master)
        self.frame.grid(row=0, column=0)

        # okno ze wzorem funkcji
        self.top_left_frame = Frame(self.frame)
        self.top_left_frame.pack()
        self.wzor_funkcji_text = Label(self.top_left_frame, text="Wzór funkcji", font=("Times New Roman", 20),
                                       background='yellow')
        self.wzor_funkcji_text.pack()
        self.text1 = StringVar()
        self.wzor_funkcji = Entry(self.top_left_frame, width=40, textvariable=self.text1)
        self.wzor_funkcji.pack()
        self.fige = matplotlib.figure.Figure(figsize=(4, 0.5), dpi=100)
        self.ax = self.fige.add_subplot(111)
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        self.can = FigureCanvasTkAgg(self.fige, master=self.top_left_frame)
        self.can.get_tk_widget().pack(expand=1)
        self.can._tkcanvas.pack(expand=1)

        # okno z przyciskami
        self.top_middle_frame1 = Frame(self.frame)
        self.top_middle_frame1.pack()
        self.x_button = Button(self.top_middle_frame1, text='x', command=self.add_x)
        self.x_button.grid(row=0, column=0, padx=5, pady=10)
        self.nawias1 = Button(self.top_middle_frame1, text='(', command=self.add_nawias1)
        self.nawias1.grid(row=0, column=1, padx=5, pady=10)
        self.nawias2 = Button(self.top_middle_frame1, text=')', command=self.add_nawias2)
        self.nawias2.grid(row=0, column=2, padx=5, pady=10)
        self.plus = Button(self.top_middle_frame1, text='+', command=self.add_plus)
        self.plus.grid(row=1, column=0, padx=5, pady=10)
        self.minus = Button(self.top_middle_frame1, text='-', command=self.add_minus)
        self.minus.grid(row=1, column=1, padx=5, pady=10)
        self.razy = Button(self.top_middle_frame1, text='*', command=self.add_razy)
        self.razy.grid(row=1, column=2, padx=5, pady=10)
        self.dzielenie = Button(self.top_middle_frame1, text='/', command=self.add_dzielenie)
        self.dzielenie.grid(row=2, column=0, padx=5, pady=10)
        self.potega = Button(self.top_middle_frame1, text='^', command=self.add_potega)
        self.potega.grid(row=2, column=1, padx=5, pady=10)
        self.exp = Button(self.top_middle_frame1, text='exp', command=self.add_exp)
        self.exp.grid(row=2, column=2, padx=5, pady=10)
        self.sin = Button(self.top_middle_frame1, text='sin', command=self.add_sin)
        self.sin.grid(row=3, column=0, padx=5, pady=10)
        self.cos = Button(self.top_middle_frame1, text='cos', command=self.add_cos)
        self.cos.grid(row=3, column=1, padx=5, pady=10)
        self.sqrt = Button(self.top_middle_frame1, text='√', command=self.add_sqrt)
        self.sqrt.grid(row=3, column=2, padx=5, pady=10)
        self.tg = Button(self.top_middle_frame1, text='tan', command=self.add_tg)
        self.tg.grid(row=4, column=0, padx=5, pady=10)
        self.ctg = Button(self.top_middle_frame1, text='cot', command=self.add_ctg)
        self.ctg.grid(row=4, column=1, padx=5, pady=10)
        self.abs = Button(self.top_middle_frame1, text='||', command=self.add_abs)
        self.abs.grid(row=4, column=2, padx=5, pady=10)
        self.log = Button(self.top_middle_frame1, text='log', command=self.add_log)
        self.log.grid(row=5, column=0, padx=5, pady=10)
        self.znak = Button(self.top_middle_frame1, text=';', command=self.add_znak)
        self.znak.grid(row=5, column=1, padx=5, pady=10)
        self.backspace = Button(self.top_middle_frame1, text="cofnij", command=self.add_backspace)
        self.backspace.grid(row=5, column=2, padx=5, pady=10)

        # okno z zakresami
        self.top_middle_frame2 = Frame(self.frame)
        self.top_middle_frame2.pack()
        self.minx_label = Label(self.top_middle_frame2, text='x min.')
        self.minx_label.grid(row=0, column=0)
        self.minx = Entry(self.top_middle_frame2, width=5)
        self.minx.grid(row=1, column=0, padx=20, pady=5)

        self.maxx_label = Label(self.top_middle_frame2, text='x max.')
        self.maxx_label.grid(row=0, column=1)
        self.maxx = Entry(self.top_middle_frame2, width=5)
        self.maxx.grid(row=1, column=1, padx=20, pady=5)

        self.miny_label = Label(self.top_middle_frame2, text='y min.')
        self.miny_label.grid(row=0, column=2)
        self.miny = Entry(self.top_middle_frame2, width=5)
        self.miny.grid(row=1, column=2, padx=20, pady=5)

        self.maxy_label = Label(self.top_middle_frame2, text='y max.')
        self.maxy_label.grid(row=0, column=3)
        self.maxy = Entry(self.top_middle_frame2, width=5)
        self.maxy.grid(row=1, column=3, padx=20, pady=5)

        # okno z nazwami osi i tytułem wykresu
        self.top_middle_frame3 = Frame(self.frame)
        self.top_middle_frame3.pack()
        self.title_label = Label(self.top_middle_frame3, text='Tytuł wykresu')
        self.title_label.grid(row=0, column=0)
        self.title = Entry(self.top_middle_frame3, width=20)
        self.title.grid(row=1, column=0, padx=5, pady=5)

        self.x_label = Label(self.top_middle_frame3, text="Podpis osi x")
        self.x_label.grid(row=0, column=1)
        self.x = Entry(self.top_middle_frame3, width=20)
        self.x.grid(row=1, column=1, padx=5, pady=5)

        self.y_label = Label(self.top_middle_frame3, text="Podpis osi y")
        self.y_label.grid(row=0, column=2)
        self.y = Entry(self.top_middle_frame3, width=20)
        self.y.grid(row=1, column=2, padx=5, pady=5)

        # okno z Przyciskami przelicz i zakończ
        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack()
        self.rysuj = Button(self.bottom_frame, text="Rysuj wykres", command=self.draw_graph)
        self.rysuj.grid(row=0, column=1, padx=10, pady=10)
        self.legend_label = StringVar()
        self.legenda = Checkbutton(self.bottom_frame, text="Legenda", variable=self.legend_label,
                                   offvalue='Bez legendy', onvalue='Z legendą')
        self.legend_label.set('Z legendą')
        self.legenda.grid(row=0, column=0, padx=10, pady=10)
        self.clean = Button(self.bottom_frame, text="Wyczyść", command=self.clean_)
        self.clean.grid(row=0, column=2, padx=10, pady=10)
        self.zakoncz = Button(self.bottom_frame, text="Zakończ", command=self.quit)
        self.zakoncz.grid(row=0, column=3, padx=10, pady=20)

        self.right_frame = Frame(master)
        self.right_frame.grid(row=0, column=1)
        self.text = Label(self.right_frame, text='Wykres funkcji', font=("Times New Roman", 20), background='yellow')
        self.text.grid(row=0, column=0)
        self.fig = Figure(figsize=(10, 5.7), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, self.right_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=10)
        self.master.bind_all('<Key>', self.keycodess)
        self.numbers = '1234567890'

    def quit(self):
        """Funkcja kończąca pracę okienka."""

        import sys
        sys.exit()

    def clean_(self):
        """Funkcja czyszcząca wszyskie pola (wraz z płótnem do rysowania wykresu)."""

        self.wzor_funkcji.delete(0, 'end')
        self.minx.delete(0, 'end')
        self.maxx.delete(0, 'end')
        self.miny.delete(0, 'end')
        self.maxy.delete(0, 'end')
        self.title.delete(0, 'end')
        self.x.delete(0, 'end')
        self.y.delete(0, 'end')
        self.fig = Figure(figsize=(10, 5.7), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, self.right_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0)
        self.ax.clear()
        self.can.draw()

    def add_x(self):
        """Funkcja dodająca 'x' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), 'x')
        self.graph('x')

    def add_nawias1(self):
        """Funkcja dodająca '(' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), '(')
        self.graph('(')

    def add_nawias2(self):
        """Funkcja dodająca ')' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), ')')
        self.graph(')')

    def add_plus(self):
        """Funkcja dodająca '+' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), '+')
        self.graph('+')

    def add_minus(self):
        """Funkcja dodająca '-' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), '-')
        self.graph('-')

    def add_razy(self):
        """Funkcja dodająca '*' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), '*')
        self.graph('*')

    def add_dzielenie(self):
        """Funkcja dodająca '/' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), '/')
        self.graph('/')

    def add_potega(self):
        """Funkcja dodająca '^' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), '^')
        self.graph('**')

    def add_exp(self):
        """Funkcja dodająca 'exp(' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), 'exp(')
        self.graph('exp(')

    def add_sin(self):
        """Funkcja dodająca 'sin(' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), 'sin(')
        self.graph('sin(')

    def add_cos(self):
        """Funkcja dodająca 'cos(' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), 'cos(')
        self.graph('cos(')

    def add_sqrt(self):
        """Funkcja dodająca 'sqrt(' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), "sqrt(")
        self.graph('sqrt(')

    def add_tg(self):
        """Funkcja dodająca 'tan(' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), 'tan(')
        self.graph('tan(')

    def add_ctg(self):
        """Funkcja dodająca '(1/tan(' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), '(1/tan(')
        self.graph('(1/tan(')

    def add_abs(self):
        """Funkcja dodająca 'abs(' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), 'abs(')
        self.graph('abs(')

    def add_log(self):
        """Funkcja dodająca 'log(' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), 'log(')
        self.graph('log(')

    def add_znak(self):
        """Funkcja dodająca ';' do pola do wpisywania wzoru funkcji."""
        self.wzor_funkcji.insert(len(self.wzor_funkcji.get()), ';')
        self.graph(';')

    def add_backspace(self):
        """Funkcja usuwająca z pola do wpisywania wzoru funkcji całe części funkcji elementarnych."""
        if self.wzor_funkcji.get()[-5:] == 'sqrt(':
            self.wzor_funkcji.delete(len(self.wzor_funkcji.get()) - 5, 'end')
        elif self.wzor_funkcji.get()[-4:] == 'exp(' or self.wzor_funkcji.get()[
                                                       -4:] == 'sin(' or self.wzor_funkcji.get()[
                                                                         -4:] == 'cos(' or self.wzor_funkcji.get()[
                                                                                           -4:] == 'log(' or self.wzor_funkcji.get()[
                                                                                                             -4:] == 'abs(':
            self.wzor_funkcji.delete(len(self.wzor_funkcji.get()) - 4, 'end')
        elif self.wzor_funkcji.get()[-7:] == '(1/tan(':
            self.wzor_funkcji.delete(len(self.wzor_funkcji.get()) - 7, 'end')
        elif self.wzor_funkcji.get()[-4:] == 'tan(':
            self.wzor_funkcji.delete(len(self.wzor_funkcji.get()) - 4, 'end')
        elif self.wzor_funkcji.get()[-2:] == '**':
            self.wzor_funkcji.delete(len(self.wzor_funkcji.get()) - 2, 'end')
        else:
            self.wzor_funkcji.delete(len(self.wzor_funkcji.get()) - 1, 'end')

    def draw_graph(self):
        """Funkcja rysująca wykres."""
        self.functions = self.wzor_funkcji.get()
        if '^' in self.functions:
            self.functions = self.functions.replace('^', '**')
        if ',' in self.functions:
            self.functions = self.functions.replace(',', '.')
        self.fig = Figure(figsize=(10, 5.7), dpi=100)
        self.figure = self.fig.add_subplot()
        try:
            x = linspace(float(self.minx.get()), float(self.maxx.get()),
                         1000 * (math.floor(float(self.maxx.get())) - math.floor(float(self.minx.get()))))
        except:
            if self.minx.get() == '' and self.maxx.get() == '':
                x = linspace(-10, 10, 1000)
            else:
                msb.showerror("Błąd", "W miejscu 'min x' i 'max x' trzeba wpisać liczbę lub zostawić puste pole")
                return
        # self.functions = self.convert(self.functions)
        try:
            self.function = str(self.functions).split(';')
            ##############################################
            for i in self.function:
                if 'x' not in i:
                    i = i + '*(x/x)'
                self.figure.plot(x, eval(i))
            self.figure.grid(True)
            if self.legend_label.get() == "Legenda" or self.legend_label.get() == "Z legendą":
                self.figure.legend(self.function)
            try:
                self.figure.set_ylim([float(self.miny.get()), float(self.maxy.get())])
            except ValueError:
                if self.miny.get() == "" and self.maxy.get() == '':
                    self.figure.set_ylim()
                else:
                    msb.showerror("Błąd", "W miejscu 'min y' i 'max y' trzeba wpisać liczbę lub zostawić puste pole")
                    return
        except:
            self.functions = self.convert(self.functions)
            self.function = str(self.functions).split(';')
            ##############################################
            for i in self.function:
                if 'x' not in i:
                    i = i + '*(x/x)'
                try:
                    self.figure.plot(x, eval(i))
                except:
                    if self.wzor_funkcji.get() == '':
                        msb.showinfo("Info", "Wpisz funkcję")
                    else:
                        if '*(x/x)' in i:
                            i = i.replace('*(x/x)', '')
                        msb.showerror("Błąd", "Niepoprawna funkcja: " + f'{i}')
                    return
            self.figure.grid(True)
            if self.legend_label.get() == "Legenda" or self.legend_label.get() == "Z legendą":
                for i in range(len(self.function)):
                    self.function[i] = self.function[i].replace('**', "^")
                    index = 0
                    while index < len(self.function[i]):
                        if self.function[i][index] == "^":
                            if self.function[i][index + 1] == '{':
                                index+=1
                                continue
                            index += 1
                            if self.function[i][index] == "(":
                                self.function[i] = self.function[i][:index] + "{" + self.function[i][index + 1:]
                                while self.function[i][index] != ")":
                                    index += 1
                                self.function[i] = self.function[i][:index] + "}" + self.function[i][index + 1:]
                                index = 0
                            if self.function[i][index] in self.numbers:
                                self.function[i] = self.function[i][:index] + "{" + self.function[i][index:]
                                index += 1
                                while self.function[i][index] in self.numbers:
                                    if index + 1 == len(self.function[i]):
                                        self.function[i] = self.function[i][:index + 1] + "}"
                                    else:
                                        index += 1
                                self.function[i] = self.function[i][:index] + "}" + self.function[i][index:]
                                index = 0
                        index += 1
                    self.function[i] = '$' + self.function[i].replace('*', "\\cdot ") + '$'
                self.figure.legend(self.function)
            try:
                self.figure.set_ylim([float(self.miny.get()), float(self.maxy.get())])
            except ValueError:
                if self.miny.get() == "" and self.maxy.get() == '':
                    self.figure.set_ylim()
                else:
                    msb.showerror("Błąd", "W miejscu 'min y' i 'max y' trzeba wpisać liczbę lub zostawić puste pole")
                    return
        self.figure.set_xlabel(self.x.get())
        self.figure.set_ylabel(self.y.get())
        self.figure.set_title(self.title.get())
        self.canvas = FigureCanvasTkAgg(self.fig, self.right_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0)

    def keycodess(self, event):
        """Funkcja obsługująca wybrane klawisze z klawiatury."""
        try:
            self.master.bind('<Key>', self.graph)
        except:
            pass

        if event.keysym == 'Return':
            self.draw_graph()
        if event.keysym == 'Escape':
            self.quit()
        if event.keysym == 'F1':
            if self.legend_label.get() == 'Z legendą':
                self.legend_label.set('Bez legendy')
            else:
                self.legend_label.set('Z legendą')
        if event.keysym == "Delete":
            self.add_backspace()
        if event.keysym == "Control_R":
            self.clean_()
        if len(self.wzor_funkcji.get()) == 0:
            self.ax.clear()
            self.can.draw()

    def graph(self, text):
        try:
            self.tmptext = self.wzor_funkcji.get()
            self.tmptext.replace("**", "^")
            index = 0
            while index < len(self.tmptext):
                if self.tmptext[index] == "^":
                    if self.tmptext[index+1] == '{':
                        index+=1
                        continue
                    index += 1
                    if self.tmptext[index] == "(":
                        self.tmptext = self.tmptext[:index] + "{" + self.tmptext[index + 1:]

                        # while open_bracet - close_bracket != 0 and self.tmptext[index] != ")":
                        #     print(open_bracet, close_bracket, "aa")
                        #     if self.tmptext[index] == "(":
                        #         open_bracet+=1
                        #     if self.tmptext[index] == ")":
                        #         open_bracet-=1
                        #     index += 1
                        # while self.tmptext[index] != ")" and open_bracet - close_bracket != 0:
                        #     index += 1
                        while self.tmptext[index] != ")":
                            index += 1
                        self.tmptext = self.tmptext[:index] + "}" + self.tmptext[index + 1:]
                        index = 0
                    if self.tmptext[index] in self.numbers:
                        self.tmptext = self.tmptext[:index] + "{" + self.tmptext[index:]
                        index += 1
                        while self.tmptext[index] in self.numbers:
                            if index+1 == len(self.tmptext):
                                self.tmptext = self.tmptext[:index+1] + "}"
                            else:
                                index += 1
                        self.tmptext = self.tmptext[:index] + "}" + self.tmptext[index:]
                        index = 0
                index += 1
            self.tmptext = self.tmptext.replace('*', '\\cdot')
            print(self.tmptext)
            self.tmptext = "$" + self.tmptext + "$"
            self.ax.clear()
            self.ax.text(0.10, 0.4, self.tmptext, fontsize=10)
            self.can.draw()
        except:
            pass

    def convert(self, function):
        special_letter = "sincoqrtexptanlgb"
        function = function.replace("**", "^")
        special_function = ["sin", "cos", "sqrt", "exp", "tan", "log", "abs"]
        self.operations = ["+", "-", "*", "/", "^", ';']
        index = 0
        while index < len(function):
            if function[index] == 'x' and function[index - 1:index + 2] != 'exp':
                if index - 1 >= 0:
                    if function[index - 1] not in self.operations and function[index - 1] != "(":
                        function = function[:index] + "*" + function[index:]
                elif index + 1 < len(function):
                    if function[index + 1] not in self.operations and function[index + 1] != ")":
                        function = function[:index + 1] + "*" + function[index + 1:]
                index += 1
            else:
                index += 1
        index = 0
        while index < len(function):
            if function[index] in self.numbers:
                if index - 1 >= 0:
                    if function[index - 1] not in self.operations and function[index - 1] != "(" and function[
                        index - 1] not in self.numbers:
                        function = function[:index] + "*" + function[index:]
                index += 1
            else:
                index += 1
        index = 0
        while index < len(function):
            if function[index] in special_letter:
                if function[index:index + 2] in special_function or function[index:index + 3] in special_function:
                    if index - 1 >= 0:
                        if function[index - 1] not in self.operations and function[index - 1] != "(":
                            function = function[:index] + "*" + function[index:]
            index += 1

        function = function.replace("^", "**")
        return function


if __name__ == "__main__":
    root = Tk()
    root.title("Generator wykresów")
    my_window = window(root)
    root.mainloop()
    print(pydoc.doc(my_window))
