import math
import numpy as np
from Hoocner import Hoocner


def KhoangLiNghiem(yNgang, Y):
    khoangLiNghiem = []
    for i in range(len(Y)-1):
        if ((Y[i] - yNgang)*(Y[i+1]-yNgang) < 0):
            khoangLiNghiem.append((Y[i], Y[i+1]))
    return khoangLiNghiem


def LapTien(X,Y,yNgang):
    


if __name__ == "__main__":
    X = []
    Y = []
    with open("input.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            X.append(float(data[0]))
            Y.append(float(data[1]))
    yNgang = 3.15
    print(KhoangLiNghiem(yNgang, Y))
