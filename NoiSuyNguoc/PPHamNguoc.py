import math
import numpy as np
import sys
sys.path.insert(0, r"C:\Users\Giang\Desktop\PPS\Hoocner")
from Hoocner import Hoocner
sys.path.append(r"C:\Users\Giang\Desktop\PPS\NiuTon_MocBatKy")
from NiuTon_MocBatKy import NiuTon_Tien


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


def KhoangDonDieu(Y):
    SaiPhanCap1 = SAIPHANCAP1(Y)
    khoangDonDieu = []
    temp = SaiPhanCap1[0]
    index = []
    index.append(0)
    for i in range(1, len(SaiPhanCap1)):
        if (temp*SaiPhanCap1[i]) < 0:
            temp = SaiPhanCap1[i]
            index.append(i)
    index.append(len(SaiPhanCap1))
    doDaiMax = index[1] - index[0]
    for i in range(len(index)-1):
        if (doDaiMax < (index[i+1] - index[i])):
            doDaiMax = index[i+1] - index[i]
            for j in range(index[i], index[i+1]+1):
                khoangDonDieu.append(Y[j])

    return khoangDonDieu

def HamNguoc(Y):
    pass



if __name__ == "__main__":
    X = []
    Y = []
    with open(r"C:\Users\Giang\Desktop\PPS\NiuTon_MocBatKy\input.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            X.append(float(data[0]))
            Y.append(float(data[1]))

    
    heSoNiuTon = NiuTon_Tien.HESONIUTON(KhoangDonDieu(Y),)
    # print(SAIPHANCAP1(Y))
    print(KhoangDonDieu(Y))
    # print(KhoangLiNghiem(4,Y))
    # print(HamNguoc(Y))
