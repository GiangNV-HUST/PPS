import numpy
import sympy

x = sympy.symbols("x")

def BangNoiSuy(f,a,b,n):
    bangNoiSuy = numpy.zeros((n+1,2))
    h = (b-a)/ n
    bangNoiSuy[0][0] = a
    for i in range(0,n):
        bangNoiSuy[i+1][0] = bangNoiSuy[i][0] + h
    for i in range(0,n+1):
        bangNoiSuy[i][1] = f.subs(x,bangNoiSuy[i][0])
    return bangNoiSuy


def TinhI(X,Y):
    n = int((len(X)-1)/2)
    I = 0
    h = X[1] - X[0]
    for i in range(n):
        I += h*(Y[2*i]+4*Y[2*i+1]+Y[2*i+2])/3
    return I

if __name__ == "__main__":
    print("SỬ DỤNG PHƯƠNG PHÁP SIMSON TÍNH GẦN ĐÚNG TÍCH PHÂN!")
    X=[]
    Y= []
    n=10
    f = 1/(1+x)
    a=0
    b=1
    print(f"Tích phân của hàm f= {f} trên đoạn [{a},{b}] là")
    bangNoiSuy = BangNoiSuy(f,a,b,n)
    print(f"Bảng nội suy tương ứng với n = {n} là:")
    print(bangNoiSuy)
    for i in range(n+1):
        X.append(bangNoiSuy[i][0])
        Y.append(bangNoiSuy[i][1])
    
    print("Giá trị của I là:",TinhI(X,Y))
