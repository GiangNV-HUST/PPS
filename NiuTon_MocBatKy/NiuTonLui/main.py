import NiuTon_Lui

if __name__ == "__main__":
    X = []
    Y = []
    with open("inputLui.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            X.append(float(data[0]))
            Y.append(float(data[1]))

    TiSaiPhanCapN = NiuTon_Lui.TISAIPHANCAPN(X, Y)
    # Bảng tỉ sai phân có các hàng tương ứng với các cấp
    print("Bảng tỉ sai phân cấp n của đa thức:\n", TiSaiPhanCapN)

    HeSoNiuTon = NiuTon_Lui.HESONIUTON(X, Y)
    # Hệ số tỉ sai phân bắt đầu từ cấp 0 đến n
    print("Hệ số NiuTon của đa thức\n", HeSoNiuTon)

    # Đa thức có dạng F(x) =  a_n*x^n+ ...+ a_0*x^0
    HeSoDaThuc = NiuTon_Lui.HESODATHUC(X, HeSoNiuTon)
    print("Hệ số của đa thức là: \n", HeSoDaThuc)

    x = 13.5
    print(f"Giá trị của hàm số tại x = {x} là: ",
          NiuTon_Lui.GIATRIHAMSOTAIX(HeSoDaThuc, x))
