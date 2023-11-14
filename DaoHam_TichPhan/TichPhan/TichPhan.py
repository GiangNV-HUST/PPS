import Lagrange1
import  Lagrange2

def TinhA_i(HeSoW,x_i,a,b):
    Li = Lagrange1.TinhLj(HeSoW,x_i)
    n = len(Li)
    A_i = 0
    for i in range(0,n):
        A_i += Li[i]*(b**(n-i) - a**(n-i))/(n-i)
    return A_i
def TinhI(X,Y,a,b):
    I = 0
    n = len(X)
    for i in range(n):
        I += TinhA_i(X,X[i],a,b)*Y[i]
    return I

if __name__ == "__main__":
    X = []
    Y = []

    with open(r"C:\Users\Giang\Desktop\PPS\Lagrange\input.txt", "r") as file:
        for line in file:
            data = line.strip().split(" ")
            X.append(float(data[0]))
            Y.append(float(data[1]))
    print(TinhI(X,Y,1,2))