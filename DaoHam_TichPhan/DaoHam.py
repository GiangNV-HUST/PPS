import Lagrange1
import Hoocner
import Lagrange2
import numpy
import math
from Hoocner import Hoocner


def TinhPn(X, Y):
    n = len(X)
    HeSoW = numpy.array([i for i in range(n)])
    p_n = numpy.zeros(n)
    Wt = Hoocner.TinhWx(HeSoW)

    for i in range(n):
        Thuong = Hoocner.ChiaDaThucChoXTruC(Wt, HeSoW[i])
        SoDu = Thuong.pop()
        p_n += (-1)**(n-1-i)/(math.factorial(i) *
                              math.factorial(n-1-i)) * numpy.array(Thuong)*Y[i]
    return p_n


def DaoHamPnTaix(X, Y, x):
    t = (x - X[0])/(X[1] - X[0])
    HeSoPn = TinhPn(X, Y)
    PnPhay = Hoocner.DaoHamCuaDaThucTaiC(HeSoPn, t)
    return PnPhay/(X[1]-X[0])


if __name__ == "__main__":
    X = []
    Y = []

    with open(r"C:\Users\Giang\Desktop\PPS\Lagrange\input.txt", "r") as file:
        for line in file:
            data = line.strip().split(" ")
            X.append(float(data[0]))
            Y.append(float(data[1]))

    # print(TinhPn(X, Y, X[1]))
    print(DaoHamPnTaix(X, Y, X[3]))
