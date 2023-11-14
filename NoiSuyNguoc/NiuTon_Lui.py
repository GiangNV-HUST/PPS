import numpy as np
from Hoocner import Hoocner


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
    X.reverse()
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
        GiaTriHam += HeSoDaThuc[len(HeSoDaThuc)-1-i] * x**(i)
        # print(i)
        # print(len(HeSoDaThuc)-1-i)
    return GiaTriHam


if __name__ == "__main__":
    X = []
    Y = []
    with open(r"C:\Users\Giang\Desktop\PPS\NiuTon_MocBatKy\input.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            X.append(float(data[0]))
            Y.append(float(data[1]))

    TiSaiPhanCapN = TISAIPHANCAPN(X, Y)
    # Bảng tỉ sai phân có các hàng tương ứng với6 các cấp
    print("Bảng tỉ sai phân cấp n của đa thức:\n", TiSaiPhanCapN)

    HeSoNiuTon = HESONIUTON(X, Y)
    # Hệ số tỉ sai phân bắt đầu từ cấp 0 đến n
    print("Hệ số NiuTon của đa thức\n", HeSoNiuTon)

    # Đa thức có dạng F(x) =  a_n*x^n+ ...+ a_0*x^0
    HeSoDaThuc = HESODATHUC(X, HeSoNiuTon)
    print("Hệ số của đa thức là: \n", HeSoDaThuc)

    x = 4.27
    print(f"Giá trị của hàm số tại x = {x} là: ",
          GIATRIHAMSOTAIX(HeSoDaThuc, x))
