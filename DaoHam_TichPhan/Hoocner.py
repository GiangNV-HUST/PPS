
class Hoocner:
    def ChiaDaThucChoXTruCKhongCoDu(HeSoDaThuc, c):
        HeSoThuong = [0]*len(HeSoDaThuc)
        HeSoThuong[0] = HeSoDaThuc[0]
        for i in range(1, len(HeSoDaThuc)):
            HeSoThuong[i] = HeSoThuong[i-1]*float(c)+HeSoDaThuc[i]
        HeSoThuong.pop()
        return HeSoThuong

    def ChiaDaThucChoXTruC(HeSoDaThuc, c):
        HeSoThuong = [0]*len(HeSoDaThuc)
        HeSoThuong[0] = HeSoDaThuc[0]
        for i in range(1, len(HeSoDaThuc)):
            HeSoThuong[i] = HeSoThuong[i-1]*float(c)+HeSoDaThuc[i]
        return HeSoThuong

    def NhanDaThucVoiXTruC(HeSoDaThuc, c):
        HeSoDaThuc.append(0)
        HeSoTich = [0]*len(HeSoDaThuc)
        HeSoTich[0] = HeSoDaThuc[0]
        for i in range(1, len(HeSoDaThuc)):
            HeSoTich[i] = HeSoDaThuc[i]-HeSoDaThuc[i-1]*float(c)
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

    def DaoHamCapNCuaDaThucTaiC(HeSoDaThuc, c, n):
        Qx = Hoocner.ChiaDaThucChoXTruC(HeSoDaThuc, c)
        MaTranQx = [[0 for i in range(len(Qx))] for i in range(len(Qx))]
        DaoHamCacCap = []
        MaTranQx[0] = Qx
        DaoHamCacCap.append(Qx[len(Qx)-1])
        for i in range(n):
            Qx = Hoocner.ChiaDaThucChoXTruC(Qx, c)
            Qx.pop()
            DaoHamCacCap.append(Qx[len(Qx)-1])
            for j in range(len(Qx)):
                MaTranQx[i+1][j] = Qx[j]
            print(f"Giá trị đạo hàm cấp {i+1} của Pn(x) tại c là: {DaoHamCacCap[i+1]}")
        return MaTranQx

    def TinhWx(HeSoW):
        HeSoDaThuc = [1]
        for i in range(len(HeSoW)):
            HeSoDaThuc = Hoocner.NhanDaThucVoiXTruC(HeSoDaThuc, HeSoW[i])
        return HeSoDaThuc
