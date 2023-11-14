import numpy as np
import math
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


def HESOSAIPHAN(Y):
    HeSoSaiPhan = np.zeros(len(Y))
    HeSoSaiPhan[0] = Y[0]
    SaiPhanCapN = SAIPHANCAPN(Y)
    for i in range(1, len(Y)):
        HeSoSaiPhan[i] = SaiPhanCapN[i-1, 0]
    return HeSoSaiPhan


def HESODATHUC(Y):
    HeSoSaiPhan = HESOSAIPHAN(Y)
    n = len(HeSoSaiPhan)
    HeSoDaThuc = np.zeros(n)
    X = [i for i in range(0, n)]
    HeSoWx = np.zeros((n, n))
    HeSoWx[0, n-1] = HeSoSaiPhan[0]
    for i in range(1, n):
        line = Hoocner.TinhWx(X[0:i])
        for j in range(len(line)):
            HeSoWx[i, n+j-i-1] = line[j] / math.factorial(i) * HeSoSaiPhan[i]
    print(HeSoWx)
    for line in HeSoWx:
        HeSoDaThuc += line
    return HeSoDaThuc


def GIATRIHAMSO(t, Y):
    GiaTriHam = 0
    HeSoDaThuc = HESODATHUC(Y)
    for i in range(len(HeSoDaThuc)):
        GiaTriHam += HeSoDaThuc[i] * t**(len(HeSoDaThuc)-i-1)
    return GiaTriHam


if __name__ == "__main__":
    X = []
    Y = []
    with open(r"C:\Users\Giang\Desktop\PPS\NiuTon_MocBatKy\input.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            X.append(float(data[0]))
            Y.append(float(data[1]))

    # Bảng sai phân có các hàng tương ứng với các cấp
    SaiPhanCapN = SAIPHANCAPN(Y)
    print("Bảng sai phân cấp n của đa thức:\n",SaiPhanCapN)

    # Hệ số sai phân bắt đầu từ cấp 0 đến n
    HeSoSaiPhan = HESOSAIPHAN(Y)
    print("Hệ số sai phân:\n", HeSoSaiPhan)

    # Đa thức NiuTon có dạng a_n*t^n + a_n-1*t^n-1 +... + a_0
    HeSoDaThuc = HESODATHUC(Y)
    print("Hệ số đa thức Niuton mốc cách đều:\n", HeSoDaThuc)


    x = 4.27
    t = (x-X[0])/(X[1]-X[0])
    GiaTriHamSo =GIATRIHAMSO(t, Y)
    print("Giá trị biểu thức tại:\n", GiaTriHamSo)
