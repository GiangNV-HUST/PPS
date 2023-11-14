import Hoocner
import numpy
import sympy

t = sympy.Symbol('t', real=True)
x = sympy.Symbol('x', real=True)


def BangNoiSuy(f, X):
    bangNoiSuy = numpy.zeros((len(X), 2))
    for i in range(len(X)):
        bangNoiSuy[i][1] = f.subs(x, X[i])
        bangNoiSuy[i][0] = X[i]
    return bangNoiSuy


def TinhPt(X, Y):
    n = len(X)
    h = X[1]-X[0]
    HeSoW = [i for i in range(n)]
    Pt = numpy.zeros(n)
    DaThuc = Hoocner.TinhWx(HeSoW)
    for i in range(n):
        arr = Hoocner.ChiaDaThucChoXTruCKhongCoDu(DaThuc, i)
        Pt += numpy.array(arr)/Hoocner.GiaTriCuaDaThucTaiC(arr, i)*Y[i]

    return Pt


def DaoHamPt(X, Y, c):
    t = (c-X[0])/(X[1]-X[0])
    Pt = TinhPt(X, Y)
    DaoHam = 0
    for i in range(len(Pt)-1):
        DaoHam += Pt[i]*t**(len(Pt)-1-i)/(X[1]-X[0])*(len(Pt)-1-i)
    return DaoHam


if __name__ == "__main__":
    #! Đọc từ fire input
    X = []
    Y = []

    with open("inputDaoHam.txt", "r") as file:
        for line in file:
            data = line.strip().split(" ")
            X.append(float(data[0]))
            Y.append(float(data[1]))
    
    bangNoiSuy = numpy.zeros((len(X),2))
    for i in range(len(X)):
        bangNoiSuy[i][0] = X[i]
        bangNoiSuy[i][1] = Y[i]
    print(bangNoiSuy)

    # !Đọc từ hàm 
    # X = [50, 55, 60, 65]
    # Y = []

    # f = sympy.log(x, 10)
    # bangNoiSuy = BangNoiSuy(f, X)
    # for i in range(len(X)):
    #     Y.append(bangNoiSuy[i][1])
    # print(BangNoiSuy(f, X))


    c = X[1]
    Pt = TinhPt(X, Y)
    P_t = 0
    for i in range(len(Pt)):
        P_t += Pt[i] * t**(len(Pt)-i-1)
    print(f"Đa thức nội suy từ {len(X)} điểm nội suy là: P(t) =", P_t)
    print(f"Đạo hàm của hàm tại x = {c} là:", DaoHamPt(X, Y, c))
