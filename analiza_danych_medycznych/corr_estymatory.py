import scipy.special as ssp
import numpy as np
import scipy.stats as ss
import random as rnd
from numba import jit
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

g = lambda alfa, n: int(np.floor(n * alfa))


def L(X, t, alfa):
    Y = sorted(X)
    n = len(X)
    _g = g(alfa, n)
    if Y[_g] < X[t] and X[t] < Y[n - _g]:
        return 1
    return 0


def mean_X(X, alfa):
    suma1 = sum([L(X, i, alfa) for i in range(len(X))])
    suma2 = sum([X[i] * L(X, i, alfa) for i in range(len(X))])
    return 1 / suma1 * suma2


def cov2(X, Y, alfa):
    n = len(X)
    L_vector = [L(X, i, alfa) for i in range(n)]
    L2_vector = [L(Y, i, alfa) for i in range(n)]
    suma1 = sum(np.array(L_vector) * np.array(L2_vector))
    suma2 = sum(((np.array(X) - mean_X(X, alfa)) * (np.array(Y) - mean_X(Y, alfa))) * np.array(L_vector) * np.array(L2_vector))
    return suma2 / suma1


# def corr2(X, Y, alfa):
#     acvf = cov2(X, Y, alfa)
#     return [i / acvf for i in cov2(X, Y, alfa)]


def corr4(X, Y):
    X = np.array(X) - np.mean(X)
    Y = np.array(Y) - np.mean(Y)
    denominator = np.median([X[i] * Y[i] for i in range(len(X))])
    return np.median(X * Y) / denominator


def J(x):
    return ss.norm.ppf(x)


def c(X):
    n = len(X)
    R = sorted(X)
    return 1 / np.sum([(J((list(X).index(R[i]) + 1) / (n + 1))) ** 2 for i in range(n)])


def corr3(X, Y):
    n = len(X)
    R = sorted(X)
    R2 = sorted(Y)
    suma = sum([J((R.index(list(X)[i]) + 1) / (n + 1)) * J((R2.index(list(Y)[i]) + 1) / (n + 1)) for i in range(n)])
    return (c(X) * suma)

@jit(nopython=True)
def corr5(X, Y):
    n = len(X)
    suma = 0
    for i in range(n):
        for j in range(i):
            suma += np.sign((X[i] - X[j]) * (Y[i] - Y[j]))
    return 2/((n)*(n - 1))*suma


# def corr5(X, Y):
#     n = len(X)
#     return 1 / ((n * (n - 1)) * sum([np.sign((X[i] - X[j]) * (Y[i] - Y[j])) for i in range(n) for j in range(i)]))

def corr6(X, Y):
    n = len(X)
    medianaX = np.median(X)
    medianaY = np.median(Y)
    return 1 / n * sum([np.sign((X[i] - medianaX) * (Y[i] - medianaY)) for i in range(n)])

def corr8(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    return (np.var(Y + X) - np.var(Y - X)) / (np.var(Y + X) + np.var(Y - X))


def MAD2(X, const=1.4826):
    return (const * np.median([abs(i - np.median(X)) for i in X])) ** 2


def IQR2(X, const=0.7413):
    return (const * (np.quantile(X, 0.75) - np.quantile(X, 0.25))) ** 2


def corr9(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    return (MAD2(Y + X) - MAD2(Y - X)) / (MAD2(Y + X) + MAD2(Y - X))


def corr10(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    return (IQR2(Y + X) - IQR2(Y - X)) / (IQR2(Y + X) + IQR2(Y - X))


if __name__ == "__main__":
    df = pd.read_csv("macierz_korelacji.csv")
    df.drop("Unnamed: 0", axis=1, inplace=True)
    cols = df.columns
    print(len(df.columns))
    corr_matrix = np.zeros((len(df.columns), len(df.columns)))
    corr = df.corr()
    for i in df.columns:
        if i not in corr.columns:
            df.drop(i, axis=1, inplace=True)
    cols = df.columns
    print(len(df.columns))
    corr_matrix = np.zeros((len(df.columns), len(df.columns)))
    for i in range(len(df.columns)):
        print(i)
        #    if isinstance(df[str(i)], int) or isinstance(df[str(i)], float):
        #     print(df[i].values)
        for j in range(len(df.columns)):
            try:
                a=list(df[cols[i]].values)
                corr_matrix[i, j] = corr8(list(*df[cols[i]].values), list(*df[cols[j]].values))
            except:
                pass

