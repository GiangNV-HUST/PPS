from Hoocner import Hoocner
import numpy as np
HeSoW = []
HeSoDaThuc = [2,3,0,-1,4]
c = 1


if __name__ == "__main__":
    print("Bắt đầu chương trình!")
    # print("Hàm Wx là: ")
    # print(Hoocner.TinhWx(HeSoW))
    # print("Giá trị của đa thức tại c là: ")
    # print(Hoocner.GiaTriCuaDaThucTaiC(HeSoDaThuc,c))
    # print("Thương của đa thức chia cho x-c là: ")
    # print(Hoocner.ChiaDaThucChoXTruC(HeSoDaThuc,c))
    print(np.array(Hoocner.DaoHamCapNCuaDaThucTaiC(HeSoDaThuc, c,3)))
    print("Kết thúc chương trình!")