from Hoocner import Hoocner
import math
import numpy as np


def SAIPHANCAP1(Y):
    SaiPhanCap1 = np.zeros(len(Y)-1)
    for i in range(len(Y)-1):
        SaiPhanCap1[i] = Y[i+1] - Y[i]
    return SaiPhanCap1


def SAIPHANCAPN(Y):
    SaiPhanCap1 = SAIPHANCAP1(Y)
    SaiPhanCapN = np.zeros((len(Y)-1, len(Y)-1))
    SaiPhanCapN[0] = SaiPhanCap1
    for i in range(1, len(Y)-1):
        for j in range(len(Y)-i-1):
            SaiPhanCapN[i, j] = SaiPhanCapN[i-1, j+1] - SaiPhanCapN[i-1, j]
    return SaiPhanCapN


def HeSoGauss(Y):
    SaiPhanCapN = SAIPHANCAPN(Y)
    n = len(Y)
    heSoGauss = np.zeros(n)
    heSoGauss[0] = Y[math.ceil((n-1)/2)]
    for i in range(n-1):
        heSoGauss[i+1] = SaiPhanCapN[i, (len(SaiPhanCapN[i])-1-i)//2]
        # Hệ số gauss luôn nằm ở vị trí phần nguyên phía dưới của len(line-1)/2
    return heSoGauss


def HESODATHUC(Y):
    n = len(Y)
    heSoDaThuc = np.zeros(len(Y))
    T = [i for i in range(-(n-3)//2, (n+1)//2)]
    heSoGauss = HeSoGauss(Y)
    BangWx = np.zeros((len(Y), len(Y)))
    BangWx[0, len(Y)-1] = heSoGauss[0]
    for i in range(len(T)):
        line = Hoocner.TinhWx(T[len(T)//2-1-(i+1)//2:len(T)//2+(i)//2])
        for j in range(len(line)):
            BangWx[i+1, len(Y)+j-i-2] = line[j] * \
                heSoGauss[i+1]/math.factorial(i+1)
    for line in BangWx:
        heSoDaThuc += line
    return heSoDaThuc


def GiaTriDaThuc(Y, t):
    heSoDaThuc = HESODATHUC(Y)
    giaTriDaThuc = Hoocner.GiaTriCuaDaThucTaiC(heSoDaThuc, t)
    return giaTriDaThuc


if __name__ == "__main__":
    X = []
    Y = []
    with open(r"C:\Users\Giang\Desktop\PPS\NiuTon_MocBatKy\input.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            X.append(float(data[0]))
            Y.append(float(data[1]))

    x = 3.15
    t = (x-X[0])/(X[1]-X[0])
    # Hệ số Gauss được lưu theo thứ tự tăng dần [y_0, delta y_-1, delta^2 y_-1, delta^3 y_-2, delta^4 y_2]
    print(HeSoGauss(Y))

    # Đa thức được in ra màn hình với dạng a_n-1*t^n-1 +a_n-2*t^n-2 +...+ a_1*t + a_0
    print(HESODATHUC(Y))
    # print(GiaTriDaThuc(Y, 2))
    # print(heso)
