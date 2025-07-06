from datetime import datetime

class Phim:
    def __init__(self,ma, theloai, ngaykc, ten,sotap ):
        self.ma = ma
        self.theloai = theloai
        self.ngaykc = ngaykc
        self.ten = ten
        self.sotap = sotap
    
    
    def __str__(self):
        return f'{self.ma} {self.theloai} {self.ngaykc} {self.ten} {self.sotap}'  

n, m  = map(int, input().split())


theloai = dict()
for i in range(n):
    ma = f'TL{(i +1):03d}'
    theloai[ma] = (ma, input().strip())

arr = []
for i in range(m):
    ma = f'P{(i+ 1):03d}'
    p = Phim(ma, theloai[input().strip()][1], input().strip(), input().strip(), int(input()))
    arr.append(p)
    
arr.sort(key=lambda x: (datetime.strptime(x.ngaykc, "%d/%m/%Y"),x.ten,-x.sotap))

for el in arr:
    print(el)