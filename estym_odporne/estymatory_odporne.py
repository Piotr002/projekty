import scipy.special as ssp
import numpy as np
import scipy.stats as ss
import random as rnd

Zt = lambda p, zt, n: np.array(
    [0 if i > 2 * p else (zt if i < p else -zt) for i in (rnd.random() for i in range(n))])  # szum dyskretny

autocov = lambda X, lag: [
    1 / len(X) * (np.sum((np.array(X[:len(X) - i]) - np.mean(X)) * (np.array(X[i:]) - np.mean(X)))) for i in
    range(lag[0], lag[1] + 1)]  # klasyczna autokowariancja

autocorr = lambda X, lag: [i / autocov(X, [0, 1])[0] for i in autocov(X, lag)]  # klasyczna autokorelacja

def Q(X, k):
    values = [abs(X[j] - X[i]) for i in range(len(X)) for j in range(i)]
    values = sorted(values)
    return k * values[int(np.floor((ssp.binom(len(X), 2) + 2) / 4))]

def autocov1(X, lag, k):
    acvf = []
    for h in range(lag[0], lag[1] + 1):
        if h == 0:
            u = np.array(X)
        else:
            u = np.array(X[:-h])
        v = np.array(X[h:])
        acvf.append(1 / 4 * ((Q(u + v, k)) ** 2 - (Q(u - v, k)) ** 2))
    return acvf

def autocorr1(X, lag, k):
    acf = []
    for h in range(lag[0], lag[1] + 1):
        if h == 0:
            u = np.array(X)
        else:
            u = np.array(X[:-h])
        v = np.array(X[h:])
        acf.append(((Q(u + v, k)) ** 2 - (Q(u - v, k)) ** 2) / ((Q(u + v, k)) ** 2 + (Q(u - v, k)) ** 2))
    return acf

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

def autocov2(X, lag, alfa):
    n = len(X)
    L_vector = [L(X, i, alfa) for i in range(n)]
    acvf = []
    for h in range(lag[0], lag[1] + 1):
        if h == 0:
            suma1 = sum(L_vector)
            suma2 = sum(np.array(X) ** 2 * np.array(L_vector))
        else:
            suma1 = sum(np.array(L_vector[:-h]) * np.array(L_vector[h:]))
            suma2 = sum(np.array(X[:-h] - mean_X(X, alfa)) * np.array(X[h:] - mean_X(X, alfa)) * np.array(
                L_vector[:-h]) * np.array(L_vector[h:]))
        acvf.append(suma2 / suma1)
    return acvf

def autocorr2(X, lag, alfa):
    acvf = autocov2(X, lag, alfa)[0]
    return [i / acvf for i in autocov2(X, lag, alfa)]

def autocorr4(X, lag):
    X = np.array(X) - np.mean(X)
    acf = [1.0]
    denominator = np.median([i**2 for i in X])
    for h in range(lag[0] + 1, lag[1] + 1):
        acf.append(np.median(np.array(X[:-h]) * np.array(X[h:]))/denominator)
    return acf

def J(x):
    return ss.norm.ppf(x)

def c(X):
    n = len(X)
    R = sorted(X)
    return 1 / np.sum([(J((list(X).index(R[i]) + 1) / (n + 1)))**2 for i in range(n)])

def autocorr3(X, lag):
    acf = []
    n = len(X)
    R = sorted(X)
    for h in range(lag[0], lag[1] + 1):
        suma = 0
        for i in range(n-h):
            suma += J((R.index(list(X)[i]) + 1)/(n+1)) * J((R.index(list(X)[i + h]) + 1)/ (n+1))
        acf.append(c(X) * suma)
    return acf

def autocorr5(X, lag):
    n = len(X)
    return [2/((n - h)*(n - h - 1)) * np.sum([np.sign((X[i] - X[j]) * (X[i + h] - X[j + h]))
                                              for i in range(n - h) for j in range(i)]) for h in range(lag[0], lag[1] + 1)]

def autocorr6(X, lag):
    n = len(X)
    mediana = np.median(X)
    acf = [1/(n - h) * np.sum(np.sign((np.array(X[:-h]) - mediana) *
                                      (np.array(X[h:]) - mediana))) for h in range(lag[0] + 1, lag[1] + 1)]
    return [1, *acf]

def zmatrix(X, k):
    n = len(X)
    # Zk = np.zeros((k + 1, n + k))
    # for j in range(k + 1):
    #     Zk[j, j:j + n - 1] = X
    # return Zk
    return np.matrix([[*[0 for i in range(j)], *[X[i] for i in range(n)], *[0 for i in range(k - j)]] for j in range(k+1)])

def gamma_k(X, k):
    z_matr = zmatrix(X, k)
    return (z_matr * z_matr.transpose())/len(X)

def Xi(X, k, i, j):
    gamm = gamma_k(X, k)
    return gamm[i - 1, j - 1]/np.sqrt(gamm[i - 1, i - 1] * gamm[j - 1, j - 1])

def autocorr7(X, lag):
    k = lag[1]
    return [1/(k - h + 1)*sum([Xi(X, k, i, i + h) for i in range(1, k - h + 2)]) for h in range(lag[0], lag[1] + 1)]

def autocorr8(X, lag):
    X = np.array(X)
    return [(np.var(X+X) - np.var(X - X))/(np.var(X+X) + np.var(X - X)) if h == 0 else
            (np.var(X[h:]+X[:-h]) - np.var(X[h:] - X[:-h]))/(np.var(X[h:]+X[:-h]) + np.var(X[h:] - X[:-h]))
            for h in range(lag[0], lag[1] + 1)]

def MAD2(X, const=1.4826):
    return (const * np.median([abs(i - np.median(X)) for i in X]))**2

def IQR2(X, const=0.7413):
    return (const * (np.quantile(X, 0.75) - np.quantile(X, 0.25)))**2

def autocorr9(X, lag):
    X = np.array(X)
    return [(MAD2(X+X) - MAD2(X - X))/(MAD2(X+X) + MAD2(X - X)) if h == 0 else
            (MAD2(X[h:]+X[:-h]) - MAD2(X[h:] - X[:-h]))/(MAD2(X[h:]+X[:-h]) + MAD2(X[h:] - X[:-h]))
            for h in range(lag[0], lag[1] + 1)]

def autocorr10(X, lag):
    X = np.array(X)
    return [(IQR2(X+X) - IQR2(X - X))/(IQR2(X+X) + IQR2(X - X)) if h == 0 else
            (IQR2(X[h:]+X[:-h]) - IQR2(X[h:] - X[:-h]))/(IQR2(X[h:]+X[:-h]) + IQR2(X[h:] - X[:-h]))
            for h in range(lag[0], lag[1] + 1)]