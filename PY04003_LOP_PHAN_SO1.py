import math

class Phanso:
    def __init__(self, tu, mau):
        self.tu  = tu
        self.mau = mau
    
    
    def rutGon(self):
        ucln = math.gcd(tu, mau)
        return Phanso(tu//ucln, mau// ucln)
    
    
    def __str__(self):
        return f'{self.tu}/{self.mau}'



if __name__ == "__main__":
    tu, mau = map(int, input().split())
    ps = Phanso(tu, mau)
    ps2 = ps.rutGon()
    print(ps2)