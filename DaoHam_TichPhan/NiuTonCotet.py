import numpy
import sympy
import Hoocner

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

def ChonMocDanhGiaSaiSo(X,Y,n):
    MocNoiSuy = numpy.zeros((2,round((len(X)+1)/n)))
    
    for i in range(round((len(X)+1)/n)):
        MocNoiSuy[0][i]= X[n*i]
        MocNoiSuy[1][i]= Y[n*i]
    return MocNoiSuy


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


def TinhI(X, Y, m):
    N = int((len(X)-1)/m)
    I = 0
    Hi = HeSoCoTet(m)
    h = X[1] - X[0]
    for i in range(N):
        for j in range(m+1):
            I += h*(Y[m*i+j])*Hi[j]
    return I



if __name__ == "__main__":
    print("SỬ DỤNG PHƯƠNG PHÁP NiuTonCoTet TÍNH GẦN ĐÚNG TÍCH PHÂN!")
    # X = []
    # Y = []
    # # n là số đoạn của bảng sai phân hay độ dài tập X-1
    # n = 20
    #! m là hệ số cotet
    m = 2
    # f = (3.5*x**2 + 0.1*x - 2.8)/(x-0.4)
    # a = 2.2
    # b = 3.4
    # print(f"Tích phân của hàm f= {f} trên đoạn [{a},{b}] là")
    # bangNoiSuy = BangNoiSuy(f, a, b, n)
    # print(f"Bảng nội suy tương ứng với n = {n} là:")
    # print(bangNoiSuy)
    # for i in range(n+1):
    #     X.append(bangNoiSuy[i][0])
    #     Y.append(bangNoiSuy[i][1])
    
    X = []
    Y = []
    with open("input.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            X.append(float(data[0]))
            Y.append(float(data[1]))
    # !c chia theo lưới phủ
    c=2
    MocSaiSo = ChonMocDanhGiaSaiSo(X,Y,c)
    XSaiSo = []
    YSaiSo = []
    for i in range(len(MocSaiSo[0])):
        XSaiSo.append(MocSaiSo[0][i])
        YSaiSo.append(MocSaiSo[1][i])

    I_h = TinhI(X, Y,m)
    I_hTrenC = TinhI(XSaiSo, YSaiSo,m)
    print(HeSoCoTet(m))
    print("Giá trị của I là:",I_h)
    print("Giá trị của I_hTrenC là:", I_hTrenC)
    print(f"Giá trị của |I_h - I_h/{c}| = {(I_h-I_hTrenC)*4/3}")
