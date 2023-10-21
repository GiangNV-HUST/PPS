import math
import numpy as np
import sys
sys.path.insert(0, r"C:\Users\Giang\Desktop\PPS\Hoocner")
from Hoocner import Hoocner


def SAIPHANCAP1(Y):
    SaiPhanCap1 = np.zeros(len(Y)-1)
    for i in range(len(Y)-1):
        SaiPhanCap1[i] = Y[i+1] - Y[i]
    return SaiPhanCap1


def KhoangLiNghiem(yNgang, Y):
    khoangLiNghiem = []
    for i in range(len(Y)-1):
        if ((Y[i] - yNgang)*(Y[i+1]-yNgang) < 0):
            khoangLiNghiem.append((Y[i], Y[i+1]))
    return khoangLiNghiem


def KhoangDonDieuY(Y):
    SaiPhanCap1 = SAIPHANCAP1(Y)
    khoangDonDieuY = []
    temp = SaiPhanCap1[0]
    index = []
    index.append(0)
    for i in range(1, len(SaiPhanCap1)):
        if (temp*SaiPhanCap1[i]) < 0:
            temp = SaiPhanCap1[i]
            index.append(i)
    index.append(len(SaiPhanCap1))
    khoangDonDieuY = []
    doDaiMax = index[1] - index[0]
    for i in range(len(index)-1):
        if (doDaiMax <= (index[i+1] - index[i])):
            doDaiMax = index[i+1] - index[i]
            for j in range(index[i], index[i+1]+1):
                khoangDonDieuY.append(Y[j])
    return khoangDonDieuY


def KhoangDonDieuX(X, Y):
    XDonDieu = []
    khoangDonDieuY = KhoangDonDieuY(Y)
    for i in range(len(Y)):
        if (Y[i] == khoangDonDieuY[0]):
            index = i
            for j in range(index, len(khoangDonDieuY)+index):
                XDonDieu.append(X[j])
    return XDonDieu


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
        HeSoNiuTon[i] = TiSaiPhanCapN[i-1, 0]
    return HeSoNiuTon


def HESODATHUC(X, HeSoNiuTon):
    BangWx = np.zeros((len(X), len(X)))
    n = len(X)
    BangWx[0, n-1] = HeSoNiuTon[0]
    HeSoDaThuc = np.zeros(len(X))
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
        GiaTriHam += HeSoDaThuc[len(HeSoDaThuc)-i-1] * x**i
    return GiaTriHam


if __name__ == "__main__":
    X = []
    Y = []
    with open(r"C:\Users\Giang\Desktop\PPS\NiuTon_MocBatKy\input.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            X.append(float(data[0]))
            Y.append(float(data[1]))

    # heSoNiuTon = NiuTon_Tien.HESONIUTON(KhoangDonDieuY(Y),)
    # print(SAIPHANCAP1(Y))
    khoangDonDieuY = KhoangDonDieuY(Y)
    print(khoangDonDieuY)
    khoangDonDieuX = KhoangDonDieuX(X, Y)
    hESONIUTON = HESONIUTON(khoangDonDieuY, khoangDonDieuX)
    heSoDaThuc = HESODATHUC(khoangDonDieuY, hESONIUTON)
    print(heSoDaThuc)
    print(GIATRIHAMSOTAIX(heSoDaThuc, 3.15))
    # print(KhoangLiNghiem(4,Y))
    # print(HamNguoc(Y))
