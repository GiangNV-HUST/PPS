import numpy
import sympy
import Lagrange

x = sympy.symbols("x")


def BangNoiSuy(f, a, b, n):
    h = (b-a)/n
    bangNoiSuy = numpy.zeros((2, n+1))
    bangNoiSuy[0][0] = a
    bangNoiSuy[1][0] = f.subs(x, a)
    for i in range(n):
        bangNoiSuy[0][i+1] = bangNoiSuy[0][i] + h
        bangNoiSuy[1][i+1] = f.subs(x, bangNoiSuy[0][i+1])
    return bangNoiSuy


def TinhI(X, Y):
    h = X[1] - X[0]
    I = 0
    n = len(X)
    for i in range(n-1):
        I += h*(Y[i]+Y[i+1])/2
    return I


if __name__ == "__main__":
    f = 1/(1+x)
    n = 10
    a = 0
    b = 1
    bangNoiSuy = BangNoiSuy(f, a, b, n)
    print(f"Bảng nội suy của hàm f= {f} là:")
    print(bangNoiSuy)
    X = []
    Y = []
    for i in range(n+1):
        X.append(bangNoiSuy[0][i])
        Y.append(bangNoiSuy[1][i])
    print(TinhI(X, Y))
    print(len(bangNoiSuy[1]))
