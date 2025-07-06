from decimal import Decimal, ROUND_HALF_UP
class HocSinh:
    def __init__(self, ma, ten, diem):
        self.ma = ma
        self.ten = ten
        self.diem = diem
        tongDiem = diem[0] * 2  + diem[1] * 2 + sum(diem[2:])
        dtb = tongDiem / (8 + 2 + 2)
        self.dtb = dtb.quantize(Decimal('0.1'), ROUND_HALF_UP)
        self.loai = self.xepLoai()
        
    def xepLoai(self):
        if self.dtb >= 9: return "XUAT SAC"
        if self.dtb >= 8: return "GIOI"
        if self.dtb >= 7: return "KHA"
        if self.dtb >=5: return 'TB'
        return 'YEU'   
     
    def __str__(self):
        return f'{self.ma} {self.ten} {self.dtb:.1f} {self.loai}'  

arr = []
for i in range(int(input())):
    hs = HocSinh(f'HS{(i + 1):02d}',input(), list(map(Decimal, input().split())))
    arr.append(hs)

arr.sort(key=lambda x: (-x.dtb, x.ma))

for el in arr:
    print(el)