import random
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, StringVar, Canvas
from tkinter.ttk import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import sys
import imageio
import os


class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.randint(3, 8)
        self.turn = None

    def move_up(self):
        self.x -= 1

    def move_down(self):
        self.x += 1

    def move_left(self):
        self.y -= 1

    def move_right(self):
        self.y += 1


class Traffic_light2_3:
    def __init__(self, x, y):
        self.x_1 = x
        self.y_1 = y
        self.x_2 = x - 3
        self.y_2 = y
        self.x_3 = x - 3
        self.y_3 = y - 3
        self.x_4 = x
        self.y_4 = y - 3
        self.color_1 = 1
        self.color_2 = 1
        self.color_3 = 1
        self.color_4 = 2
        self.sequence = [self.color_1, self.color_2, self.color_3, self.color_4]

    def stop(self):
        self.color_4 = 1
        self.color_3 = 1
        self.color_2 = 1
        self.color_1 = 1

    def change_color(self):
        self.color_1 = self.sequence[1]
        self.color_2 = self.sequence[2]
        self.color_3 = self.sequence[3]
        self.color_4 = self.sequence[0]
        self.sequence = [self.color_1, self.color_2, self.color_3, self.color_4]


class Traffic_light4:
    def __init__(self, x, y):
        self.x_1 = x
        self.y_1 = y
        self.x_2 = x - 3
        self.y_2 = y
        self.x_3 = x - 3
        self.y_3 = y + 3
        self.color_1 = 1
        self.color_2 = 1
        self.color_3 = 2
        self.sequence = [self.color_1, self.color_2, self.color_3]

    def stop(self):
        self.color_1 = 1
        self.color_2 = 1
        self.color_3 = 1

    def change_color(self):
        self.color_1 = self.sequence[2]
        self.color_2 = self.sequence[0]
        self.color_3 = self.sequence[1]
        self.sequence = [self.color_1, self.color_2, self.color_3]


class Traffic_light1:
    def __init__(self, x, y):
        self.x_1 = x
        self.y_1 = y
        self.x_2 = x - 2
        self.y_2 = y - 3
        self.color_1 = 1
        self.color_2 = 2
        self.sequence = [self.color_1, self.color_2]

    def stop(self):
        self.color_1 = 1
        self.color_2 = 1

    def change_color(self):
        self.color_1 = self.sequence[1]
        self.color_2 = self.sequence[0]
        self.sequence = [self.color_1, self.color_2]


def rang(maximum):
    return np.linspace(0, maximum, 1000 * maximum)


def generating_jump_moments(T, lamb):
    temp_t = rang(T)
    M = max(lamb(temp_t))
    t = 0
    I = 0
    S = []
    while True:
        U_1 = random.random()
        t -= 1 / M * np.log(U_1)
        if t > T:
            return S, [i / len(S) for i in range(1, len(S) + 1)]
        U_2 = random.random()
        if U_2 <= lamb(t):
            I += 1
            S.append(t)


lambda_1 = lambda t: 1/5*(0.8 + 0.8 * np.sin(t / 2))
lambda_2 = lambda t: 1/5*np.exp((2 * np.sin(t / 12 + 3) - 0.9) ** 3)
lambda_3 = lambda t: 1/3*(0.5 * (t + 1) / (t + 1))
lambda_4 = lambda t: 1/2*(0.7 + 0.6 * (np.sin(t / 7 + 2)) ** 2 * np.cos(t / 3 + 1))
lambda_5 = lambda t: 0.2 + 0.2 * np.sign(np.sin(t / 24 + 6))
lambda_6 = lambda t: 0.1 + 0.1 * np.sin(np.sqrt(t))
lambda_7 = lambda t: 0.3 + 0.3 * np.sin(4 * np.sin(t / 2))


class Window():
    def __init__(self, master):
        # Podpis okienka
        self.top_frame = Frame(master)
        self.top_frame.grid(row=0, columnspan=2)
        self.program_name = Label(self.top_frame, text="Symulacja ruchu samochodowego", font=("Times New Roman", 40),
                                  background='yellow')
        self.program_name.pack()

        # parametry
        self.left_frame = Frame(master)
        self.left_frame.grid(row=1, column=0)

        self.green_times_label = Label(self.left_frame,
                                       text="Czasy światła zielonego\ndla poszczególnych sygnalizacji:",
                                       font=("Times New Roman", 13))
        self.green_times_label.grid(row=0, column=0, padx=20)
        self.tau_1_label = Label(self.left_frame, text='t1')
        self.tau_1_label.grid(row=1, column=0)
        self.tau_1 = Entry(self.left_frame, width=5)
        self.tau_1.grid(row=2, column=0)
        self.tau_1.insert(0, '3')

        self.tau_2_label = Label(self.left_frame, text='t2')
        self.tau_2_label.grid(row=3, column=0)
        self.tau_2 = Entry(self.left_frame, width=5)
        self.tau_2.grid(row=4, column=0)
        self.tau_2.insert(0, '10')

        self.tau_3_label = Label(self.left_frame, text='t3')
        self.tau_3_label.grid(row=5, column=0)
        self.tau_3 = Entry(self.left_frame, width=5)
        self.tau_3.grid(row=6, column=0)
        self.tau_3.insert(0, '15')

        self.tau_4_label = Label(self.left_frame, text='t4')
        self.tau_4_label.grid(row=7, column=0)
        self.tau_4 = Entry(self.left_frame, width=5)
        self.tau_4.grid(row=8, column=0)
        self.tau_4.insert(0, '5')

        self.tau_5_label = Label(self.left_frame, text='t5')
        self.tau_5_label.grid(row=9, column=0)
        self.tau_5 = Entry(self.left_frame, width=5)
        self.tau_5.grid(row=10, column=0)
        self.tau_5.insert(0, '7')

        self.tau_6_label = Label(self.left_frame, text='t6')
        self.tau_6_label.grid(row=11, column=0)
        self.tau_6 = Entry(self.left_frame, width=5)
        self.tau_6.grid(row=12, column=0)
        self.tau_6.insert(0, '5')

        self.tau_7_label = Label(self.left_frame, text='t7')
        self.tau_7_label.grid(row=13, column=0)
        self.tau_7 = Entry(self.left_frame, width=5)
        self.tau_7.grid(row=14, column=0)
        self.tau_7.insert(0, '3')

        self.tau_8_label = Label(self.left_frame, text='t8')
        self.tau_8_label.grid(row=15, column=0)
        self.tau_8 = Entry(self.left_frame, width=5)
        self.tau_8.grid(row=16, column=0)
        self.tau_8.insert(0, '15')

        self.tau_9_label = Label(self.left_frame, text='t9')
        self.tau_9_label.grid(row=17, column=0)
        self.tau_9 = Entry(self.left_frame, width=5)
        self.tau_9.grid(row=18, column=0)
        self.tau_9.insert(0, '6')

        self.tau_10_label = Label(self.left_frame, text='t10')
        self.tau_10_label.grid(row=19, column=0)
        self.tau_10 = Entry(self.left_frame, width=5)
        self.tau_10.grid(row=20, column=0)
        self.tau_10.insert(0, '1')

        self.tau_11_label = Label(self.left_frame, text='t11')
        self.tau_11_label.grid(row=21, column=0)
        self.tau_11 = Entry(self.left_frame, width=5)
        self.tau_11.grid(row=22, column=0)
        self.tau_11.insert(0, '5')

        self.tau_12_label = Label(self.left_frame, text='t12')
        self.tau_12_label.grid(row=23, column=0)
        self.tau_12 = Entry(self.left_frame, width=5)
        self.tau_12.grid(row=24, column=0)
        self.tau_12.insert(0, '6')

        self.tau_13_label = Label(self.left_frame, text='t13')
        self.tau_13_label.grid(row=25, column=0)
        self.tau_13 = Entry(self.left_frame, width=5)
        self.tau_13.grid(row=26, column=0)
        self.tau_13.insert(0, '3')

        self.gif_or_not = StringVar()
        self.gif_animation = Checkbutton(self.left_frame, text="Eksport animacji do gif", variable=self.gif_or_not,
                                         offvalue="No", onvalue="Yes")
        self.gif_or_not.set('No')
        self.new_parameters = Button(self.left_frame, text="Zastosuj", command=self.signalization_times)
        self.new_parameters.grid(row=27, column=0, padx=5, pady=10)
        self.launch = Button(self.left_frame, text="Pokaż symulację", command=self.animation)
        self.launch.grid(row=28, column=0, padx=5, pady=10)
        self.gif_animation.grid(row=29, column=0, padx=5, pady=10)
        self.gif_name_label = Label(self.left_frame, text="Nazwa gifa")
        self.gif_name_label.grid(row=30, column=0, pady=5)
        self.gif_name = Entry(self.left_frame, width=40)
        self.gif_name.grid(row=31, column=0, padx=5, pady=10)
        self.stop = Button(self.left_frame, text="Start/stop animacja", command=self.stop)
        self.end_export_to_gif = StringVar()
        self.export = Button(self.left_frame, text="Wyeksportuj do gif", command=self._export)
        self.export.grid(row=33, column=0, padx=5, pady=10)
        self.export_time = Label(self.left_frame, textvariable=self.end_export_to_gif)
        self.export_time.grid(row=32, column=0, padx=5, pady=10)
        self.end_export_to_gif.set(" ")
        self.export_gif_label = Label()
        self.stop.grid(row=34, column=0, padx=5, pady=10)

        self.close_window = Button(self.left_frame, text="Zakończ", command=self.close)
        self.close_window.grid(row=35, column=0, padx=5, pady=10)

        # animancja
        self.right_frame = Frame(master)
        self.right_frame.grid(row=1, column=1)
        self.canv = Canvas(self.right_frame, bg='white', height=350, width=410)
        self.canv.grid()
        self.figure = Figure(figsize=(16, 9))
        self.a = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.canv)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.canv)
        self.toolbar.update()
        self.canvas._tkcanvas.pack()

        self.ani_figure = plt.figure()

        ###

        self.save_animation = []
        self.stop_animation = False
        self.t = 0

    def _export(self):
        if self.gif_or_not.get() == "Yes":
            self.end_export_to_gif.set("Trwa eksportowanie...")
            root.update()
            self.save()
            self.end_export_to_gif.set("Wyeksportowano")
    def stop(self):
        if self.stop_animation:
            self.stop_animation = False
        else:
            self.stop_animation = True
        self.draw_animation()

    def close(self):
        if self.stop_animation:
            self.stop_animation = False
        else:
            self.stop_animation = True
        self.stop_animation = True
        self.draw_animation()
        sys.exit()

    def save(self):
        for i in range(len(self.save_animation)):
            plt.figure(figsize=(16, 9))
            plt.imshow(self.save_animation[i])
            plt.savefig(f'{i}_frame_for_animation_it_will_be_deleted.png')
        filenames = [f'{i}_frame_for_animation_it_will_be_deleted.png' for i in range(len(self.save_animation))]
        with imageio.get_writer(f'{self.gif_name.get()}.gif', mode='I', fps=2) as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)
        for _, __, files in os.walk(os.getcwd()):
            for file in files:
                if file in filenames:
                    os.remove(file)

    def signalization_times(self):
        self.s1 = int(self.tau_1.get()) + self.t
        self.s2 = int(self.tau_2.get()) + self.t
        self.s3 = int(self.tau_3.get()) + self.t
        self.s4 = int(self.tau_4.get()) + self.t
        self.s5 = int(self.tau_5.get()) + self.t
        self.s6 = int(self.tau_6.get()) + self.t
        self.s7 = int(self.tau_7.get()) + self.t
        self.s8 = int(self.tau_8.get()) + self.t
        self.s9 = int(self.tau_9.get()) + self.t
        self.s10 = int(self.tau_10.get()) + self.t
        self.s11 = int(self.tau_11.get()) + self.t
        self.s12 = int(self.tau_12.get()) + self.t
        self.s13 = int(self.tau_13.get()) + self.t

        self._s1 = self.s1 - self.t
        self._s2 = self.s2 - self.t
        self._s3 = self.s3 - self.t
        self._s4 = self.s4 - self.t
        self._s5 = self.s5 - self.t
        self._s6 = self.s6 - self.t
        self._s7 = self.s7 - self.t
        self._s8 = self.s8 - self.t
        self._s9 = self.s9 - self.t
        self._s10 = self.s10 - self.t
        self._s11 = self.s11 - self.t
        self._s12 = self.s12 - self.t
        self._s13 = self.s13 - self.t

    def _board(self):
        self.color_map = {-1: np.array([0, 90, 0]),  # dark green
                          0: np.array([0, 0, 0]),  # black
                          1: np.array([255, 0, 0]),  # red
                          2: np.array([0, 255, 0]),  # green
                          3: np.array([255, 255, 255]),  # white
                          4: np.array([255, 255, 0]),  # yellow
                          5: np.array([204, 0, 204]),  # purple
                          6: np.array([255, 102, 255]),  # pink
                          7: np.array([255, 128, 0]),  # orange
                          8: np.array([153, 255, 255])}  # blue
        self.board = np.zeros((29, 42))
        self.board[:10, :11] = -1
        self.board[12:23, :11] = -1
        self.board[24:, :11] = -1
        self.board[:10, 13:27] = -1
        self.board[12:, 13:27] = -1
        self.board[:10, 29:36] = -1
        self.board[:10, 38:] = -1
        self.board[12:, 29:] = -1

        self.S1 = Traffic_light1(24, 13)
        self.board[self.S1.x_1, self.S1.y_1] = self.S1.color_1
        self.board[self.S1.x_2, self.S1.y_2] = self.S1.color_2

        self.S2 = Traffic_light2_3(12, 13)
        self.board[self.S2.x_1, self.S2.y_1] = self.S2.color_1
        self.board[self.S2.x_2, self.S2.y_2] = self.S2.color_2
        self.board[self.S2.x_3, self.S2.y_3] = self.S2.color_3
        self.board[self.S2.x_4, self.S2.y_4] = self.S2.color_4

        self.S3 = Traffic_light2_3(12, 29)
        self.board[self.S3.x_1, self.S3.y_1] = self.S3.color_1
        self.board[self.S3.x_2, self.S3.y_2] = self.S3.color_2
        self.board[self.S3.x_3, self.S3.y_3] = self.S3.color_3
        self.board[self.S3.x_4, self.S3.y_4] = self.S3.color_4

        self.S4 = Traffic_light4(12, 35)
        self.board[self.S4.x_1, self.S4.y_1] = self.S4.color_1
        self.board[self.S4.x_2, self.S4.y_2] = self.S4.color_2
        self.board[self.S4.x_3, self.S4.y_3] = self.S4.color_3

        self.time_1 = generating_jump_moments(1000, lambda_1)[0]
        self.time_1 = [np.ceil(i) for i in self.time_1]
        self.time_2 = generating_jump_moments(1000, lambda_2)[0]
        self.time_2 = [np.ceil(i) for i in self.time_2]
        self.time_3 = generating_jump_moments(1000, lambda_3)[0]
        self.time_3 = [np.ceil(i) for i in self.time_3]
        self.time_4 = generating_jump_moments(1000, lambda_4)[0]
        self.time_4 = [np.ceil(i) for i in self.time_4]
        self.time_5 = generating_jump_moments(1000, lambda_5)[0]
        self.time_5 = [np.ceil(i) for i in self.time_5]
        self.time_6 = generating_jump_moments(1000, lambda_6)[0]
        self.time_6 = [np.ceil(i) for i in self.time_6]
        self.time_7 = generating_jump_moments(1000, lambda_7)[0]
        self.time_7 = [np.ceil(i) for i in self.time_7]
        self.t = 0
        self.remaining_1 = []
        self.remaining_2 = []
        self.remaining_3 = []
        self.remaining_4 = []
        self.remaining_5 = []
        self.remaining_6 = []
        self.remaining_7 = []
        self.cars = []
        self.time_for_change_signal = [random.randint(2, 4) for i in range(5)]
        self.stop_1 = 0
        self.stop_2 = 0
        self.stop_3 = 0
        self.stop_4 = 0

    def animation(self):
        self.stop_animation = False
        self._board()
        try:
            self.draw_animation()
        except:
            self.signalization_times()
            self.draw_animation()

    def draw_animation(self):
        while not self.stop_animation:
            root.update()
            for i in self.cars:
                if i.x != self.board.shape[0] - 1 and i.x != 0 and i.y != self.board.shape[1] - 1 and i.y != 0:  # todo
                    if self.board[i.x, i.y - 1] == -1 and self.board[i.x, i.y + 1] == -1:
                        i.move_left()
                    elif self.board[i.x - 1, i.y] == -1 and i.turn == None:
                        if self.board[i.x, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                    elif self.board[i.x, i.y + 1] == -1 and i.turn == None:
                        if self.board[i.x - 1, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                    elif self.board[i.x + 1, i.y] == -1 and i.turn == None:
                        if self.board[i.x, i.y + 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                    elif self.board[i.x, i.y - 1] == -1 and i.turn == None:
                        if self.board[i.x + 1, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()


                    elif self.board[i.x, i.y + 1] == 2 and i.x == 24 and i.y == 12:  # najmniejsze skrzyżowanie
                        if i.turn == None:
                            turn = random.randint(1, 3)
                            if turn == 1:
                                i.turn = "up"
                            elif turn == 2:
                                i.turn = "left"
                            else:
                                i.turn = "down"
                        if i.turn == "up" and self.board[i.x - 2, i.y] == 0 and self.board[i.x - 1, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                            i.turn = None
                            self.board[i.x, i.y] = i.color
                        elif i.turn == "left" and self.board[i.x - 1, i.y] == 0 and self.board[i.x - 1, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == 'down' and self.board[i.x - 1, i.y] == 0 and self.board[
                            i.x - 1, i.y - 1] == 0 and self.board[
                            i.x - 1, i.y - 2] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 23 and i.y == 12 and (i.turn == "left" or i.turn == 'down'):
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 23 and i.y == 11 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 23 and i.y == 10 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        i.turn = None
                        self.board[i.x, i.y] = i.color
                    elif i.x == 23 and i.y == 11 and i.turn == 'down':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        i.turn = None
                        self.board[i.x, i.y] = i.color
                    elif self.board[i.x, i.y - 1] == 2 and i.x == 22 and i.y == 11:  # druga strona
                        if i.turn == None:
                            turn = random.randint(1, 3)
                            if turn == 1:
                                i.turn = "_up"
                            elif turn == 2:
                                i.turn = "_right"
                            else:
                                i.turn = "_down"
                        if i.turn == "_up" and self.board[i.x + 1, i.y] == 0 and self.board[i.x + 2, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == "_right" and self.board[i.x + 1, i.y] == 0 and self.board[i.x + 1, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == "_down" and self.board[i.x + 1, i.y] == 0 and self.board[
                            i.x + 1, i.y + 1] == 0 and self.board[
                            i.x, i.y + 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 23 and i.y == 11 and i.turn == "_up":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        i.turn = None
                        self.board[i.x, i.y] = i.color
                    elif i.x == 23 and i.y == 11 and i.turn == "_right":
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 23 and i.y == 10 and i.turn == "_right":
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 23 and i.y == 11 and i.turn == '_down':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif self.board[i.x, i.y + 1] == 2 and i.x == 12 and i.y == 12:  # skrzyżowanie pierwsze od gory
                        if i.turn == None:
                            turn = random.randint(1, 4)
                            if turn == 1:
                                i.turn = 'right'
                            elif turn == 2:
                                i.turn = 'up'
                            elif turn == 3:
                                i.turn = "left"
                            else:
                                i.turn = 'down'
                        if i.turn == 'right' and self.board[i.x - 1, i.y] == 0 and self.board[i.x - 1, i.y + 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == 'up' and self.board[i.x - 1, i.y] == 0 and self.board[i.x - 2, i.y] == 0 and \
                                self.board[
                                    i.x - 3, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == "left" and self.board[i.x - 1, i.y] == 0 and self.board[i.x - 2, i.y] == 0 and \
                                self.board[
                                    i.x - 2, i.y - 1] == 0 and self.board[i.x - 2, i.y - 2] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == 'down' and self.board[i.x - 1, i.y] == 0 and self.board[
                            i.x - 1, i.y - 1] == 0 and self.board[
                            i.x, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 12 and i.turn == 'right':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 13 and i.turn == 'right':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 12 and i.turn == 'up':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 12 and i.turn == 'up':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 9 and i.y == 12 and i.turn == 'up':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 12 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 12 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 11 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 10 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 12 and i.turn == 'down':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 11 and i.turn == 'down':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 12 and i.y == 11 and i.turn == 'down':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif self.board[i.x - 1, i.y] == 2 and i.x == 10 and i.y == 13:  # prawa strona tego skrzyzowania
                        if i.turn == None:
                            turn = random.randint(1, 4)
                            if turn == 1:
                                i.turn = '_right'
                            elif turn == 2:
                                i.turn = '_up'
                            elif turn == 3:
                                i.turn = "_left"
                            else:
                                i.turn = '_down'
                        if i.turn == '_right' and self.board[i.x, i.y - 1] == 0 and self.board[i.x - 1, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == "_up" and self.board[i.x, i.y - 1] == 0 and self.board[i.x, i.y - 2] == 0 and \
                                self.board[
                                    i.x, i.y - 3] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '_left' and self.board[i.x, i.y - 1] == 0 and self.board[i.x, i.y - 2] == 0 and \
                                self.board[
                                    i.x + 1, i.y - 2] == 0 and self.board[i.x + 2, i.y - 2] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '_down' and self.board[i.x, i.y - 1] == 0 and self.board[
                            i.x + 1, i.y - 1] == 0 and self.board[
                            i.x + 1, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 12 and i.turn == '_right':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 9 and i.y == 12 and i.turn == '_right':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 12 and i.turn == '_up':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 11 and i.turn == '_up':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 10 and i.turn == '_up':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 12 and i.turn == '_left':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 11 and i.turn == '_left':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 11 and i.turn == '_left':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 12 and i.y == 11 and i.turn == '_left':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 12 and i.turn == '_down':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 12 and i.turn == "_down":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 13 and i.turn == "_down":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif self.board[i.x, i.y - 1] == 2 and i.x == 9 and i.y == 11:  # górna strona tego skrzyżowania
                        if i.turn == None:
                            turn = random.randint(1, 4)
                            if turn == 1:
                                i.turn = '__right'
                            elif turn == 2:
                                i.turn = '__up'
                            elif turn == 3:
                                i.turn = "__left"
                            else:
                                i.turn = '__down'
                        if i.turn == '__right' and self.board[i.x + 1, i.y] == 0 and self.board[i.x + 1, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '__up' and self.board[i.x + 1, i.y] == 0 and self.board[i.x + 2, i.y] == 0 and \
                                self.board[
                                    i.x + 3, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '__left' and self.board[i.x + 1, i.y] == 0 and self.board[i.x + 2, i.y] == 0 and \
                                self.board[
                                    i.x + 2, i.y + 1] == 0 and self.board[i.x + 2, i.y + 2] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '__down' and self.board[i.x + 1, i.y] == 0 and self.board[
                            i.x + 1, i.y + 1] == 0 and self.board[
                            i.x, i.y + 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 11 and i.turn == "__right":
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 10 and i.turn == "__right":
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 11 and i.turn == "__up":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 11 and i.turn == "__up":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 12 and i.y == 11 and i.turn == "__up":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 11 and i.turn == '__left':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 11 and i.turn == "__left":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 12 and i.turn == "__left":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 13 and i.turn == "__left":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 11 and i.turn == '__down':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 12 and i.turn == "__down":
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 9 and i.y == 12 and i.turn == "__down":
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif self.board[i.x + 1, i.y] == 2 and i.x == 11 and i.y == 10:  # lewa strona tego skrzyżowania
                        if i.turn == None:
                            turn = random.randint(1, 4)
                            if turn == 1:
                                i.turn = '___right'
                            elif turn == 2:
                                i.turn = '___up'
                            elif turn == 3:
                                i.turn = "___left"
                            else:
                                i.turn = '___down'
                        if i.turn == '___right' and self.board[i.x, i.y + 1] == 0 and self.board[i.x + 1, i.y + 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '___up' and self.board[i.x, i.y + 1] == 0 and self.board[i.x, i.y + 2] == 0 and \
                                self.board[
                                    i.x, i.y + 3] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '___left' and self.board[i.x, i.y + 1] == 0 and self.board[i.x, i.y + 2] == 0 and \
                                self.board[
                                    i.x - 1, i.y + 2] == 0 and self.board[i.x - 2, i.y + 2] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '___down' and self.board[i.x, i.y + 1] == 0 and self.board[
                            i.x - 1, i.y + 1] == 0 and \
                                self.board[i.x - 1, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 11 and i.turn == "___right":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 12 and i.y == 11 and i.turn == "___right":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 11 and i.turn == "___up":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 12 and i.turn == "___up":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 13 and i.turn == "___up":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 11 and i.turn == "___left":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 12 and i.turn == '___left':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 12 and i.turn == '___left':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 9 and i.y == 12 and i.turn == '___left':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 11 and i.turn == "___down":
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 11 and i.turn == "___down":
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 10 and i.turn == "___down":
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None




                    ##############################

                    elif self.board[i.x, i.y + 1] == 2 and i.x == 12 and i.y == 28:  # skrzyżowanie drugie od gory
                        if i.turn == None:
                            turn = random.randint(1, 4)
                            if turn == 1:
                                i.turn = 'right'
                            elif turn == 2:
                                i.turn = 'up'
                            elif turn == 3:
                                i.turn = "left"
                            else:
                                i.turn = 'down'
                        if i.turn == 'right' and self.board[i.x - 1, i.y] == 0 and self.board[i.x - 1, i.y + 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == 'up' and self.board[i.x - 1, i.y] == 0 and self.board[i.x - 2, i.y] == 0 and \
                                self.board[
                                    i.x - 3, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == "left" and self.board[i.x - 1, i.y] == 0 and self.board[i.x - 2, i.y] == 0 and \
                                self.board[
                                    i.x - 2, i.y - 1] == 0 and self.board[i.x - 2, i.y - 2] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == 'down' and self.board[i.x - 1, i.y] == 0 and self.board[
                            i.x - 1, i.y - 1] == 0 and self.board[
                            i.x, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 28 and i.turn == 'right':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 29 and i.turn == 'right':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 28 and i.turn == 'up':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 28 and i.turn == 'up':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 9 and i.y == 28 and i.turn == 'up':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 28 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 28 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 27 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 26 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 28 and i.turn == 'down':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 27 and i.turn == 'down':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 12 and i.y == 27 and i.turn == 'down':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif self.board[i.x - 1, i.y] == 2 and i.x == 10 and i.y == 29:  # prawa strona tego skrzyzowania
                        if i.turn == None:
                            turn = random.randint(1, 4)
                            if turn == 1:
                                i.turn = '_right'
                            elif turn == 2:
                                i.turn = '_up'
                            elif turn == 3:
                                i.turn = "_left"
                            else:
                                i.turn = '_down'
                        if i.turn == '_right' and self.board[i.x, i.y - 1] == 0 and self.board[i.x - 1, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == "_up" and self.board[i.x, i.y - 1] == 0 and self.board[i.x, i.y - 2] == 0 and \
                                self.board[
                                    i.x, i.y - 3] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '_left' and self.board[i.x, i.y - 1] == 0 and self.board[i.x, i.y - 2] == 0 and \
                                self.board[
                                    i.x + 1, i.y - 2] == 0 and self.board[i.x + 2, i.y - 2] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '_down' and self.board[i.x, i.y - 1] == 0 and self.board[
                            i.x + 1, i.y - 1] == 0 and self.board[
                            i.x + 1, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 28 and i.turn == '_right':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 9 and i.y == 28 and i.turn == '_right':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 28 and i.turn == '_up':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 27 and i.turn == '_up':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 26 and i.turn == '_up':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 28 and i.turn == '_left':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 27 and i.turn == '_left':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 27 and i.turn == '_left':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 12 and i.y == 27 and i.turn == '_left':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 28 and i.turn == '_down':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 28 and i.turn == "_down":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 29 and i.turn == "_down":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif self.board[i.x, i.y - 1] == 2 and i.x == 9 and i.y == 27:  # górna strona tego skrzyżowania
                        if i.turn == None:
                            turn = random.randint(1, 4)
                            if turn == 1:
                                i.turn = '__right'
                            elif turn == 2:
                                i.turn = '__up'
                            elif turn == 3:
                                i.turn = "__left"
                            else:
                                i.turn = '__down'
                        if i.turn == '__right' and self.board[i.x + 1, i.y] == 0 and self.board[i.x + 1, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '__up' and self.board[i.x + 1, i.y] == 0 and self.board[i.x + 2, i.y] == 0 and \
                                self.board[
                                    i.x + 3, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '__left' and self.board[i.x + 1, i.y] == 0 and self.board[i.x + 2, i.y] == 0 and \
                                self.board[
                                    i.x + 2, i.y + 1] == 0 and self.board[i.x + 2, i.y + 2] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '__down' and self.board[i.x + 1, i.y] == 0 and self.board[
                            i.x + 1, i.y + 1] == 0 and self.board[
                            i.x, i.y + 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 27 and i.turn == "__right":
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 26 and i.turn == "__right":
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 27 and i.turn == "__up":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 27 and i.turn == "__up":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 12 and i.y == 27 and i.turn == "__up":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 27 and i.turn == '__left':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 27 and i.turn == "__left":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 28 and i.turn == "__left":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 29 and i.turn == "__left":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 27 and i.turn == '__down':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 28 and i.turn == "__down":
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 9 and i.y == 28 and i.turn == "__down":
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif self.board[i.x + 1, i.y] == 2 and i.x == 11 and i.y == 26:  # lewa strona tego skrzyżowania
                        if i.turn == None:
                            turn = random.randint(1, 4)
                            if turn == 1:
                                i.turn = '___right'
                            elif turn == 2:
                                i.turn = '___up'
                            elif turn == 3:
                                i.turn = "___left"
                            else:
                                i.turn = '___down'
                        if i.turn == '___right' and self.board[i.x, i.y + 1] == 0 and self.board[i.x + 1, i.y + 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '___up' and self.board[i.x, i.y + 1] == 0 and self.board[i.x, i.y + 2] == 0 and \
                                self.board[
                                    i.x, i.y + 3] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '___left' and self.board[i.x, i.y + 1] == 0 and self.board[i.x, i.y + 2] == 0 and \
                                self.board[
                                    i.x - 1, i.y + 2] == 0 and self.board[i.x - 2, i.y + 2] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '___down' and self.board[i.x, i.y + 1] == 0 and self.board[
                            i.x - 1, i.y + 1] == 0 and \
                                self.board[i.x - 1, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 27 and i.turn == "___right":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 12 and i.y == 27 and i.turn == "___right":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 27 and i.turn == "___up":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 28 and i.turn == "___up":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 29 and i.turn == "___up":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 27 and i.turn == "___left":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 28 and i.turn == '___left':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 28 and i.turn == '___left':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 9 and i.y == 28 and i.turn == '___left':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 27 and i.turn == "___down":
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 27 and i.turn == "___down":
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 26 and i.turn == "___down":
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    ###############################
                    elif self.board[i.x + 1, i.y] == 2 and i.x == 11 and i.y == 35:
                        if i.turn == None:
                            turn = random.randint(1, 3)
                            if turn == 1:
                                i.turn = 'up'
                            elif turn == 2:
                                i.turn = 'left'
                            else:
                                i.turn = "down"
                        if i.turn == 'up' and self.board[i.x, i.y + 1] == 0 and self.board[i.x, i.y + 2] == 0 and \
                                self.board[
                                    i.x, i.y + 3] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == 'left' and self.board[i.x, i.y + 1] == 0 and self.board[i.x, i.y + 2] == 0 and \
                                self.board[
                                    i.x - 1, i.y + 2] == 0 and self.board[i.x - 2, i.y + 2] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == 'down' and self.board[i.x, i.y + 1] == 0 and self.board[
                            i.x - 1, i.y + 1] == 0 and self.board[
                            i.x - 1, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 36 and i.turn == 'up':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 37 and i.turn == 'up':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 38 and i.turn == 'up':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 36 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 37 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 37 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 9 and i.y == 37 and i.turn == 'left':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 11 and i.y == 36 and i.turn == 'down':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 36 and i.turn == 'down':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 35 and i.turn == 'down':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None

                    elif self.board[i.x - 1, i.y] == 2 and i.x == 10 and i.y == 38:  # prawa strona tego skrzyżowania
                        if i.turn == None:
                            turn = random.randint(1, 3)
                            if turn == 1:
                                i.turn = '_up'
                            elif turn == 2:
                                i.turn = '_right'
                            else:
                                i.turn = "_down"
                        if i.turn == '_up' and self.board[i.x, i.y - 1] == 0 and self.board[i.x, i.y - 2] == 0 and \
                                self.board[
                                    i.x, i.y - 3] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '_right' and self.board[i.x, i.y - 1] == 0 and self.board[i.x - 1, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '_down' and self.board[i.x, i.y - 1] == 0 and self.board[
                            i.x + 1, i.y + 1] == 0 and self.board[
                            i.x + 1, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 37 and i.turn == '_up':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 36 and i.turn == '_up':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 35 and i.turn == '_up':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 37 and i.turn == '_right':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 9 and i.y == 37 and i.turn == '_right':
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 37 and i.turn == '_down':
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 37 and i.turn == '_down':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 11 and i.y == 38 and i.turn == '_down':
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif self.board[i.x, i.y - 1] == 2 and i.x == 9 and i.y == 36:  # górna strona tego skrzyżowania
                        if i.turn == None:
                            turn = random.randint(1, 3)
                            if turn == 1:
                                i.turn = '__right'
                            elif turn == 2:
                                i.turn = '__left'
                            else:
                                i.turn = "__down"
                        if i.turn == "__right" and self.board[i.x + 1, i.y] == 0 and self.board[i.x + 1, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == "__left" and self.board[i.x + 1, i.y] == 0 and self.board[i.x + 2, i.y] == 0 and \
                                self.board[
                                    i.x + 2, i.y + 1] == 0 and self.board[i.x + 2, i.y + 2] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                        elif i.turn == '__down' and self.board[i.x + 1, i.y] == 0 and self.board[
                            i.x + 1, i.y + 1] == 0 and self.board[
                            i.x, i.y + 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                            self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 36 and i.turn == '__right':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 35 and i.turn == '__right':
                        self.board[i.x, i.y] = 0
                        i.move_left()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    elif i.x == 10 and i.y == 36 and i.turn == "__left":
                        self.board[i.x, i.y] = 0
                        i.move_down()
                        self.board[i.x, i.y] = i.color
                        i.turn = None
                    ## możliwe, że tu trzeba będzie poprawić - zakręt z górnego skrzyżowania w lewo

                    elif i.x == 10 and i.y == 36 and i.turn == "__down":
                        self.board[i.x, i.y] = 0
                        i.move_right()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 10 and i.y == 37 and i.turn == "__down":
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                    elif i.x == 9 and i.y == 37 and i.turn == "__down":
                        self.board[i.x, i.y] = 0
                        i.move_up()
                        self.board[i.x, i.y] = i.color
                        i.turn = None









                ##############################

                elif (i.x == 23 and i.y == 0) or (i.x == 28 and i.y == 11) or (i.x == 28 and i.y == 27) or (
                        i.x == 11 and i.y == 41) or (i.x == 0 and i.y == 37) \
                        or (i.x == 0 and i.y == 28) or (i.x == 10 and i.y == 0) or (i.x == 0 and i.y == 12):
                    self.board[i.x, i.y] = 0
                    self.cars.remove(i)
                    del i

                elif i.x == self.board.shape[0] - 1:
                    if self.board[i.x, i.y + 1] == -1:
                        if self.board[i.x - 1, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_up()
                    else:
                        del i
                elif i.x == 0:
                    if self.board[i.x, i.y - 1] == -1:
                        if self.board[i.x + 1, i.y] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_down()
                    else:
                        self.cars.remove(i)
                        del i
                elif i.y == self.board.shape[1] - 1:
                    if self.board[i.x - 1, i.y] == -1:
                        if self.board[i.x, i.y - 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_left()
                    else:
                        del i
                elif i.y == 0:
                    if self.board[i.x + 1, i.y] == -1:
                        if self.board[i.x, i.y + 1] == 0:
                            self.board[i.x, i.y] = 0
                            i.move_right()
                    else:
                        del i
            while True:
                if self.time_1[0] == self.t:
                    if len(self.time_1) == 1:
                        temp = self.time_1.pop(0)
                        self.time_1 = generating_jump_moments(1000, lambda_1)[0]
                        self.time_1 = [np.ceil(i) + temp for i in self.time_1]
                    car = Car(28, 12)
                    self.time_1.pop(0)
                    if self.board[car.x, car.y] == 0:
                        self.board[car.x, car.y] = car.color
                        self.cars.append(car)
                    else:
                        self.remaining_1.append(car)
                else:
                    break
            while True:
                if self.time_2[0] == self.t:
                    if len(self.time_2) == 1:
                        temp = self.time_2.pop(0)
                        self.time_2 = generating_jump_moments(1000, lambda_2)[0]
                        self.time_2 = [np.ceil(i) + temp for i in self.time_2]
                    car = Car(28, 28)
                    self.time_2.pop(0)
                    if self.board[car.x, car.y] == 0:
                        self.board[car.x, car.y] = car.color
                        self.cars.append(car)
                    else:
                        self.remaining_2.append(car)
                else:
                    break
            while True:
                if self.time_3[0] == self.t:
                    if len(self.time_3) == 1:
                        temp = self.time_3.pop(0)
                        self.time_3 = generating_jump_moments(1000, lambda_3)[0]
                        self.time_3 = [np.ceil(i) + temp for i in self.time_3]
                    car = Car(10, 41)
                    self.time_3.pop(0)
                    if self.board[car.x, car.y] == 0:
                        self.board[car.x, car.y] = car.color
                        self.cars.append(car)
                    else:
                        self.remaining_3.append(car)
                else:
                    break
            while True:
                if self.time_4[0] == self.t:
                    if len(self.time_4) == 1:
                        temp = self.time_4.pop(0)
                        self.time_4 = generating_jump_moments(1000, lambda_4)[0]
                        self.time_4 = [np.ceil(i) + temp for i in self.time_4]
                    car = Car(11, 0)
                    self.time_4.pop(0)
                    if self.board[car.x, car.y] == 0:
                        self.board[car.x, car.y] = car.color
                        self.cars.append(car)
                    else:
                        self.remaining_4.append(car)
                else:
                    break
            while True:
                if self.time_5[0] == self.t:
                    if len(self.time_5) == 1:
                        temp = self.time_5.pop(0)
                        self.time_5 = generating_jump_moments(1000, lambda_5)[0]
                        self.time_5 = [np.ceil(i) + temp for i in self.time_5]
                    car = Car(0, 11)
                    self.time_5.pop(0)
                    if self.board[car.x, car.y] == 0:
                        self.board[car.x, car.y] = car.color
                        self.cars.append(car)
                    else:
                        self.remaining_5.append(car)
                else:
                    break
            while True:
                if self.time_6[0] == self.t:
                    if len(self.time_6) == 1:
                        temp = self.time_6.pop(0)
                        self.time_6 = generating_jump_moments(1000, lambda_6)[0]
                        self.time_6 = [np.ceil(i) + temp for i in self.time_6]
                    car = Car(0, 27)
                    self.time_6.pop(0)
                    if self.board[car.x, car.y] == 0:
                        self.board[car.x, car.y] = car.color
                        self.cars.append(car)
                    else:
                        self.remaining_6.append(car)
                else:
                    break
            while True:
                if self.time_7[0] == self.t:
                    if len(self.time_7) == 1:
                        temp = self.time_7.pop(0)
                        self.time_7 = generating_jump_moments(1000, lambda_7)[0]
                        self.time_7 = [np.ceil(i) + temp for i in self.time_7]
                    car = Car(0, 36)
                    self.time_7.pop(0)
                    if self.board[car.x, car.y] == 0:
                        self.board[car.x, car.y] = car.color
                        self.cars.append(car)
                    else:
                        self.remaining_7.append(car)
                else:
                    break
            if self.s1 == self.t and self.S1.color_1 == 2:
                self.S1.stop()
                self.board[self.S1.x_1, self.S1.y_1] = self.S1.color_1
                self.board[self.S1.x_2, self.S1.y_2] = self.S1.color_2
                if self.board[24, 12] != 0:
                    for i in self.cars:
                        if i.x == 24 and i.y == 12:
                            if i.turn == "up":
                                self.stop_1 = self.s1 + 2
                            else:
                                self.stop_1 = self.s1 + 3
                            break
                elif self.board[23, 12] != 0:
                    for i in self.cars:
                        if i.x == 23 and i.y == 12:
                            if i.turn == "up":
                                self.stop_1 = self.s1 + 1
                            else:
                                self.stop_1 = self.s1 + 2
                            break
                elif self.board[23, 11] != 0:
                    for i in self.cars:
                        if i.x == 23 and i.y == 11:
                            self.stop_1 = self.s1 + 1
                            break
                else:
                    self.stop_1 = self.s1
            elif self.s2 == self.t and self.S1.color_2 == 2:
                self.S1.stop()
                self.board[self.S1.x_1, self.S1.y_1] = self.S1.color_1
                self.board[self.S1.x_2, self.S1.y_2] = self.S1.color_2
                if self.board[22, 11] != 0:
                    for i in self.cars:
                        if i.x == 22 and i.y == 11:
                            if i.turn == "_up":
                                self.stop_1 = self.s2 + 2
                            else:
                                self.stop_1 = self.s2 + 3
                            break
                elif self.board[23, 11] != 0:
                    for i in self.cars:
                        if i.x == 23 and i.y == 11:
                            if i.turn == "_right" or i.turn == '_up':
                                self.stop_1 = self.s2 + 1
                            else:
                                self.stop_1 = self.s2 + 2
                            break
                elif self.board[23, 12] != 0:
                    for i in self.cars:
                        if i.x == 23 and i.y == 12:
                            self.stop_1 = self.s2 + 1
                            break
                else:
                    self.stop_1 = self.s2

            if self.s3 == self.t and self.S2.color_1 == 2:
                self.S2.stop()
                self.board[self.S2.x_1, self.S2.y_1] = self.S2.color_1
                self.board[self.S2.x_2, self.S2.y_2] = self.S2.color_2
                self.board[self.S2.x_3, self.S2.y_3] = self.S2.color_3
                self.board[self.S2.x_4, self.S2.y_4] = self.S2.color_4
                if self.board[12, 12] != 0:
                    for i in self.cars:
                        if i.x == 12 and i.y == 12:
                            if i.turn == "right":
                                self.stop_2 = self.s3 + 2
                            elif i.turn == "up" or i.turn == "down":
                                self.stop_2 = self.s3 + 3
                            else:
                                self.stop_2 = self.s3 + 4
                            break
                elif self.board[11, 12] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 12:
                            if i.turn == "right":
                                self.stop_2 = self.s3 + 1
                            elif i.turn == "up" or i.turn == "down":
                                self.stop_2 = self.s3 + 2
                            else:
                                self.stop_2 = self.s3 + 3
                            break
                elif self.board[10, 12] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 12:
                            if i.turn == "up":
                                self.stop_2 = self.s3 + 1
                            else:
                                self.stop_2 = self.s3 + 2
                            break
                elif self.board[11, 11] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 11:
                            self.stop_2 = self.s3 + 1
                            break
                elif self.board[10, 11] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 11:
                            self.stop_2 = self.s3 + 1
                            break
                else:
                    self.stop_2 = self.s3
            elif self.s4 == self.t and self.S2.color_2 == 2:
                self.S2.stop()
                self.board[self.S2.x_1, self.S2.y_1] = self.S2.color_1
                self.board[self.S2.x_2, self.S2.y_2] = self.S2.color_2
                self.board[self.S2.x_3, self.S2.y_3] = self.S2.color_3
                self.board[self.S2.x_4, self.S2.y_4] = self.S2.color_4
                if self.board[10, 13] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 13:
                            if i.turn == "_right":
                                self.stop_2 = self.s4 + 2
                            elif i.turn == "_up" or i.turn == "_down":
                                self.stop_2 = self.s4 + 3
                            else:
                                self.stop_2 = self.s4 + 4
                            break
                elif self.board[10, 12] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 12:
                            if i.turn == "_right":
                                self.stop_2 = self.s4 + 1
                            elif i.turn == "_up" or i.turn == "_down":
                                self.stop_2 = self.s4 + 2
                            else:
                                self.stop_2 = self.s4 + 3
                            break
                elif self.board[10, 11] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 11:
                            if i.turn == "_up":
                                self.stop_2 = self.s4 + 1
                            elif i.turn == "_left":
                                self.stop_2 = self.s4 + 2
                            break
                elif self.board[11, 12] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 12:
                            self.stop_2 = self.s4 + 1
                            break
                elif self.board[11, 11] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 11:
                            self.stop_2 = self.s4 + 1
                            break
                else:
                    self.stop_2 = self.s4
            elif self.s5 == self.t and self.S2.color_3 == 2:
                self.S2.stop()
                self.board[self.S2.x_1, self.S2.y_1] = self.S2.color_1
                self.board[self.S2.x_2, self.S2.y_2] = self.S2.color_2
                self.board[self.S2.x_3, self.S2.y_3] = self.S2.color_3
                self.board[self.S2.x_4, self.S2.y_4] = self.S2.color_4
                if self.board[9, 11] != 0:
                    for i in self.cars:
                        if i.x == 9 and i.y == 11:
                            if i.turn == "__right":
                                self.stop_2 = self.s5 + 2
                            elif i.turn == "__up" or i.turn == "__down":
                                self.stop_2 = self.s5 + 3
                            else:
                                self.stop_2 = self.s5 + 4
                            break
                elif self.board[10, 11] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 11:
                            if i.turn == "__right":
                                self.stop_2 = self.s5 + 1
                            elif i.turn == "__up" or i.turn == "__down":
                                self.stop_2 = self.s5 + 2
                            else:
                                self.stop_2 = self.s5 + 3
                            break
                elif self.board[11, 11] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 11:
                            if i.turn == "__up":
                                self.stop_2 = self.s5 + 1
                            elif i.turn == "__left":
                                self.stop_2 = self.s5 + 2
                            break
                elif self.board[10, 12] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 12:
                            self.stop_2 = self.s5 + 1
                            break
                elif self.board[11, 12] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 12:
                            self.stop_2 = self.s5 + 1
                            break
                else:
                    self.stop_2 = self.s5
            elif self.s6 == self.t and self.S2.color_4 == 2:
                self.S2.stop()
                self.board[self.S2.x_1, self.S2.y_1] = self.S2.color_1
                self.board[self.S2.x_2, self.S2.y_2] = self.S2.color_2
                self.board[self.S2.x_3, self.S2.y_3] = self.S2.color_3
                self.board[self.S2.x_4, self.S2.y_4] = self.S2.color_4
                if self.board[11, 10] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 10:
                            if i.turn == "___right":
                                self.stop_2 = self.s6 + 2
                            elif i.turn == "___up" or i.turn == "___down":
                                self.stop_2 = self.s6 + 3
                            else:
                                self.stop_2 = self.s6 + 4
                            break
                elif self.board[11, 11] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 11:
                            if i.turn == "___right":
                                self.stop_2 = self.s6 + 1
                            elif i.turn == "___up" or i.turn == "___down":
                                self.stop_2 = self.s6 + 2
                            else:
                                self.stop_2 = self.s6 + 3
                            break
                elif self.board[11, 12] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 12:
                            if i.turn == "___up":
                                self.stop_2 = self.s6 + 1
                            elif i.turn == "___left":
                                self.stop_2 = self.s6 + 2
                            break
                elif self.board[10, 11] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 11:
                            self.stop_2 = self.s6 + 1
                            break
                elif self.board[10, 12] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 12:
                            self.stop_2 = self.s6 + 1
                            break
                else:
                    self.stop_2 = self.s6

            if self.s7 == self.t and self.S3.color_1 == 2:
                self.S3.stop()
                self.board[self.S3.x_1, self.S3.y_1] = self.S3.color_1
                self.board[self.S3.x_2, self.S3.y_2] = self.S3.color_2
                self.board[self.S3.x_3, self.S3.y_3] = self.S3.color_3
                self.board[self.S3.x_4, self.S3.y_4] = self.S3.color_4
                if self.board[12, 28] != 0:
                    for i in self.cars:
                        if i.x == 12 and i.y == 28:
                            if i.turn == "right":
                                self.stop_3 = self.s7 + 2
                            elif i.turn == "up" or i.turn == "down":
                                self.stop_3 = self.s7 + 3
                            else:
                                self.stop_3 = self.s7 + 4
                            break
                elif self.board[11, 28] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 28:
                            if i.turn == "right":
                                self.stop_3 = self.s7 + 1
                            elif i.turn == "up" or i.turn == "down":
                                self.stop_3 = self.s7 + 2
                            else:
                                self.stop_3 = self.s7 + 3
                            break
                elif self.board[10, 28] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 28:
                            if i.turn == "up":
                                self.stop_3 = self.s7 + 1
                            else:
                                self.stop_3 = self.s7 + 2
                            break
                elif self.board[11, 27] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 27:
                            self.stop_3 = self.s7 + 1
                            break
                elif self.board[10, 27] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 27:
                            self.stop_3 = self.s7 + 1
                            break
                else:
                    self.stop_3 = self.s7
            elif self.s8 == self.t and self.S3.color_2 == 2:
                self.S3.stop()
                self.board[self.S3.x_1, self.S3.y_1] = self.S3.color_1
                self.board[self.S3.x_2, self.S3.y_2] = self.S3.color_2
                self.board[self.S3.x_3, self.S3.y_3] = self.S3.color_3
                self.board[self.S3.x_4, self.S3.y_4] = self.S3.color_4
                if self.board[10, 29] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 29:
                            if i.turn == "_right":
                                self.stop_3 = self.s8 + 2
                            elif i.turn == "_up" or i.turn == "_down":
                                self.stop_3 = self.s8 + 3
                            else:
                                self.stop_3 = self.s8 + 4
                            break
                elif self.board[10, 28] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 28:
                            if i.turn == "_right":
                                self.stop_3 = self.s8 + 1
                            elif i.turn == "_up" or i.turn == "_down":
                                self.stop_3 = self.s8 + 2
                            else:
                                self.stop_3 = self.s8 + 3
                            break
                elif self.board[10, 27] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 27:
                            if i.turn == "_up":
                                self.stop_3 = self.s8 + 1
                            elif i.turn == "_left":
                                self.stop_3 = self.s8 + 2
                            break
                elif self.board[11, 28] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 28:
                            self.stop_3 = self.s8 + 1
                            break
                elif self.board[11, 27] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 27:
                            self.stop_3 = self.s8 + 1
                            break
                else:
                    self.stop_3 = self.s8
            elif self.s9 == self.t and self.S3.color_3 == 2:
                self.S3.stop()
                self.board[self.S3.x_1, self.S3.y_1] = self.S3.color_1
                self.board[self.S3.x_2, self.S3.y_2] = self.S3.color_2
                self.board[self.S3.x_3, self.S3.y_3] = self.S3.color_3
                self.board[self.S3.x_4, self.S3.y_4] = self.S3.color_4
                if self.board[9, 27] != 0:
                    for i in self.cars:
                        if i.x == 9 and i.y == 27:
                            if i.turn == "__right":
                                self.stop_3 = self.s9 + 2
                            elif i.turn == "__up" or i.turn == "__down":
                                self.stop_3 = self.s9 + 3
                            else:
                                self.stop_3 = self.s9 + 4
                            break
                elif self.board[10, 27] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 27:
                            if i.turn == "__right":
                                self.stop_3 = self.s9 + 1
                            elif i.turn == "__up" or i.turn == "__down":
                                self.stop_3 = self.s9 + 2
                            else:
                                self.stop_3 = self.s9 + 3
                            break
                elif self.board[11, 27] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 27:
                            if i.turn == "__up":
                                self.stop_3 = self.s9 + 1
                            elif i.turn == "__left":
                                self.stop_3 = self.s9 + 2
                            break
                elif self.board[10, 28] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 28:
                            self.stop_3 = self.s9 + 1
                            break
                elif self.board[11, 28] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 28:
                            self.stop_3 = self.s9 + 1
                            break
                else:
                    self.stop_3 = self.s9
            elif self.s10 == self.t and self.S3.color_4 == 2:
                self.S3.stop()
                self.board[self.S3.x_1, self.S3.y_1] = self.S3.color_1
                self.board[self.S3.x_2, self.S3.y_2] = self.S3.color_2
                self.board[self.S3.x_3, self.S3.y_3] = self.S3.color_3
                self.board[self.S3.x_4, self.S3.y_4] = self.S3.color_4
                if self.board[11, 10] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 10:
                            if i.turn == "___right":
                                self.stop_3 = self.s10 + 2
                            elif i.turn == "___up" or i.turn == "___down":
                                self.stop_3 = self.s10 + 3
                            else:
                                self.stop_3 = self.s10 + 4
                            break
                elif self.board[11, 11] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 11:
                            if i.turn == "___right":
                                self.stop_3 = self.s10 + 1
                            elif i.turn == "___up" or i.turn == "___down":
                                self.stop_3 = self.s10 + 2
                            else:
                                self.stop_3 = self.s10 + 3
                            break
                elif self.board[11, 12] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 12:
                            if i.turn == "___up":
                                self.stop_3 = self.s10 + 1
                            elif i.turn == "___left":
                                self.stop_3 = self.s10 + 2
                            break
                elif self.board[10, 11] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 11:
                            self.stop_3 = self.s10 + 1
                            break
                elif self.board[10, 12] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 12:
                            self.stop_3 = self.s10 + 1
                            break
                else:
                    self.stop_3 = self.s10

            if self.s11 == self.t and self.S4.color_1 == 2:
                self.S4.stop()
                self.board[self.S4.x_1, self.S4.y_1] = self.S4.color_1
                self.board[self.S4.x_2, self.S4.y_2] = self.S4.color_2
                self.board[self.S4.x_3, self.S4.y_3] = self.S4.color_3
                if self.board[11, 35] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 35:
                            if i.turn == "up" or i.turn == "down":
                                self.stop_4 = self.s11 + 3
                            else:
                                self.stop_4 = self.s11 + 4
                            break
                elif self.board[11, 36] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 36:
                            if i.turn == "up" or i.turn == "down":
                                self.stop_4 = self.s11 + 2
                            else:
                                self.stop_4 = self.s11 + 3
                            break
                elif self.board[11, 37] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 37:
                            if i.turn == "up":
                                self.stop_4 = self.s11 + 1
                            else:
                                self.stop_4 = self.s11 + 2
                            break
                elif self.board[10, 36] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 36:
                            self.stop_4 = self.s11 + 1
                            break
                elif self.board[10, 37] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 37:
                            self.stop_4 = self.s11 + 1
                            break
                else:
                    self.stop_4 = self.s11
            elif self.s12 == self.t and self.S4.color_2 == 2:
                self.S4.stop()
                self.board[self.S4.x_1, self.S4.y_1] = self.S4.color_1
                self.board[self.S4.x_2, self.S4.y_2] = self.S4.color_2
                self.board[self.S4.x_3, self.S4.y_3] = self.S4.color_3
                if self.board[9, 36] != 0:
                    for i in self.cars:
                        if i.x == 9 and i.y == 36:
                            if i.turn == "_right":
                                self.stop_4 = self.s12 + 2
                            elif i.turn == "_down":
                                self.stop_4 = self.s12 + 3
                            else:
                                self.stop_4 = self.s12 + 4
                            break
                elif self.board[10, 36] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 36:
                            if i.turn == "_right":
                                self.stop_4 = self.s12 + 1
                            elif i.turn == "_down":
                                self.stop_4 = self.s12 + 2
                            else:
                                self.stop_4 = self.s12 + 3
                            break
                elif self.board[10, 37] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 37:
                            self.stop_4 = self.s12 + 1
                            break
                elif self.board[10, 36] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 37:
                            self.stop_4 = self.s12 + 2
                            break
                elif self.board[10, 37] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 37:
                            self.stop_4 = self.s12 + 1
                            break
                else:
                    self.stop_4 = self.s12
            elif self.s11 == self.t and self.S4.color_3 == 2:
                self.S4.stop()
                self.board[self.S4.x_1, self.S4.y_1] = self.S4.color_1
                self.board[self.S4.x_2, self.S4.y_2] = self.S4.color_2
                self.board[self.S4.x_3, self.S4.y_3] = self.S4.color_3
                if self.board[10, 38] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 38:
                            if i.turn == "__right":
                                self.stop_4 = self.s13 + 2
                            else:
                                self.stop_4 = self.s13 + 3
                            break
                elif self.board[10, 37] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 37:
                            if i.turn == "__right":
                                self.stop_4 = self.s13 + 1
                            else:
                                self.stop_4 = self.s13 + 2
                            break
                elif self.board[10, 36] != 0:
                    for i in self.cars:
                        if i.x == 10 and i.y == 36:
                            self.stop_4 = self.s13 + 1
                            break
                elif self.board[11, 37] != 0:
                    for i in self.cars:
                        if i.x == 11 and i.y == 37:
                            self.stop_4 = self.s13 + 1
                            break
                else:
                    self.stop_4 = self.s13
            if self.t == self.stop_1 and self.S1.sequence[0] == 2:
                self.S1.change_color()
                self.s1 = self.stop_1 + self._s1
                self.s2 = self.stop_1 + self._s1
                self.board[self.S1.x_1, self.S1.y_1] = self.S1.color_1
                self.board[self.S1.x_2, self.S1.y_2] = self.S1.color_2
            elif self.t == self.stop_1 and self.S1.sequence[1] == 2:
                self.S1.change_color()
                self.s1 = self.stop_1 + self._s2
                self.s2 = self.stop_1 + self._s1
                self.board[self.S1.x_1, self.S1.y_1] = self.S1.color_1
                self.board[self.S1.x_2, self.S1.y_2] = self.S1.color_2

            if self.t == self.stop_2 and self.S2.sequence[0] == 2:
                self.S2.change_color()
                self.s3 = self.stop_2 + self._s3
                self.s4 = self.stop_2 + self._s3
                self.s5 = self.stop_2 + self._s3
                self.s6 = self.stop_2 + self._s3
                self.board[self.S2.x_1, self.S2.y_1] = self.S2.color_1
                self.board[self.S2.x_2, self.S2.y_2] = self.S2.color_2
                self.board[self.S2.x_3, self.S2.y_3] = self.S2.color_3
                self.board[self.S2.x_4, self.S2.y_4] = self.S2.color_4
            elif self.t == self.stop_2 and self.S2.sequence[1] == 2:
                self.S2.change_color()
                self.s3 = self.stop_2 + self._s4
                self.s4 = self.stop_2 + self._s4
                self.s5 = self.stop_2 + self._s4
                self.s6 = self.stop_2 + self._s4
                self.board[self.S2.x_1, self.S2.y_1] = self.S2.color_1
                self.board[self.S2.x_2, self.S2.y_2] = self.S2.color_2
                self.board[self.S2.x_3, self.S2.y_3] = self.S2.color_3
                self.board[self.S2.x_4, self.S2.y_4] = self.S2.color_4
            elif self.t == self.stop_2 and self.S2.sequence[2] == 2:
                self.S2.change_color()
                self.s3 = self.stop_2 + self._s5
                self.s4 = self.stop_2 + self._s5
                self.s5 = self.stop_2 + self._s5
                self.s6 = self.stop_2 + self._s5
                self.board[self.S2.x_1, self.S2.y_1] = self.S2.color_1
                self.board[self.S2.x_2, self.S2.y_2] = self.S2.color_2
                self.board[self.S2.x_3, self.S2.y_3] = self.S2.color_3
                self.board[self.S2.x_4, self.S2.y_4] = self.S2.color_4
            elif self.t == self.stop_2 and self.S2.sequence[3] == 2:
                self.S2.change_color()
                self.s3 = self.stop_2 + self._s6
                self.s4 = self.stop_2 + self._s6
                self.s5 = self.stop_2 + self._s6
                self.s6 = self.stop_2 + self._s6
                self.board[self.S2.x_1, self.S2.y_1] = self.S2.color_1
                self.board[self.S2.x_2, self.S2.y_2] = self.S2.color_2
                self.board[self.S2.x_3, self.S2.y_3] = self.S2.color_3
                self.board[self.S2.x_4, self.S2.y_4] = self.S2.color_4

            if self.t == self.stop_3 and self.S3.sequence[0] == 2:
                self.S3.change_color()
                self.s7 = self.stop_3 + self._s7
                self.s8 = self.stop_3 + self._s7
                self.s9 = self.stop_3 + self._s7
                self.s10 = self.stop_3 + self._s7
                self.board[self.S3.x_1, self.S3.y_1] = self.S3.color_1
                self.board[self.S3.x_2, self.S3.y_2] = self.S3.color_2
                self.board[self.S3.x_3, self.S3.y_3] = self.S3.color_3
                self.board[self.S3.x_4, self.S3.y_4] = self.S3.color_4
            elif self.t == self.stop_3 and self.S3.sequence[1] == 2:
                self.S3.change_color()
                self.s7 = self.stop_3 + self._s8
                self.s8 = self.stop_3 + self._s8
                self.s9 = self.stop_3 + self._s8
                self.s10 = self.stop_3 + self._s8
                self.board[self.S3.x_1, self.S3.y_1] = self.S3.color_1
                self.board[self.S3.x_2, self.S3.y_2] = self.S3.color_2
                self.board[self.S3.x_3, self.S3.y_3] = self.S3.color_3
                self.board[self.S3.x_4, self.S3.y_4] = self.S3.color_4
            elif self.t == self.stop_3 and self.S3.sequence[2] == 2:
                self.S3.change_color()
                self.s7 = self.stop_3 + self._s9
                self.s8 = self.stop_3 + self._s9
                self.s9 = self.stop_3 + self._s9
                self.s10 = self.stop_3 + self._s9
                self.board[self.S3.x_1, self.S3.y_1] = self.S3.color_1
                self.board[self.S3.x_2, self.S3.y_2] = self.S3.color_2
                self.board[self.S3.x_3, self.S3.y_3] = self.S3.color_3
                self.board[self.S3.x_4, self.S3.y_4] = self.S3.color_4
            elif self.t == self.stop_3 and self.S3.sequence[3] == 2:
                self.S3.change_color()
                self.s7 = self.stop_3 + self._s10
                self.s8 = self.stop_3 + self._s10
                self.s9 = self.stop_3 + self._s10
                self.s10 = self.stop_3 + self._s10
                self.board[self.S3.x_1, self.S3.y_1] = self.S3.color_1
                self.board[self.S3.x_2, self.S3.y_2] = self.S3.color_2
                self.board[self.S3.x_3, self.S3.y_3] = self.S3.color_3
                self.board[self.S3.x_4, self.S3.y_4] = self.S3.color_4

            if self.t == self.stop_4 and self.S4.sequence[0] == 2:
                self.S4.change_color()
                self.s11 = self.stop_4 + self._s11
                self.s12 = self.stop_4 + self._s11
                self.s13 = self.stop_4 + self._s11
                self.board[self.S4.x_1, self.S4.y_1] = self.S4.color_1
                self.board[self.S4.x_2, self.S4.y_2] = self.S4.color_2
                self.board[self.S4.x_3, self.S4.y_3] = self.S4.color_3
            elif self.t == self.stop_4 and self.S4.sequence[1] == 2:
                self.S4.change_color()
                self.s11 = self.stop_4 + self._s12
                self.s12 = self.stop_4 + self._s12
                self.s13 = self.stop_4 + self._s12
                self.board[self.S4.x_1, self.S4.y_1] = self.S4.color_1
                self.board[self.S4.x_2, self.S4.y_2] = self.S4.color_2
                self.board[self.S4.x_3, self.S4.y_3] = self.S4.color_3
            elif self.t == self.stop_4 and self.S4.sequence[2] == 2:
                self.S4.change_color()
                self.s11 = self.stop_4 + self._s13
                self.s12 = self.stop_4 + self._s13
                self.s13 = self.stop_4 + self._s13
                self.board[self.S4.x_1, self.S4.y_1] = self.S4.color_1
                self.board[self.S4.x_2, self.S4.y_2] = self.S4.color_2
                self.board[self.S4.x_3, self.S4.y_3] = self.S4.color_3

            for i in self.cars:
                self.board[i.x, i.y] = i.color

            if self.remaining_1:
                if self.board[self.remaining_1[-1].x, self.remaining_1[-1].y] == 0:
                    car = self.remaining_1.pop()
                    self.board[car.x, car.y] = car.color
                    self.cars.append(car)
            if self.remaining_2:
                if self.board[self.remaining_2[-1].x, self.remaining_2[-1].y] == 0:
                    car = self.remaining_2.pop()
                    self.board[car.x, car.y] = car.color
                    self.cars.append(car)
            if self.remaining_3:
                if self.board[self.remaining_3[-1].x, self.remaining_3[-1].y] == 0:
                    car = self.remaining_3.pop()
                    self.board[car.x, car.y] = car.color
                    self.cars.append(car)
            if self.remaining_4:
                if self.board[self.remaining_4[-1].x, self.remaining_4[-1].y] == 0:
                    car = self.remaining_4.pop()
                    self.board[car.x, car.y] = car.color
                    self.cars.append(car)
            if self.remaining_5:
                if self.board[self.remaining_5[-1].x, self.remaining_5[-1].y] == 0:
                    car = self.remaining_5.pop()
                    self.board[car.x, car.y] = car.color
                    self.cars.append(car)
            if self.remaining_6:
                if self.board[self.remaining_6[-1].x, self.remaining_6[-1].y] == 0:
                    car = self.remaining_6.pop()
                    self.board[car.x, car.y] = car.color
                    self.cars.append(car)
            if self.remaining_7:
                if self.board[self.remaining_7[-1].x, self.remaining_7[-1].y] == 0:
                    car = self.remaining_7.pop()
                    self.board[car.x, car.y] = car.color
                    self.cars.append(car)

            self.data_3d = np.ndarray(shape=(self.board.shape[0], self.board.shape[1], 3), dtype=int)
            for i in range(0, self.board.shape[0]):
                for j in range(0, self.board.shape[1]):
                    self.data_3d[i][j] = self.color_map[self.board[i][j]]
            self.a.clear()
            self.a.axis("off")
            self.a.imshow(self.data_3d)
            self.figure.canvas.draw()
            self.save_animation.append(self.data_3d)
            plt.pause(0.5)
            self.t += 1


if __name__ == "__main__":
    global root
    root = Tk()
    root.title("Symulacja ruchu samochodowego")
    my_window = Window(root)
    root.mainloop()
