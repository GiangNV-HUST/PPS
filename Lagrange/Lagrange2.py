from Hoocner import Hoocner
import numpy as np


def TinhPi(HeSoW, x_i, y_i):
    Wx = Hoocner.TinhWx(HeSoW)
    WPhayX = Hoocner.DaoHamCuaDaThucTaiC(Wx, x_i)
    HeSoThuong = []
    HeSoThuong = Hoocner.ChiaDaThucChoXTruC(Wx, x_i)
    HeSoThuong.pop()
    Pi = np.array(HeSoThuong)*y_i/WPhayX
    return Pi


def TinhPn(HeSoW, X, Y):
    Pn = np.empty(len(HeSoW))
    for i in range(len(X)):
        Pi = TinhPi(HeSoW, X[i], Y[i])
        Pn += np.array(Pi)
    return Pn


if __name__ == "__main__":
    X = []
    Y = []

    with open(r"C:\Users\Giang\Desktop\PPS\Lagrange\input.txt", "r") as file:
        for line in file:
            data = line.strip().split(" ")
            X.append(float(data[0]))
            Y.append(float(data[1]))

    print(TinhPn(X, X, Y))
