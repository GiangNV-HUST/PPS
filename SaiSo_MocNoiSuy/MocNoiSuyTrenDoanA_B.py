import math
import numpy

class MocNoiSuy:
    def MocNoiSuy(a, b, n):
        X = [None]*(n+1)
        for i in range(n+1):
            X[i] = 1/2*((b-a)*math.cos((2*i+1)/(2*(n+1))*math.pi)+(b+a))
        X.reverse()
        return X

    def TinhY(Z):
        numpy.array(Z)
        

    if __name__ == "__main__":
        a = 1
        b = 5
        n = 8
        print("Các mốc nội suy tối ưu trên [a,b] là: ")
        print(MocNoiSuy(a, b, n))

