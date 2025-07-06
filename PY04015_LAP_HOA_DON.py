class KhachHang:
    def __init__(self, ma, ten, chiso):
        self.ma = ma
        self.ten = ten
        self.chiso = chiso
        self.tongTien =self.tinhTongTien()
    
    def tinhTongTien(self):
        cs = self.chiso
        if cs <= 50:
            return cs * 100 * 1.02
        if cs <=100:
            return (50 * 100 + (cs- 50)* 150)* 1.03
        return  (50 * 100 + 50* 150 + (cs- 100)* 200)*1.05
        
    def __str__(self):
       return f'{self.ma} {self.ten} {round(self.tongTien)}'


arr = []
for i in range(int(input())):
    ten = input()
    csCu = int(input())
    csMoi = int(input())
    hieucs = csMoi - csCu
    kh =KhachHang(f'KH{(i + 1):02d}', ten, hieucs)
    arr.append(kh)

arr.sort(key=lambda x: (-x.tongTien))

for el in arr:
    print(el)
    
        
        