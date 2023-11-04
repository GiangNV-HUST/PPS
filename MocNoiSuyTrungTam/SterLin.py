import math
import numpy as np
from Hoocner import Hoocner


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


def HeSoSterLin(Y):
    SaiPhanCapN = SAIPHANCAPN(Y)
    n = len(Y)
    heSoSterLin = np.zeros(n)
    heSoSterLin[0] = Y[math.ceil((n-1)/2)]
    for i in range(n-1):
        heSoSterLin[i+1] = (SaiPhanCapN[i, math.ceil((len(SaiPhanCapN[i])-1-i)/2)] +
                            SaiPhanCapN[i, ((len(SaiPhanCapN[i])-1-i)//2)])/2
        # Hệ số sterlin bằng sai phân của 2 vị trí 
    return heSoSterLin


def HeSoDaThuc(Y):
    n =len(Y)
    heSoDaThuc = np.zeros(len(Y))
    T = [i for i in range(-(n-3)//2, (n+1)//2)]
    HeSoSterLin = HeSoSterLin(Y)
    BangWx = np.zeros((len(Y), len(Y)))
    BangWx[0, len(Y)-1] = HeSoSterLin[0]
    for i in range()

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

    print(SAIPHANCAPN(Y))
    print(HeSoSterLin(Y))
    # print(heso)
