from Hoocner import Hoocner
import numpy as np


def TinhLj(HeSoW, x_j):
    Wx = Hoocner.TinhWx(HeSoW)
    HeSoThuong = Hoocner.ChiaDaThucChoXTruC(Wx, x_j)
    HeSoThuong.pop()
    L_j = np.array(HeSoThuong)/Hoocner.DaoHamCuaDaThucTaiC(Wx, x_j)
    return L_j


def TinhPn(HeSoW, X, Y):
    Pn = np.empty(len(X))
    for i in range(len(X)):
        Pn += np.array(TinhLj(HeSoW, X[i])*Y[i])
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
