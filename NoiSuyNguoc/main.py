import NiuTon_Lui


if __name__ == "__main__":
    X = []
    Y = []
    with open("input.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            X.append(float(data[0]))
            Y.append(float(data[1]))

    print(NiuTon_Lui.TISAIPHANCAP1(X,Y))
    print(NiuTon_Lui.TISAIPHANCAPN(X,Y))
    
    heSoNiuTon = NiuTon_Lui.HESONIUTON(X,Y)
    print(heSoNiuTon)
    heSoDaThuc = NiuTon_Lui.HESODATHUC(X,heSoNiuTon)
    print(heSoDaThuc)
    print(NiuTon_Lui.GIATRIHAMSOTAIX(heSoDaThuc,13.5))