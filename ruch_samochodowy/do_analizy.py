import random
import numpy as np
import matplotlib.pyplot as plt


class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.randint(3, 8)
        self.turn = None
        self.time = 0

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


lambda_1 = lambda t: 0.8 + 0.8 * np.sin(t / 2)
lambda_2 = lambda t: np.exp((2 * np.sin(t / 12 + 3) - 0.9) ** 3)
lambda_3 = lambda t: 0.5 * (t + 1) / (t + 1)
lambda_4 = lambda t: 0.7 + 0.6 * (np.sin(t / 7 + 2)) ** 2 * np.cos(t / 3 + 1)
lambda_5 = lambda t: 0.2 + 0.2 * np.sign(np.sin(t / 24 + 6))
lambda_6 = lambda t: 0.1 + 0.1 * np.sin(np.sqrt(t))
lambda_7 = lambda t: 0.3 + 0.3 * np.sin(4 * np.sin(t / 2))


def main(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13):
    _s1, _s2, _s3, _s4, _s5, _s6, _s7, _s8, _s9, _s10, _s11, _s12, _s13 = s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13
    color_map = {-1: np.array([0, 90, 0]),  # dark green
                 0: np.array([0, 0, 0]),  # black
                 1: np.array([255, 0, 0]),  # red
                 2: np.array([0, 255, 0]),  # green
                 3: np.array([255, 255, 255]),  # white
                 4: np.array([255, 255, 0]),  # yellow
                 5: np.array([204, 0, 204]),  # purple
                 6: np.array([255, 102, 255]),  # pink
                 7: np.array([255, 128, 0]),  # orange
                 8: np.array([153, 255, 255])}  # blue
    board = np.zeros((29, 42))
    board[:10, :11] = -1
    board[12:23, :11] = -1
    board[24:, :11] = -1
    board[:10, 13:27] = -1
    board[12:, 13:27] = -1
    board[:10, 29:36] = -1
    board[:10, 38:] = -1
    board[12:, 29:] = -1

    S1 = Traffic_light1(24, 13)
    board[S1.x_1, S1.y_1] = S1.color_1
    board[S1.x_2, S1.y_2] = S1.color_2

    S2 = Traffic_light2_3(12, 13)
    board[S2.x_1, S2.y_1] = S2.color_1
    board[S2.x_2, S2.y_2] = S2.color_2
    board[S2.x_3, S2.y_3] = S2.color_3
    board[S2.x_4, S2.y_4] = S2.color_4

    S3 = Traffic_light2_3(12, 29)
    board[S3.x_1, S3.y_1] = S3.color_1
    board[S3.x_2, S3.y_2] = S3.color_2
    board[S3.x_3, S3.y_3] = S3.color_3
    board[S3.x_4, S3.y_4] = S3.color_4

    S4 = Traffic_light4(12, 35)
    board[S4.x_1, S4.y_1] = S4.color_1
    board[S4.x_2, S4.y_2] = S4.color_2
    board[S4.x_3, S4.y_3] = S4.color_3

    time_1 = generating_jump_moments(1000, lambda_1)[0]
    time_1 = [np.ceil(i) for i in time_1]
    time_2 = generating_jump_moments(1000, lambda_2)[0]
    time_2 = [np.ceil(i) for i in time_2]
    time_3 = generating_jump_moments(1000, lambda_3)[0]
    time_3 = [np.ceil(i) for i in time_3]
    time_4 = generating_jump_moments(1000, lambda_4)[0]
    time_4 = [np.ceil(i) for i in time_4]
    time_5 = generating_jump_moments(1000, lambda_5)[0]
    time_5 = [np.ceil(i) for i in time_5]
    time_6 = generating_jump_moments(1000, lambda_6)[0]
    time_6 = [np.ceil(i) for i in time_6]
    time_7 = generating_jump_moments(1000, lambda_7)[0]
    time_7 = [np.ceil(i) for i in time_7]
    t = 0
    remaining_1 = []
    remaining_2 = []
    remaining_3 = []
    remaining_4 = []
    remaining_5 = []
    remaining_6 = []
    remaining_7 = []
    cars = []
    stop_1 = 0
    stop_2 = 0
    stop_3 = 0
    stop_4 = 0

    cars_number = []
    remaining_cars_number = []
    times = []

    for t in range(101):
        for i in cars:
            if i.x != board.shape[0] - 1 and i.x != 0 and i.y != board.shape[1] - 1 and i.y != 0:  # todo
                if board[i.x, i.y - 1] == -1 and board[i.x, i.y + 1] == -1:
                    i.move_left()
                elif board[i.x - 1, i.y] == -1 and i.turn == None:
                    if board[i.x, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                elif board[i.x, i.y + 1] == -1 and i.turn == None:
                    if board[i.x - 1, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                elif board[i.x + 1, i.y] == -1 and i.turn == None:
                    if board[i.x, i.y + 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                elif board[i.x, i.y - 1] == -1 and i.turn == None:
                    if board[i.x + 1, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()


                elif board[i.x, i.y + 1] == 2 and i.x == 24 and i.y == 12:  # najmniejsze skrzyżowanie
                    if i.turn == None:
                        turn = random.randint(1, 3)
                        if turn == 1:
                            i.turn = "up"
                        elif turn == 2:
                            i.turn = "left"
                        else:
                            i.turn = "down"
                    if i.turn == "up" and board[i.x - 2, i.y] == 0 and board[i.x - 1, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                        i.turn = None
                        board[i.x, i.y] = i.color
                    elif i.turn == "left" and board[i.x - 1, i.y] == 0 and board[i.x - 1, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                        board[i.x, i.y] = i.color
                    elif i.turn == 'down' and board[i.x - 1, i.y] == 0 and board[
                        i.x - 1, i.y - 1] == 0 and board[
                        i.x - 1, i.y - 2] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                        board[i.x, i.y] = i.color
                elif i.x == 23 and i.y == 12 and (i.turn == "left" or i.turn == 'down'):
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 23 and i.y == 11 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 23 and i.y == 10 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_left()
                    i.turn = None
                    board[i.x, i.y] = i.color
                elif i.x == 23 and i.y == 11 and i.turn == 'down':
                    board[i.x, i.y] = 0
                    i.move_down()
                    i.turn = None
                    board[i.x, i.y] = i.color
                elif board[i.x, i.y - 1] == 2 and i.x == 22 and i.y == 11:  # druga strona
                    if i.turn == None:
                        turn = random.randint(1, 3)
                        if turn == 1:
                            i.turn = "_up"
                        elif turn == 2:
                            i.turn = "_right"
                        else:
                            i.turn = "_down"
                    if i.turn == "_up" and board[i.x + 1, i.y] == 0 and board[i.x + 2, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                    elif i.turn == "_right" and board[i.x + 1, i.y] == 0 and board[i.x + 1, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                    elif i.turn == "_down" and board[i.x + 1, i.y] == 0 and board[
                        i.x + 1, i.y + 1] == 0 and board[
                        i.x, i.y + 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                elif i.x == 23 and i.y == 11 and i.turn == "_up":
                    board[i.x, i.y] = 0
                    i.move_down()
                    i.turn = None
                    board[i.x, i.y] = i.color
                elif i.x == 23 and i.y == 11 and i.turn == "_right":
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 23 and i.y == 10 and i.turn == "_right":
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 23 and i.y == 11 and i.turn == '_down':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif board[i.x, i.y + 1] == 2 and i.x == 12 and i.y == 12:  # skrzyżowanie pierwsze od gory
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
                    if i.turn == 'right' and board[i.x - 1, i.y] == 0 and board[i.x - 1, i.y + 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                        board[i.x, i.y] = i.color
                    elif i.turn == 'up' and board[i.x - 1, i.y] == 0 and board[i.x - 2, i.y] == 0 and \
                            board[
                                i.x - 3, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                        board[i.x, i.y] = i.color
                    elif i.turn == "left" and board[i.x - 1, i.y] == 0 and board[i.x - 2, i.y] == 0 and \
                            board[
                                i.x - 2, i.y - 1] == 0 and board[i.x - 2, i.y - 2] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                        board[i.x, i.y] = i.color
                    elif i.turn == 'down' and board[i.x - 1, i.y] == 0 and board[
                        i.x - 1, i.y - 1] == 0 and board[
                        i.x, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                        board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 12 and i.turn == 'right':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 13 and i.turn == 'right':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 12 and i.turn == 'up':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 12 and i.turn == 'up':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 9 and i.y == 12 and i.turn == 'up':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 12 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 12 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 11 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 10 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 12 and i.turn == 'down':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 11 and i.turn == 'down':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 12 and i.y == 11 and i.turn == 'down':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif board[i.x - 1, i.y] == 2 and i.x == 10 and i.y == 13:  # prawa strona tego skrzyzowania
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
                    if i.turn == '_right' and board[i.x, i.y - 1] == 0 and board[i.x - 1, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                        board[i.x, i.y] = i.color
                    elif i.turn == "_up" and board[i.x, i.y - 1] == 0 and board[i.x, i.y - 2] == 0 and \
                            board[
                                i.x, i.y - 3] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                        board[i.x, i.y] = i.color
                    elif i.turn == '_left' and board[i.x, i.y - 1] == 0 and board[i.x, i.y - 2] == 0 and \
                            board[
                                i.x + 1, i.y - 2] == 0 and board[i.x + 2, i.y - 2] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                        board[i.x, i.y] = i.color
                    elif i.turn == '_down' and board[i.x, i.y - 1] == 0 and board[
                        i.x + 1, i.y - 1] == 0 and board[
                        i.x + 1, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                        board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 12 and i.turn == '_right':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 9 and i.y == 12 and i.turn == '_right':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 12 and i.turn == '_up':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 11 and i.turn == '_up':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 10 and i.turn == '_up':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 12 and i.turn == '_left':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 11 and i.turn == '_left':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 11 and i.turn == '_left':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 12 and i.y == 11 and i.turn == '_left':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 12 and i.turn == '_down':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 12 and i.turn == "_down":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 13 and i.turn == "_down":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif board[i.x, i.y - 1] == 2 and i.x == 9 and i.y == 11:  # górna strona tego skrzyżowania
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
                    if i.turn == '__right' and board[i.x + 1, i.y] == 0 and board[i.x + 1, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                    elif i.turn == '__up' and board[i.x + 1, i.y] == 0 and board[i.x + 2, i.y] == 0 and \
                            board[
                                i.x + 3, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                    elif i.turn == '__left' and board[i.x + 1, i.y] == 0 and board[i.x + 2, i.y] == 0 and \
                            board[
                                i.x + 2, i.y + 1] == 0 and board[i.x + 2, i.y + 2] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                    elif i.turn == '__down' and board[i.x + 1, i.y] == 0 and board[
                        i.x + 1, i.y + 1] == 0 and board[
                        i.x, i.y + 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 11 and i.turn == "__right":
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 10 and i.turn == "__right":
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 11 and i.turn == "__up":
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 11 and i.turn == "__up":
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 12 and i.y == 11 and i.turn == "__up":
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 11 and i.turn == '__left':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 11 and i.turn == "__left":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 12 and i.turn == "__left":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 13 and i.turn == "__left":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 11 and i.turn == '__down':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 12 and i.turn == "__down":
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 9 and i.y == 12 and i.turn == "__down":
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif board[i.x + 1, i.y] == 2 and i.x == 11 and i.y == 10:  # lewa strona tego skrzyżowania
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
                    if i.turn == '___right' and board[i.x, i.y + 1] == 0 and board[i.x + 1, i.y + 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                        board[i.x, i.y] = i.color
                    elif i.turn == '___up' and board[i.x, i.y + 1] == 0 and board[i.x, i.y + 2] == 0 and \
                            board[
                                i.x, i.y + 3] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                        board[i.x, i.y] = i.color
                    elif i.turn == '___left' and board[i.x, i.y + 1] == 0 and board[i.x, i.y + 2] == 0 and \
                            board[
                                i.x - 1, i.y + 2] == 0 and board[i.x - 2, i.y + 2] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                        board[i.x, i.y] = i.color
                    elif i.turn == '___down' and board[i.x, i.y + 1] == 0 and board[
                        i.x - 1, i.y + 1] == 0 and \
                            board[i.x - 1, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                        board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 11 and i.turn == "___right":
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 12 and i.y == 11 and i.turn == "___right":
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 11 and i.turn == "___up":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 12 and i.turn == "___up":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 13 and i.turn == "___up":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 11 and i.turn == "___left":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 12 and i.turn == '___left':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 12 and i.turn == '___left':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 9 and i.y == 12 and i.turn == '___left':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 11 and i.turn == "___down":
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 11 and i.turn == "___down":
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 10 and i.turn == "___down":
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None




                ##############################

                elif board[i.x, i.y + 1] == 2 and i.x == 12 and i.y == 28:  # skrzyżowanie drugie od gory
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
                    if i.turn == 'right' and board[i.x - 1, i.y] == 0 and board[i.x - 1, i.y + 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                        board[i.x, i.y] = i.color
                    elif i.turn == 'up' and board[i.x - 1, i.y] == 0 and board[i.x - 2, i.y] == 0 and \
                            board[
                                i.x - 3, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                        board[i.x, i.y] = i.color
                    elif i.turn == "left" and board[i.x - 1, i.y] == 0 and board[i.x - 2, i.y] == 0 and \
                            board[
                                i.x - 2, i.y - 1] == 0 and board[i.x - 2, i.y - 2] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                        board[i.x, i.y] = i.color
                    elif i.turn == 'down' and board[i.x - 1, i.y] == 0 and board[
                        i.x - 1, i.y - 1] == 0 and board[
                        i.x, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                        board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 28 and i.turn == 'right':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 29 and i.turn == 'right':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 28 and i.turn == 'up':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 28 and i.turn == 'up':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 9 and i.y == 28 and i.turn == 'up':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 28 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 28 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 27 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 26 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 28 and i.turn == 'down':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 27 and i.turn == 'down':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 12 and i.y == 27 and i.turn == 'down':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif board[i.x - 1, i.y] == 2 and i.x == 10 and i.y == 29:  # prawa strona tego skrzyzowania
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
                    if i.turn == '_right' and board[i.x, i.y - 1] == 0 and board[i.x - 1, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                        board[i.x, i.y] = i.color
                    elif i.turn == "_up" and board[i.x, i.y - 1] == 0 and board[i.x, i.y - 2] == 0 and \
                            board[
                                i.x, i.y - 3] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                        board[i.x, i.y] = i.color
                    elif i.turn == '_left' and board[i.x, i.y - 1] == 0 and board[i.x, i.y - 2] == 0 and \
                            board[
                                i.x + 1, i.y - 2] == 0 and board[i.x + 2, i.y - 2] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                        board[i.x, i.y] = i.color
                    elif i.turn == '_down' and board[i.x, i.y - 1] == 0 and board[
                        i.x + 1, i.y - 1] == 0 and board[
                        i.x + 1, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                        board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 28 and i.turn == '_right':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 9 and i.y == 28 and i.turn == '_right':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 28 and i.turn == '_up':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 27 and i.turn == '_up':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 26 and i.turn == '_up':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 28 and i.turn == '_left':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 27 and i.turn == '_left':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 27 and i.turn == '_left':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 12 and i.y == 27 and i.turn == '_left':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 28 and i.turn == '_down':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 28 and i.turn == "_down":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 29 and i.turn == "_down":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif board[i.x, i.y - 1] == 2 and i.x == 9 and i.y == 27:  # górna strona tego skrzyżowania
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
                    if i.turn == '__right' and board[i.x + 1, i.y] == 0 and board[i.x + 1, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                    elif i.turn == '__up' and board[i.x + 1, i.y] == 0 and board[i.x + 2, i.y] == 0 and \
                            board[
                                i.x + 3, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                    elif i.turn == '__left' and board[i.x + 1, i.y] == 0 and board[i.x + 2, i.y] == 0 and \
                            board[
                                i.x + 2, i.y + 1] == 0 and board[i.x + 2, i.y + 2] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                    elif i.turn == '__down' and board[i.x + 1, i.y] == 0 and board[
                        i.x + 1, i.y + 1] == 0 and board[
                        i.x, i.y + 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 27 and i.turn == "__right":
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 26 and i.turn == "__right":
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 27 and i.turn == "__up":
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 27 and i.turn == "__up":
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 12 and i.y == 27 and i.turn == "__up":
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 27 and i.turn == '__left':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 27 and i.turn == "__left":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 28 and i.turn == "__left":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 29 and i.turn == "__left":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 27 and i.turn == '__down':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 28 and i.turn == "__down":
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 9 and i.y == 28 and i.turn == "__down":
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif board[i.x + 1, i.y] == 2 and i.x == 11 and i.y == 26:  # lewa strona tego skrzyżowania
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
                    if i.turn == '___right' and board[i.x, i.y + 1] == 0 and board[i.x + 1, i.y + 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                        board[i.x, i.y] = i.color
                    elif i.turn == '___up' and board[i.x, i.y + 1] == 0 and board[i.x, i.y + 2] == 0 and \
                            board[
                                i.x, i.y + 3] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                        board[i.x, i.y] = i.color
                    elif i.turn == '___left' and board[i.x, i.y + 1] == 0 and board[i.x, i.y + 2] == 0 and \
                            board[
                                i.x - 1, i.y + 2] == 0 and board[i.x - 2, i.y + 2] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                        board[i.x, i.y] = i.color
                    elif i.turn == '___down' and board[i.x, i.y + 1] == 0 and board[
                        i.x - 1, i.y + 1] == 0 and \
                            board[i.x - 1, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                        board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 27 and i.turn == "___right":
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 12 and i.y == 27 and i.turn == "___right":
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 27 and i.turn == "___up":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 28 and i.turn == "___up":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 29 and i.turn == "___up":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 27 and i.turn == "___left":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 28 and i.turn == '___left':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 28 and i.turn == '___left':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 9 and i.y == 28 and i.turn == '___left':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 27 and i.turn == "___down":
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 27 and i.turn == "___down":
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 26 and i.turn == "___down":
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None
                ###############################
                elif board[i.x + 1, i.y] == 2 and i.x == 11 and i.y == 35:
                    if i.turn == None:
                        turn = random.randint(1, 3)
                        if turn == 1:
                            i.turn = 'up'
                        elif turn == 2:
                            i.turn = 'left'
                        else:
                            i.turn = "down"
                    if i.turn == 'up' and board[i.x, i.y + 1] == 0 and board[i.x, i.y + 2] == 0 and \
                            board[
                                i.x, i.y + 3] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                        board[i.x, i.y] = i.color
                    elif i.turn == 'left' and board[i.x, i.y + 1] == 0 and board[i.x, i.y + 2] == 0 and \
                            board[
                                i.x - 1, i.y + 2] == 0 and board[i.x - 2, i.y + 2] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                        board[i.x, i.y] = i.color
                    elif i.turn == 'down' and board[i.x, i.y + 1] == 0 and board[
                        i.x - 1, i.y + 1] == 0 and board[
                        i.x - 1, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                        board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 36 and i.turn == 'up':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 37 and i.turn == 'up':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 38 and i.turn == 'up':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 36 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 37 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 37 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 9 and i.y == 37 and i.turn == 'left':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 11 and i.y == 36 and i.turn == 'down':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 36 and i.turn == 'down':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 35 and i.turn == 'down':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None

                elif board[i.x - 1, i.y] == 2 and i.x == 10 and i.y == 38:  # prawa strona tego skrzyżowania
                    if i.turn == None:
                        turn = random.randint(1, 3)
                        if turn == 1:
                            i.turn = '_up'
                        elif turn == 2:
                            i.turn = '_right'
                        else:
                            i.turn = "_down"
                    if i.turn == '_up' and board[i.x, i.y - 1] == 0 and board[i.x, i.y - 2] == 0 and \
                            board[
                                i.x, i.y - 3] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                        board[i.x, i.y] = i.color
                    elif i.turn == '_right' and board[i.x, i.y - 1] == 0 and board[i.x - 1, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                        board[i.x, i.y] = i.color
                    elif i.turn == '_down' and board[i.x, i.y - 1] == 0 and board[
                        i.x + 1, i.y + 1] == 0 and board[
                        i.x + 1, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                        board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 37 and i.turn == '_up':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 36 and i.turn == '_up':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 35 and i.turn == '_up':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 37 and i.turn == '_right':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 9 and i.y == 37 and i.turn == '_right':
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 37 and i.turn == '_down':
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 37 and i.turn == '_down':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 11 and i.y == 38 and i.turn == '_down':
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif board[i.x, i.y - 1] == 2 and i.x == 9 and i.y == 36:  # górna strona tego skrzyżowania
                    if i.turn == None:
                        turn = random.randint(1, 3)
                        if turn == 1:
                            i.turn = '__right'
                        elif turn == 2:
                            i.turn = '__left'
                        else:
                            i.turn = "__down"
                    if i.turn == "__right" and board[i.x + 1, i.y] == 0 and board[i.x + 1, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                    elif i.turn == "__left" and board[i.x + 1, i.y] == 0 and board[i.x + 2, i.y] == 0 and \
                            board[
                                i.x + 2, i.y + 1] == 0 and board[i.x + 2, i.y + 2] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                    elif i.turn == '__down' and board[i.x + 1, i.y] == 0 and board[
                        i.x + 1, i.y + 1] == 0 and board[
                        i.x, i.y + 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                        board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 36 and i.turn == '__right':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 35 and i.turn == '__right':
                    board[i.x, i.y] = 0
                    i.move_left()
                    board[i.x, i.y] = i.color
                    i.turn = None
                elif i.x == 10 and i.y == 36 and i.turn == "__left":
                    board[i.x, i.y] = 0
                    i.move_down()
                    board[i.x, i.y] = i.color
                    i.turn = None
                ## możliwe, że tu trzeba będzie poprawić - zakręt z górnego skrzyżowania w lewo

                elif i.x == 10 and i.y == 36 and i.turn == "__down":
                    board[i.x, i.y] = 0
                    i.move_right()
                    board[i.x, i.y] = i.color
                elif i.x == 10 and i.y == 37 and i.turn == "__down":
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                elif i.x == 9 and i.y == 37 and i.turn == "__down":
                    board[i.x, i.y] = 0
                    i.move_up()
                    board[i.x, i.y] = i.color
                    i.turn = None









            ##############################

            elif (i.x == 23 and i.y == 0) or (i.x == 28 and i.y == 11) or (i.x == 28 and i.y == 27) or (
                    i.x == 11 and i.y == 41) or (i.x == 0 and i.y == 37) \
                    or (i.x == 0 and i.y == 28) or (i.x == 10 and i.y == 0) or (i.x == 0 and i.y == 12):
                board[i.x, i.y] = 0
                cars.remove(i)
                times.append(i.time)
                del i

            elif i.x == board.shape[0] - 1:
                if board[i.x, i.y + 1] == -1:
                    if board[i.x - 1, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_up()
                else:
                    cars.remove(i)
                    times.append(i.time)
                    del i
            elif i.x == 0:
                if board[i.x, i.y - 1] == -1:
                    if board[i.x + 1, i.y] == 0:
                        board[i.x, i.y] = 0
                        i.move_down()
                else:
                    cars.remove(i)
                    times.append(i.time)
                    del i
            elif i.y == board.shape[1] - 1:
                if board[i.x - 1, i.y] == -1:
                    if board[i.x, i.y - 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_left()
                else:
                    cars.remove(i)
                    times.append(i.time)
                    del i
            elif i.y == 0:
                if board[i.x + 1, i.y] == -1:
                    if board[i.x, i.y + 1] == 0:
                        board[i.x, i.y] = 0
                        i.move_right()
                else:
                    cars.remove(i)
                    times.append(i.time)
                    del i
        while True:
            if time_1[0] == t:
                if len(time_1) == 1:
                    temp = time_1.pop(0)
                    time_1 = generating_jump_moments(1000, lambda_1)[0]
                    time_1 = [np.ceil(i) + temp for i in time_1]
                car = Car(28, 12)
                time_1.pop(0)
                if board[car.x, car.y] == 0:
                    board[car.x, car.y] = car.color
                    cars.append(car)
                else:
                    remaining_1.append(car)
            else:
                break
        while True:
            if time_2[0] == t:
                if len(time_2) == 1:
                    temp = time_2.pop(0)
                    time_2 = generating_jump_moments(1000, lambda_2)[0]
                    time_2 = [np.ceil(i) + temp for i in time_2]
                car = Car(28, 28)
                time_2.pop(0)
                if board[car.x, car.y] == 0:
                    board[car.x, car.y] = car.color
                    cars.append(car)
                else:
                    remaining_2.append(car)
            else:
                break
        while True:
            if time_3[0] == t:
                if len(time_3) == 1:
                    temp = time_3.pop(0)
                    time_3 = generating_jump_moments(1000, lambda_3)[0]
                    time_3 = [np.ceil(i) + temp for i in time_3]
                car = Car(10, 41)
                time_3.pop(0)
                if board[car.x, car.y] == 0:
                    board[car.x, car.y] = car.color
                    cars.append(car)
                else:
                    remaining_3.append(car)
            else:
                break
        while True:
            if time_4[0] == t:
                if len(time_4) == 1:
                    temp = time_4.pop(0)
                    time_4 = generating_jump_moments(1000, lambda_4)[0]
                    time_4 = [np.ceil(i) + temp for i in time_4]
                car = Car(11, 0)
                time_4.pop(0)
                if board[car.x, car.y] == 0:
                    board[car.x, car.y] = car.color
                    cars.append(car)
                else:
                    remaining_4.append(car)
            else:
                break
        while True:
            if time_5[0] == t:
                if len(time_5) == 1:
                    temp = time_5.pop(0)
                    time_5 = generating_jump_moments(1000, lambda_5)[0]
                    time_5 = [np.ceil(i) + temp for i in time_5]
                car = Car(0, 11)
                time_5.pop(0)
                if board[car.x, car.y] == 0:
                    board[car.x, car.y] = car.color
                    cars.append(car)
                else:
                    remaining_5.append(car)
            else:
                break
        while True:
            if time_6[0] == t:
                if len(time_6) == 1:
                    temp = time_6.pop(0)
                    time_6 = generating_jump_moments(1000, lambda_6)[0]
                    time_6 = [np.ceil(i) + temp for i in time_6]
                car = Car(0, 27)
                time_6.pop(0)
                if board[car.x, car.y] == 0:
                    board[car.x, car.y] = car.color
                    cars.append(car)
                else:
                    remaining_6.append(car)
            else:
                break
        while True:
            if time_7[0] == t:
                if len(time_7) == 1:
                    temp = time_7.pop(0)
                    time_7 = generating_jump_moments(1000, lambda_7)[0]
                    time_7 = [np.ceil(i) + temp for i in time_7]
                car = Car(0, 36)
                time_7.pop(0)
                if board[car.x, car.y] == 0:
                    board[car.x, car.y] = car.color
                    cars.append(car)
                else:
                    remaining_7.append(car)
            else:
                break
        if s1 == t and S1.color_1 == 2:
            S1.stop()
            board[S1.x_1, S1.y_1] = S1.color_1
            board[S1.x_2, S1.y_2] = S1.color_2
            if board[24, 12] != 0:
                for i in cars:
                    if i.x == 24 and i.y == 12:
                        if i.turn == "up":
                            stop_1 = s1 + 2
                        else:
                            stop_1 = s1 + 3
                        break
            elif board[23, 12] != 0:
                for i in cars:
                    if i.x == 23 and i.y == 12:
                        if i.turn == "up":
                            stop_1 = s1 + 1
                        else:
                            stop_1 = s1 + 2
                        break
            elif board[23, 11] != 0:
                for i in cars:
                    if i.x == 23 and i.y == 11:
                        stop_1 = s1 + 1
                        break
            else:
                stop_1 = s1
        elif s2 == t and S1.color_2 == 2:
            S1.stop()
            board[S1.x_1, S1.y_1] = S1.color_1
            board[S1.x_2, S1.y_2] = S1.color_2
            if board[22, 11] != 0:
                for i in cars:
                    if i.x == 22 and i.y == 11:
                        if i.turn == "_up":
                            stop_1 = s2 + 2
                        else:
                            stop_1 = s2 + 3
                        break
            elif board[23, 11] != 0:
                for i in cars:
                    if i.x == 23 and i.y == 11:
                        if i.turn == "_right" or i.turn == '_up':
                            stop_1 = s2 + 1
                        else:
                            stop_1 = s2 + 2
                        break
            elif board[23, 12] != 0:
                for i in cars:
                    if i.x == 23 and i.y == 12:
                        stop_1 = s2 + 1
                        break
            else:
                stop_1 = s2

        if s3 == t and S2.color_1 == 2:
            S2.stop()
            board[S2.x_1, S2.y_1] = S2.color_1
            board[S2.x_2, S2.y_2] = S2.color_2
            board[S2.x_3, S2.y_3] = S2.color_3
            board[S2.x_4, S2.y_4] = S2.color_4
            if board[12, 12] != 0:
                for i in cars:
                    if i.x == 12 and i.y == 12:
                        if i.turn == "right":
                            stop_2 = s3 + 2
                        elif i.turn == "up" or i.turn == "down":
                            stop_2 = s3 + 3
                        else:
                            stop_2 = s3 + 4
                        break
            elif board[11, 12] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 12:
                        if i.turn == "right":
                            stop_2 = s3 + 1
                        elif i.turn == "up" or i.turn == "down":
                            stop_2 = s3 + 2
                        else:
                            stop_2 = s3 + 3
                        break
            elif board[10, 12] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 12:
                        if i.turn == "up":
                            stop_2 = s3 + 1
                        else:
                            stop_2 = s3 + 2
                        break
            elif board[11, 11] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 11:
                        stop_2 = s3 + 1
                        break
            elif board[10, 11] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 11:
                        stop_2 = s3 + 1
                        break
            else:
                stop_2 = s3
        elif s4 == t and S2.color_2 == 2:
            S2.stop()
            board[S2.x_1, S2.y_1] = S2.color_1
            board[S2.x_2, S2.y_2] = S2.color_2
            board[S2.x_3, S2.y_3] = S2.color_3
            board[S2.x_4, S2.y_4] = S2.color_4
            if board[10, 13] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 13:
                        if i.turn == "_right":
                            stop_2 = s4 + 2
                        elif i.turn == "_up" or i.turn == "_down":
                            stop_2 = s4 + 3
                        else:
                            stop_2 = s4 + 4
                        break
            elif board[10, 12] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 12:
                        if i.turn == "_right":
                            stop_2 = s4 + 1
                        elif i.turn == "_up" or i.turn == "_down":
                            stop_2 = s4 + 2
                        else:
                            stop_2 = s4 + 3
                        break
            elif board[10, 11] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 11:
                        if i.turn == "_up":
                            stop_2 = s4 + 1
                        elif i.turn == "_left":
                            stop_2 = s4 + 2
                        break
            elif board[11, 12] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 12:
                        stop_2 = s4 + 1
                        break
            elif board[11, 11] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 11:
                        stop_2 = s4 + 1
                        break
            else:
                stop_2 = s4
        elif s5 == t and S2.color_3 == 2:
            S2.stop()
            board[S2.x_1, S2.y_1] = S2.color_1
            board[S2.x_2, S2.y_2] = S2.color_2
            board[S2.x_3, S2.y_3] = S2.color_3
            board[S2.x_4, S2.y_4] = S2.color_4
            if board[9, 11] != 0:
                for i in cars:
                    if i.x == 9 and i.y == 11:
                        if i.turn == "__right":
                            stop_2 = s5 + 2
                        elif i.turn == "__up" or i.turn == "__down":
                            stop_2 = s5 + 3
                        else:
                            stop_2 = s5 + 4
                        break
            elif board[10, 11] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 11:
                        if i.turn == "__right":
                            stop_2 = s5 + 1
                        elif i.turn == "__up" or i.turn == "__down":
                            stop_2 = s5 + 2
                        else:
                            stop_2 = s5 + 3
                        break
            elif board[11, 11] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 11:
                        if i.turn == "__up":
                            stop_2 = s5 + 1
                        elif i.turn == "__left":
                            stop_2 = s5 + 2
                        break
            elif board[10, 12] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 12:
                        stop_2 = s5 + 1
                        break
            elif board[11, 12] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 12:
                        stop_2 = s5 + 1
                        break
            else:
                stop_2 = s5
        elif s6 == t and S2.color_4 == 2:
            S2.stop()
            board[S2.x_1, S2.y_1] = S2.color_1
            board[S2.x_2, S2.y_2] = S2.color_2
            board[S2.x_3, S2.y_3] = S2.color_3
            board[S2.x_4, S2.y_4] = S2.color_4
            if board[11, 10] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 10:
                        if i.turn == "___right":
                            stop_2 = s6 + 2
                        elif i.turn == "___up" or i.turn == "___down":
                            stop_2 = s6 + 3
                        else:
                            stop_2 = s6 + 4
                        break
            elif board[11, 11] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 11:
                        if i.turn == "___right":
                            stop_2 = s6 + 1
                        elif i.turn == "___up" or i.turn == "___down":
                            stop_2 = s6 + 2
                        else:
                            stop_2 = s6 + 3
                        break
            elif board[11, 12] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 12:
                        if i.turn == "___up":
                            stop_2 = s6 + 1
                        elif i.turn == "___left":
                            stop_2 = s6 + 2
                        break
            elif board[10, 11] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 11:
                        stop_2 = s6 + 1
                        break
            elif board[10, 12] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 12:
                        stop_2 = s6 + 1
                        break
            else:
                stop_2 = s6

        if s7 == t and S3.color_1 == 2:
            S3.stop()
            board[S3.x_1, S3.y_1] = S3.color_1
            board[S3.x_2, S3.y_2] = S3.color_2
            board[S3.x_3, S3.y_3] = S3.color_3
            board[S3.x_4, S3.y_4] = S3.color_4
            if board[12, 28] != 0:
                for i in cars:
                    if i.x == 12 and i.y == 28:
                        if i.turn == "right":
                            stop_3 = s7 + 2
                        elif i.turn == "up" or i.turn == "down":
                            stop_3 = s7 + 3
                        else:
                            stop_3 = s7 + 4
                        break
            elif board[11, 28] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 28:
                        if i.turn == "right":
                            stop_3 = s7 + 1
                        elif i.turn == "up" or i.turn == "down":
                            stop_3 = s7 + 2
                        else:
                            stop_3 = s7 + 3
                        break
            elif board[10, 28] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 28:
                        if i.turn == "up":
                            stop_3 = s7 + 1
                        else:
                            stop_3 = s7 + 2
                        break
            elif board[11, 27] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 27:
                        stop_3 = s7 + 1
                        break
            elif board[10, 27] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 27:
                        stop_3 = s7 + 1
                        break
            else:
                stop_3 = s7
        elif s8 == t and S3.color_2 == 2:
            S3.stop()
            board[S3.x_1, S3.y_1] = S3.color_1
            board[S3.x_2, S3.y_2] = S3.color_2
            board[S3.x_3, S3.y_3] = S3.color_3
            board[S3.x_4, S3.y_4] = S3.color_4
            if board[10, 29] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 29:
                        if i.turn == "_right":
                            stop_3 = s8 + 2
                        elif i.turn == "_up" or i.turn == "_down":
                            stop_3 = s8 + 3
                        else:
                            stop_3 = s8 + 4
                        break
            elif board[10, 28] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 28:
                        if i.turn == "_right":
                            stop_3 = s8 + 1
                        elif i.turn == "_up" or i.turn == "_down":
                            stop_3 = s8 + 2
                        else:
                            stop_3 = s8 + 3
                        break
            elif board[10, 27] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 27:
                        if i.turn == "_up":
                            stop_3 = s8 + 1
                        elif i.turn == "_left":
                            stop_3 = s8 + 2
                        break
            elif board[11, 28] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 28:
                        stop_3 = s8 + 1
                        break
            elif board[11, 27] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 27:
                        stop_3 = s8 + 1
                        break
            else:
                stop_3 = s8
        elif s9 == t and S3.color_3 == 2:
            S3.stop()
            board[S3.x_1, S3.y_1] = S3.color_1
            board[S3.x_2, S3.y_2] = S3.color_2
            board[S3.x_3, S3.y_3] = S3.color_3
            board[S3.x_4, S3.y_4] = S3.color_4
            if board[9, 27] != 0:
                for i in cars:
                    if i.x == 9 and i.y == 27:
                        if i.turn == "__right":
                            stop_3 = s9 + 2
                        elif i.turn == "__up" or i.turn == "__down":
                            stop_3 = s9 + 3
                        else:
                            stop_3 = s9 + 4
                        break
            elif board[10, 27] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 27:
                        if i.turn == "__right":
                            stop_3 = s9 + 1
                        elif i.turn == "__up" or i.turn == "__down":
                            stop_3 = s9 + 2
                        else:
                            stop_3 = s9 + 3
                        break
            elif board[11, 27] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 27:
                        if i.turn == "__up":
                            stop_3 = s9 + 1
                        elif i.turn == "__left":
                            stop_3 = s9 + 2
                        break
            elif board[10, 28] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 28:
                        stop_3 = s9 + 1
                        break
            elif board[11, 28] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 28:
                        stop_3 = s9 + 1
                        break
            else:
                stop_3 = s9
        elif s10 == t and S3.color_4 == 2:
            S3.stop()
            board[S3.x_1, S3.y_1] = S3.color_1
            board[S3.x_2, S3.y_2] = S3.color_2
            board[S3.x_3, S3.y_3] = S3.color_3
            board[S3.x_4, S3.y_4] = S3.color_4
            if board[11, 10] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 10:
                        if i.turn == "___right":
                            stop_3 = s10 + 2
                        elif i.turn == "___up" or i.turn == "___down":
                            stop_3 = s10 + 3
                        else:
                            stop_3 = s10 + 4
                        break
            elif board[11, 11] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 11:
                        if i.turn == "___right":
                            stop_3 = s10 + 1
                        elif i.turn == "___up" or i.turn == "___down":
                            stop_3 = s10 + 2
                        else:
                            stop_3 = s10 + 3
                        break
            elif board[11, 12] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 12:
                        if i.turn == "___up":
                            stop_3 = s10 + 1
                        elif i.turn == "___left":
                            stop_3 = s10 + 2
                        break
            elif board[10, 11] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 11:
                        stop_3 = s10 + 1
                        break
            elif board[10, 12] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 12:
                        stop_3 = s10 + 1
                        break
            else:
                stop_3 = s10

        if s11 == t and S4.color_1 == 2:
            S4.stop()
            board[S4.x_1, S4.y_1] = S4.color_1
            board[S4.x_2, S4.y_2] = S4.color_2
            board[S4.x_3, S4.y_3] = S4.color_3
            if board[11, 35] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 35:
                        if i.turn == "up" or i.turn == "down":
                            stop_4 = s11 + 3
                        else:
                            stop_4 = s11 + 4
                        break
            elif board[11, 36] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 36:
                        if i.turn == "up" or i.turn == "down":
                            stop_4 = s11 + 2
                        else:
                            stop_4 = s11 + 3
                        break
            elif board[11, 37] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 37:
                        if i.turn == "up":
                            stop_4 = s11 + 1
                        else:
                            stop_4 = s11 + 2
                        break
            elif board[10, 36] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 36:
                        stop_4 = s11 + 1
                        break
            elif board[10, 37] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 37:
                        stop_4 = s11 + 1
                        break
            else:
                stop_4 = s11
        elif s12 == t and S4.color_2 == 2:
            S4.stop()
            board[S4.x_1, S4.y_1] = S4.color_1
            board[S4.x_2, S4.y_2] = S4.color_2
            board[S4.x_3, S4.y_3] = S4.color_3
            if board[9, 36] != 0:
                for i in cars:
                    if i.x == 9 and i.y == 36:
                        if i.turn == "_right":
                            stop_4 = s12 + 2
                        elif i.turn == "_down":
                            stop_4 = s12 + 3
                        else:
                            stop_4 = s12 + 4
                        break
            elif board[10, 36] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 36:
                        if i.turn == "_right":
                            stop_4 = s12 + 1
                        elif i.turn == "_down":
                            stop_4 = s12 + 2
                        else:
                            stop_4 = s12 + 3
                        break
            elif board[10, 37] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 37:
                        stop_4 = s12 + 1
                        break
            elif board[10, 36] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 37:
                        stop_4 = s12 + 2
                        break
            elif board[10, 37] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 37:
                        stop_4 = s12 + 1
                        break
            else:
                stop_4 = s12
        elif s11 == t and S4.color_3 == 2:
            S4.stop()
            board[S4.x_1, S4.y_1] = S4.color_1
            board[S4.x_2, S4.y_2] = S4.color_2
            board[S4.x_3, S4.y_3] = S4.color_3
            if board[10, 38] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 38:
                        if i.turn == "__right":
                            stop_4 = s13 + 2
                        else:
                            stop_4 = s13 + 3
                        break
            elif board[10, 37] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 37:
                        if i.turn == "__right":
                            stop_4 = s13 + 1
                        else:
                            stop_4 = s13 + 2
                        break
            elif board[10, 36] != 0:
                for i in cars:
                    if i.x == 10 and i.y == 36:
                        stop_4 = s13 + 1
                        break
            elif board[11, 37] != 0:
                for i in cars:
                    if i.x == 11 and i.y == 37:
                        stop_4 = s13 + 1
                        break
            else:
                stop_4 = s13
        if t == stop_1 and S1.sequence[0] == 2:
            S1.change_color()
            s1 = stop_1 + _s1
            s2 = stop_1 + _s1
            board[S1.x_1, S1.y_1] = S1.color_1
            board[S1.x_2, S1.y_2] = S1.color_2
        elif t == stop_1 and S1.sequence[1] == 2:
            S1.change_color()
            s1 = stop_1 + _s2
            s2 = stop_1 + _s1
            board[S1.x_1, S1.y_1] = S1.color_1
            board[S1.x_2, S1.y_2] = S1.color_2

        if t == stop_2 and S2.sequence[0] == 2:
            S2.change_color()
            s3 = stop_2 + _s3
            s4 = stop_2 + _s3
            s5 = stop_2 + _s3
            s6 = stop_2 + _s3
            board[S2.x_1, S2.y_1] = S2.color_1
            board[S2.x_2, S2.y_2] = S2.color_2
            board[S2.x_3, S2.y_3] = S2.color_3
            board[S2.x_4, S2.y_4] = S2.color_4
        elif t == stop_2 and S2.sequence[1] == 2:
            S2.change_color()
            s3 = stop_2 + _s4
            s4 = stop_2 + _s4
            s5 = stop_2 + _s4
            s6 = stop_2 + _s4
            board[S2.x_1, S2.y_1] = S2.color_1
            board[S2.x_2, S2.y_2] = S2.color_2
            board[S2.x_3, S2.y_3] = S2.color_3
            board[S2.x_4, S2.y_4] = S2.color_4
        elif t == stop_2 and S2.sequence[2] == 2:
            S2.change_color()
            s3 = stop_2 + _s5
            s4 = stop_2 + _s5
            s5 = stop_2 + _s5
            s6 = stop_2 + _s5
            board[S2.x_1, S2.y_1] = S2.color_1
            board[S2.x_2, S2.y_2] = S2.color_2
            board[S2.x_3, S2.y_3] = S2.color_3
            board[S2.x_4, S2.y_4] = S2.color_4
        elif t == stop_2 and S2.sequence[3] == 2:
            S2.change_color()
            s3 = stop_2 + _s6
            s4 = stop_2 + _s6
            s5 = stop_2 + _s6
            s6 = stop_2 + _s6
            board[S2.x_1, S2.y_1] = S2.color_1
            board[S2.x_2, S2.y_2] = S2.color_2
            board[S2.x_3, S2.y_3] = S2.color_3
            board[S2.x_4, S2.y_4] = S2.color_4

        if t == stop_3 and S3.sequence[0] == 2:
            S3.change_color()
            s7 = stop_3 + _s7
            s8 = stop_3 + _s7
            s9 = stop_3 + _s7
            s10 = stop_3 + _s7
            board[S3.x_1, S3.y_1] = S3.color_1
            board[S3.x_2, S3.y_2] = S3.color_2
            board[S3.x_3, S3.y_3] = S3.color_3
            board[S3.x_4, S3.y_4] = S3.color_4
        elif t == stop_3 and S3.sequence[1] == 2:
            S3.change_color()
            s7 = stop_3 + _s8
            s8 = stop_3 + _s8
            s9 = stop_3 + _s8
            s10 = stop_3 + _s8
            board[S3.x_1, S3.y_1] = S3.color_1
            board[S3.x_2, S3.y_2] = S3.color_2
            board[S3.x_3, S3.y_3] = S3.color_3
            board[S3.x_4, S3.y_4] = S3.color_4
        elif t == stop_3 and S3.sequence[2] == 2:
            S3.change_color()
            s7 = stop_3 + _s9
            s8 = stop_3 + _s9
            s9 = stop_3 + _s9
            s10 = stop_3 + _s9
            board[S3.x_1, S3.y_1] = S3.color_1
            board[S3.x_2, S3.y_2] = S3.color_2
            board[S3.x_3, S3.y_3] = S3.color_3
            board[S3.x_4, S3.y_4] = S3.color_4
        elif t == stop_3 and S3.sequence[3] == 2:
            S3.change_color()
            s7 = stop_3 + _s10
            s8 = stop_3 + _s10
            s9 = stop_3 + _s10
            s10 = stop_3 + _s10
            board[S3.x_1, S3.y_1] = S3.color_1
            board[S3.x_2, S3.y_2] = S3.color_2
            board[S3.x_3, S3.y_3] = S3.color_3
            board[S3.x_4, S3.y_4] = S3.color_4

        if t == stop_4 and S4.sequence[0] == 2:
            S4.change_color()
            s11 = stop_4 + _s11
            s12 = stop_4 + _s11
            s13 = stop_4 + _s11
            board[S4.x_1, S4.y_1] = S4.color_1
            board[S4.x_2, S4.y_2] = S4.color_2
            board[S4.x_3, S4.y_3] = S4.color_3
        elif t == stop_4 and S4.sequence[1] == 2:
            S4.change_color()
            s11 = stop_4 + _s12
            s12 = stop_4 + _s12
            s13 = stop_4 + _s12
            board[S4.x_1, S4.y_1] = S4.color_1
            board[S4.x_2, S4.y_2] = S4.color_2
            board[S4.x_3, S4.y_3] = S4.color_3
        elif t == stop_4 and S4.sequence[2] == 2:
            S4.change_color()
            s11 = stop_4 + _s13
            s12 = stop_4 + _s13
            s13 = stop_4 + _s13
            board[S4.x_1, S4.y_1] = S4.color_1
            board[S4.x_2, S4.y_2] = S4.color_2
            board[S4.x_3, S4.y_3] = S4.color_3

        for i in cars:
            board[i.x, i.y] = i.color

        if remaining_1:
            if board[remaining_1[-1].x, remaining_1[-1].y] == 0:
                car = remaining_1.pop()
                board[car.x, car.y] = car.color
                cars.append(car)
        if remaining_2:
            if board[remaining_2[-1].x, remaining_2[-1].y] == 0:
                car = remaining_2.pop()
                board[car.x, car.y] = car.color
                cars.append(car)
        if remaining_3:
            if board[remaining_3[-1].x, remaining_3[-1].y] == 0:
                car = remaining_3.pop()
                board[car.x, car.y] = car.color
                cars.append(car)
        if remaining_4:
            if board[remaining_4[-1].x, remaining_4[-1].y] == 0:
                car = remaining_4.pop()
                board[car.x, car.y] = car.color
                cars.append(car)
        if remaining_5:
            if board[remaining_5[-1].x, remaining_5[-1].y] == 0:
                car = remaining_5.pop()
                board[car.x, car.y] = car.color
                cars.append(car)
        if remaining_6:
            if board[remaining_6[-1].x, remaining_6[-1].y] == 0:
                car = remaining_6.pop()
                board[car.x, car.y] = car.color
                cars.append(car)
        if remaining_7:
            if board[remaining_7[-1].x, remaining_7[-1].y] == 0:
                car = remaining_7.pop()
                board[car.x, car.y] = car.color
                cars.append(car)
        for i in cars:
            i.time += 1
        cars_number.append(len(cars))
        remaining_cars_number.append(
            len(remaining_1) + len(remaining_2) + len(remaining_3) + len(remaining_4) + len(remaining_5) + len(
                remaining_6) + len(remaining_7))
    return cars_number, remaining_cars_number, times

if __name__ == "__main__":
    main(5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
