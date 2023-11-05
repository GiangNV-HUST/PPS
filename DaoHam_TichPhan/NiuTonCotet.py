import numpy
import sympy
from Hoocner import Hoocner

x = sympy.symbols("x")


def BangNoiSuy(f, a, b, n):
    bangNoiSuy = numpy.zeros((n+1, 2))
    h = (b-a) / n
    bangNoiSuy[0][0] = a
    for i in range(0, n):
        bangNoiSuy[i+1][0] = bangNoiSuy[i][0] + h
    for i in range(0, n+1):
        bangNoiSuy[i][1] = f.subs(x, bangNoiSuy[i][0])
    return bangNoiSuy


def HeSoCoTet(m):
    HeSoW = [i for i in range(m+1)]
    HeSoT = Hoocner.TinhWx(HeSoW)
    heSoCoTet = []
    for i in range(m+1):
        _kq = 0
        T_tru_j = numpy.array(Hoocner.ChiaDaThucChoXTruCKhongCoDu(HeSoT, i))
        Hi = T_tru_j/Hoocner.GiaTriCuaDaThucTaiC(T_tru_j, i)
        for j in range(len(Hi)):
            _kq += Hi[j]*(len(Hi)-1)**(len(Hi)-j)/(len(Hi)-j)
        heSoCoTet.append(_kq)
    return heSoCoTet


def TinhI(X, Y,m):
    N = int((len(X)-1)/m)
    I = 0
    Hi = HeSoCoTet(m)
    h = X[1] - X[0]
    for i in range(N):
        for j in range(m+1):
            I += h*(Y[m*i+j])*Hi[j]
    return I



if __name__ == "__main__":
    print("SỬ DỤNG PHƯƠNG PHÁP SIMSON TÍNH GẦN ĐÚNG TÍCH PHÂN!")
    X = []
    Y = []
    # n là số đoạn của bảng sai phân hay độ dài tập X-1
    n = 10
    # m là hệ số cotet
    m = 10
    f = 1/(1+x)
    a = 0
    b = 1
    print(f"Tích phân của hàm f= {f} trên đoạn [{a},{b}] là")
    bangNoiSuy = BangNoiSuy(f, a, b, n)
    print(f"Bảng nội suy tương ứng với n = {n} là:")
    print(bangNoiSuy)
    for i in range(n+1):
        X.append(bangNoiSuy[i][0])
        Y.append(bangNoiSuy[i][1])

    # print("Giá trị của I là:", TinhI(X, Y))
    print(HeSoCoTet(m))
    print(TinhI(X,Y,m))
