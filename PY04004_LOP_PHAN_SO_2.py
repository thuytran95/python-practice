import math

class Phanso:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutGon(self):
        ucln = math.gcd(self.tu, self.mau)
        return Phanso(self.tu//ucln, self.mau// ucln)

    def tinhTong(self, p):
        mauChung= (self.mau * p.mau)//math.gcd(self.mau, p.mau)
        tuChung = self.tu * (mauChung//self.mau) + p.tu * (mauChung// p.mau)
        return Phanso(tuChung,mauChung)        

    def __str__(self):
        return f'{self.tu}/{self.mau}'



if __name__ == "__main__":
    tu1, mau1, tu2, mau2 = map(int, input().split())
    ps1 = Phanso(tu1,mau1)
    ps2 = Phanso(tu2, mau2)
    ps1 =  ps1.rutGon()
    ps2 = ps2.rutGon()
    tongPs = ps1.tinhTong(ps2)
    tongPs = tongPs.rutGon()
    print(tongPs)