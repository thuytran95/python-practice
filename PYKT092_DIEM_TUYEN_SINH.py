def chuanhoa (s):
    ss = s.strip().lower().split()
    res = []
    for el in ss:
        res.append(el.title())
    return ' '.join(res)
    

class ThiSinh:
    def __init__(self, ma,ten, diem, dantoc, khuvuc):
        self.ma = ma
        self.ten = ten
        self.khuvuc = khuvuc
        self.dantoc = dantoc
        self.diem = diem + self.tinhDiemUuTien()
        
    
    def tinhDiemUuTien(self):
        diemut = 0 
        if self.khuvuc == '1': diemut +=1.5
        elif self.khuvuc == '2' : diemut += 1
        
        if self.dantoc != "Kinh": diemut +=1.5
        return diemut


    def __str__(self):
        return f"{self.ma} {self.ten} {self.diem} {'Do' if self.diem >= 20.5 else 'Truot'}"
        
arr = []
for i in range(int(input())):
    ten = chuanhoa(input())
    ts = ThiSinh(f'TS{(i +1):02d}', ten, float(input()), input().strip(), input().strip())
    arr.append(ts)


arr.sort(key=lambda x: (-x.diem, x.ma))
for el in arr:
    print(el)
