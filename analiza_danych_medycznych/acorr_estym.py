import scipy.special as ssp
import numpy as np
import scipy.stats as ss
import random as rnd

Zt = lambda p, zt, n: np.array(
    [0 if i > 2 * p else (zt if i < p else -zt) for i in (rnd.random() for i in range(n))])  # szum dyskretny

auto2cov = lambda X, Y, lag: [
    1 / len(X) * (np.sum((np.array(X[:len(X) - i]) - np.mean(X)) * (np.array(Y[i:]) - np.mean(Y)))) if i >= 0 else
    1 / len(X) * (np.sum((np.array(X[-i:]) - np.mean(X)) * (np.array(Y[:i]) - np.mean(Y)))) for i in
    range(lag[0], lag[1] + 1)]  # klasyczna autokowariancja

auto2corr = lambda X,Y, lag: [i / auto2cov(X, Y, [0, 1])[0] for i in auto2cov(X, Y, lag)]  # klasyczna autokorelacja

pearson = lambda X,Y, lag: [i / (np.sqrt(np.sum((np.array(X) - np.mean(X))**2)) * np.sqrt(np.sum((np.array(Y) - np.mean(Y))**2))) for i in auto2cov(X, Y, lag)]

def Q(X, k):
    values = [abs(X[j] - X[i]) for i in range(len(X)) for j in range(i)]
    values = sorted(values)
    return k * values[int(np.floor((ssp.binom(len(X), 2) + 2) / 4))]

def auto2cov1(X, Y, lag, k):
    acvf = []
    for h in range(lag[0], lag[1] + 1):
        if h == 0:
            u = np.array(X)
        else:
            u = np.array(X[:-h])
        v = np.array(Y[h:])
        acvf.append(1 / 4 * ((Q(u + v, k)) ** 2 - (Q(u - v, k)) ** 2))
    return acvf

def auto2corr1(X, Y, lag, k):
    acf = []
    for h in range(lag[0], lag[1] + 1):
        if h == 0:
            u = np.array(X)
            v = np.array(Y[h:])
        elif h < 0:
            u = np.array(X[-h:])
            v = np.array(Y[:h])
        else:
            u = np.array(X[:-h])
            v = np.array(Y[h:])
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

def auto2cov2(X, Y, lag, alfa):
    n = len(X)
    L_vector = [L(X, i, alfa) for i in range(n)]
    L2_vector = [L(Y, i, alfa) for i in range(n)]
    acvf = []
    for h in range(lag[0], lag[1] + 1):
        if h == 0:
            suma1 = sum(np.array(L_vector) * np.array(L2_vector))
            suma2 = sum(np.array(X) * np.array(L_vector) * np.array(Y) ** 2 * np.array(L2_vector))
        elif h < 0:
            suma1 = sum(np.array(L_vector[-h:]) * np.array(L2_vector[:h]))
            suma2 = sum(np.array(X[-h:] - mean_X(X, alfa)) * np.array(Y[:h] - mean_X(Y, alfa)) * np.array(
                L_vector[-h:]) * np.array(L2_vector[:h]))
        else:
            suma1 = sum(np.array(L_vector[:-h]) * np.array(L2_vector[h:]))
            suma2 = sum(np.array(X[:-h] - mean_X(X, alfa)) * np.array(Y[h:] - mean_X(Y, alfa)) * np.array(
                L_vector[:-h]) * np.array(L2_vector[h:]))
        acvf.append(suma2 / suma1)
    return acvf

def auto2corr2(X, Y, lag, alfa):
    acvf = auto2cov2(X, Y, lag, alfa)[0]
    return [i / acvf for i in auto2cov2(X, Y, lag, alfa)]

def auto2corr4(X, Y, lag):
    X = np.array(X) - np.mean(X)
    Y = np.array(Y) - np.mean(Y)
    acf = []
    denominator = np.median([X[i] * Y[i] for i in range(len(X))])
    for h in range(lag[0], lag[1] + 1):
        if h < 0:
            acf.append(np.median(np.array(X[-h:]) * np.array(Y[:h]))/denominator)
        elif h == 0:
            acf.append(np.median(np.array(X[:]) * np.array(Y[:]))/denominator)
        else:
            acf.append(np.median(np.array(X[:-h]) * np.array(Y[h:]))/denominator)
    return acf

def J(x):
    return ss.norm.ppf(x)

def c(X):
    n = len(X)
    R = sorted(X)
    return 1 / np.sum([(J((list(X).index(R[i]) + 1) / (n + 1)))**2 for i in range(n)])

def auto2corr3(X, Y, lag):
    acf = []
    n = len(X)
    R = sorted(X)
    R2 = sorted(Y)
    for h in range(lag[0], lag[1] + 1):
        suma = 0
        for i in range(n-abs(h)):
            suma += J((R.index(list(X)[i if h >= 0 else i - h]) + 1)/(n+1)) * J((R2.index(list(Y)[i + h if h >= 0 else i]) + 1)/ (n+1))
        acf.append(c(X) * suma)
    return acf

def auto2corr5(X, Y, lag):
    n = len(X)
    acf = []
    for h in range(lag[0], lag[1] + 1):
        if h >= 0:
            acf.append(2/((n - h)*(n - h - 1)) * np.sum([np.sign((X[i] - X[j]) * (Y[i + h] - Y[j + h]))
                                                  for i in range(n - h) for j in range(i)]))
        else:
            acf.append(2/((n + h)*(n + h - 1)) * np.sum([np.sign((X[i - h] - X[j - h]) * (Y[i] - Y[j]))
                                                         for i in range(n + h) for j in range(i)]))
    return acf

def auto2corr6(X, Y, lag):
    n = len(X)
    mediana = np.median(X)
    mediana2 =  np.median(Y)
    acf = []
    for h in range(lag[0], lag[1] + 1):
        if h >= 0:
            acf.append(1/(n - h) * np.sum(np.sign((np.array(X[:-h] if h > 0 else np.array(X)) - mediana) *
                                              (np.array(Y[h:]) - mediana2))))
        else:
            acf.append(1/(n - h) * np.sum(np.sign((np.array(X[-h:]) - mediana) *
                                                  (np.array(Y[:h]) - mediana2))))

    return acf

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

def auto2corr8(X, Y, lag):
    X = np.array(X)
    Y = np.array(Y)
    return [(np.var(Y+X) - np.var(Y - X))/(np.var(Y+X) + np.var(Y - X)) if h == 0 else
            (np.var(Y[:h]+X[-h:]) - np.var(Y[:h] - X[-h:]))/(np.var(Y[:h]+X[-h:]) + np.var(Y[:h] - X[-h:])) if h < 0 else
            (np.var(Y[h:]+X[:-h]) - np.var(Y[h:] - X[:-h]))/(np.var(Y[h:]+X[:-h]) + np.var(Y[h:] - X[:-h]))
            for h in range(lag[0], lag[1] + 1)]

def MAD2(X, const=1.4826):
    return (const * np.median([abs(i - np.median(X)) for i in X]))**2

def IQR2(X, const=0.7413):
    return (const * (np.quantile(X, 0.75) - np.quantile(X, 0.25)))**2

def auto2corr9(X, Y, lag):
    X = np.array(X)
    Y = np.array(Y)
    return [(MAD2(Y+X) - MAD2(Y - X))/(MAD2(Y+X) + MAD2(Y - X)) if h == 0 else
            (MAD2(Y[:h]+X[-h:]) - MAD2(Y[:h] - X[-h:]))/(MAD2(Y[:h]+X[-h:]) + MAD2(Y[:h] - X[-h:])) if h < 0 else
            (MAD2(Y[h:]+X[:-h]) - MAD2(Y[h:] - X[:-h]))/(MAD2(Y[h:]+X[:-h]) + MAD2(Y[h:] - X[:-h]))
            for h in range(lag[0], lag[1] + 1)]

def auto2corr10(X, Y, lag):
    X = np.array(X)
    Y = np.array(Y)
    return [(IQR2(Y+X) - IQR2(Y - X))/(IQR2(Y+X) + IQR2(Y - X)) if h == 0 else
            (IQR2(Y[:h]+X[-h:]) - IQR2(Y[:h] - X[-h:]))/(IQR2(Y[:h]+X[-h:]) + IQR2(Y[:h] - X[-h:])) if h < 0 else
            (IQR2(Y[h:]+X[:-h]) - IQR2(Y[h:] - X[:-h]))/(IQR2(Y[h:]+X[:-h]) + IQR2(Y[h:] - X[:-h]))
            for h in range(lag[0], lag[1] + 1)]