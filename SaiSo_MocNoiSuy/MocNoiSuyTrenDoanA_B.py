import math
import numpy

class MocNoiSuy:
    def MocNoiSuy(a, b, n):
        X = [None]*(n+1)
        for i in range(n+1):
            X[i] = 1/2*((b-a)*math.cos((2*i+1)/(2*(n+1))*math.pi)+(b+a))
        X.reverse()
        return X
 

    if __name__ == "__main__":
        a = 1
        b = 5
        n = 8
        Z = numpy.array([-1.14159,-1.23368,-1.2758,-1.27445,-1.23452,-1.15954,-1.05189,-0.54357,-0.3122])
        print(Z+1/5)
        print("Các mốc nội suy tối ưu trên [a,b] là: ")
        print(MocNoiSuy(a, b, n))

