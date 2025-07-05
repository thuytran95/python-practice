class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
        
    def cong(self, p):
        thuc = self.thuc + p.thuc
        ao = self.ao + p.ao
        return SoPhuc(thuc, ao)
    
    def nhan(self, p):
        thuc = self.thuc * p.thuc + (-1) * self.ao * p.ao
        ao = self.thuc * p.ao + self.ao * p.thuc
        return SoPhuc(thuc, ao)
    
    def __str__(self):
        return f"{self.thuc} {'-' if self.ao < 0 else '+'} {abs(self.ao)}i"

for _ in range(int(input())):
    a, b, c , d = map(int, input().split())
    p1 = SoPhuc(a, b)
    p2 = SoPhuc(c, d)
    sptong = p1.cong(p2)
    C = sptong.nhan(p1)
    D = sptong.nhan(sptong)
    print(C, D, sep=', ')

