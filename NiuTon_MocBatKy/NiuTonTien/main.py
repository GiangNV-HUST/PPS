import NiuTon_Tien

if __name__ == "__main__":
    X = []
    Y = []
    with open("inputTien.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            X.append(float(data[0]))
            Y.append(float(data[1]))

    # Bảng tỉ sai phân có các hàng tương ứng với các cấp
    TiSaiPhanCapN = NiuTon_Tien.TISAIPHANCAPN(X, Y)
    print("Bảng tỉ hiệu cấp n của đa thức:\n", TiSaiPhanCapN)

    # Hệ số sắp xếp từ tỉ hiệu cấp 0 đến n
    HeSoNiuTon = NiuTon_Tien.HESONIUTON(X, Y)
    print("Hệ số Niuton của đa thức là:\n", HeSoNiuTon)

    # Đa thức có dạng F(x) =  a_n*x^n+ ...+ a_0*x^0
    HeSoDaThuc = NiuTon_Tien.HESODATHUC(X, HeSoNiuTon)
    print("Hệ số của đa thức là:\n", HeSoDaThuc)

    x = 3.15
    print(f"Giá trị của hàm số tại x = {x} là: ",
          NiuTon_Tien.GIATRIHAMSOTAIX(HeSoDaThuc, x))
