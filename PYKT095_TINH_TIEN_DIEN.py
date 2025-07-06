def chuanhoa(s):
    ss =s.strip().lower().split()
    res = []
    for el in ss:
        res.append(el.title())
    return ' '.join(res)



class Khachhang:
    def __init__(self, ma, ten, loai, sodien):
        self.ma =ma
        self.ten = ten
        self.loai = loai
        self.sodien = sodien
        dm = self.dinhMuc()
        self.trongdm = sodien * 450 if sodien < dm else dm * 450
        self.vuotdm = 0 if sodien <= dm else (sodien - dm)* 1000
        self.vat = self.vuotdm // 20
        self.tongtien = self.trongdm + self.vuotdm + self.vat
    
    def dinhMuc(self):
        if self.loai == 'A': return 100
        if self.loai == 'B': return 500
        return 200
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.trongdm} {self.vuotdm} {self.vat} {self.tongtien}'
 
arr  = []   
    
for i in range(int(input())):
    makh = f'KH{(i + 1):02d}'
    ten = chuanhoa(input())
    ss = input().split()
    sodien = int(ss[2])- int(ss[1]) 
    kh = Khachhang(makh, ten, ss[0],sodien)
    arr.append(kh)

arr.sort(key=lambda x: (-x.tongtien))

for el in arr:
    print(el)