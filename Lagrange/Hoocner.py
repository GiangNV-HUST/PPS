class Hoocner:
    def ChiaDaThucChoXTruC(HeSoDaThuc, c):
        HeSoThuong = [0]*len(HeSoDaThuc)
        HeSoThuong[0] = HeSoDaThuc[0]
        for i in range(1, len(HeSoDaThuc)):
            HeSoThuong[i] = HeSoThuong[i-1]*c+HeSoDaThuc[i]
        # print("Số dư là:",SoDu)
        return HeSoThuong

    def NhanDaThucVoiXTruC(HeSoDaThuc, c):
        HeSoDaThuc.append(0)
        HeSoTich = [0]*len(HeSoDaThuc)
        HeSoTich[0] = HeSoDaThuc[0]
        for i in range(1, len(HeSoDaThuc)):
            HeSoTich[i] = HeSoDaThuc[i]-HeSoDaThuc[i-1]*c
        return HeSoTich

    def GiaTriCuaDaThucTaiC(HeSoDaThuc, c):
        HeSoThuong = Hoocner.ChiaDaThucChoXTruC(HeSoDaThuc, c)
        SoDu = HeSoThuong.pop()
        return SoDu

    def DaoHamCuaDaThucTaiC(HeSoDaThuc, c):
        HeSoThuong = Hoocner.ChiaDaThucChoXTruC(HeSoDaThuc, c)
        HeSoThuong.pop()
        GiaTriDaoHamTaiC = Hoocner.GiaTriCuaDaThucTaiC(HeSoThuong, c)
        return GiaTriDaoHamTaiC

    def TinhWx(HeSoW):
        HeSoDaThuc = [1]
        for i in range(len(HeSoW)):
            HeSoDaThuc = Hoocner.NhanDaThucVoiXTruC(HeSoDaThuc, HeSoW[i])
        return HeSoDaThuc
