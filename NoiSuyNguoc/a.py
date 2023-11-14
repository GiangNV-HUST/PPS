from Hoocner import Hoocner
import NiuTon_Lui
from NiuTon_Tien import NiuTon_Tien

if __name__ == "__main__":
    X = []
    Y = []
    with open("input.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            X.append(float(data[0]))
            Y.append(float(data[1]))

    print(Y)
    print(X)
    bangSaiPhan = NiuTon_Lui.TISAIPHANCAPN(Y,X)
    print("Bảng sai phân: ")
    print(bangSaiPhan)
    print("Hệ số Niu Ton là: ")
    heSoNiuTon = NiuTon_Lui.HESONIUTON(Y,X)
    print(heSoNiuTon)
    heSoDaThuc = NiuTon_Lui.HESODATHUC(Y,heSoNiuTon)
    print("Hệ số của đa thức là: ")
    print(heSoDaThuc)
    GiaTriHamSo = NiuTon_Lui.GIATRIHAMSOTAIX(heSoDaThuc,25314)
    print("Giá trị của hàm là: ")
    print(GiaTriHamSo)