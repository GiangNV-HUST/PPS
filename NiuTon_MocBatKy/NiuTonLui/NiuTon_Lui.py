import numpy as np
import Hoocner


def TISAIPHANCAP1(X, Y):
    TiSaiPhanCap1 = np.zeros(len(X)-1)
    for i in range(1, len(X)):
        TiSaiPhanCap1[i-1] = (Y[i]-Y[i-1])/(X[i] - X[i-1])
    return TiSaiPhanCap1


def TISAIPHANCAPN(X, Y):
    n = len(X) - 1
    TiSaiPhanCap1 = TISAIPHANCAP1(X, Y)
    BangSaiPhan = np.zeros((n, n))
    BangSaiPhan[0, :] = TiSaiPhanCap1
    for i in range(1, n):
        for j in range(1, n-i+1):
            BangSaiPhan[i, j-1] = (BangSaiPhan[i-1, j] -
                                   BangSaiPhan[i-1, j-1])/(X[j+i]-X[j-1])
    return BangSaiPhan


def HESONIUTON(X, Y):
    HeSoNiuTon = np.zeros(len(X))
    TiSaiPhanCapN = TISAIPHANCAPN(X, Y)
    HeSoNiuTon[0] = Y[len(Y)-1]
    n = len(X)
    for i in range(1, n):
        HeSoNiuTon[i] = TiSaiPhanCapN[i-1, n-i-1]
    return HeSoNiuTon


def HESODATHUC(X, HeSoNiuTon):
    n = len(X)
    BangWx = np.zeros((len(X), len(X)))
    BangWx[0, n-1] = HeSoNiuTon[0]
    HeSoDaThuc = np.zeros(len(X))
    X.reverse()
    for i in range(1, len(X)):
        line = HeSoNiuTon[i]*np.array(Hoocner.TinhWx(X[0:i]))
        line = line[::-1]
        for j in range(len(X)-1, len(X) - len(line)-1, -1):
            BangWx[i, j] = line[len(X)-j-1]
    for line in BangWx:
        HeSoDaThuc += np.array(line)
    return HeSoDaThuc


def GIATRIHAMSOTAIX(HeSoDaThuc, x):
    GiaTriHam = 0
    for i in range(len(HeSoDaThuc)-1, -1, -1):
        GiaTriHam += HeSoDaThuc[len(HeSoDaThuc)-1-i] * x**i
    return GiaTriHam


