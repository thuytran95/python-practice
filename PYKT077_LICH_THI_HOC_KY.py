from datetime import datetime

class LichThi:
    def __init__(self,ma, mon, ngaythi, giothi, nhom):
        self.ma = ma
        self.mon = mon
        self.ngaythi = ngaythi
        self.giothi = giothi
        self.nhom = nhom
    
    def __str__(self):
        return f'{self.ma} {self.mon[0]} {self.mon[1]} {self.ngaythi} {self.giothi} {self.nhom}'
        

n, m = map(int, input().split())

monhoc = dict()
for i in range(n):
    ma = input()
    ten = input()
    monhoc[ma]= (ma, ten, )


arr = []
for i in range(m):
    ma = f'T{(i + 1):03d}'
    s = input().split()
    maM = s[0]
    mon = monhoc[maM]
    lt = LichThi(ma, mon, s[1], s[2], s[3])
    arr.append(lt)
    
arr.sort(key=lambda x: (datetime.strptime(x.ngaythi, "%d/%m/%Y"), datetime.strptime(x.giothi, '%H:%M'), x.mon[0]))

for el in arr:
    print(el)
