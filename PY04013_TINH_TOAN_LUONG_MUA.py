from datetime import datetime

class TramDo:
    def __init__(self, ma, ten, tongTg, tongLm):
        self.ma = ma
        self.ten= ten
        self.tongTg = tongTg
        self.tongLm = tongLm    
    
    def __str__(self):
        tongGio= self.tongTg.total_seconds() / 3600
        lmtb = self.tongLm / tongGio
        return f'{self.ma} {self.ten} {lmtb:.2f}'

d = dict()
i = 1
for _ in range(int(input())):
    ten = input()
    start= datetime.strptime(input(), "%H:%M")
    end= datetime.strptime(input(), "%H:%M")
    duration = end - start
    lm = float(input())
    if ten in d:
        d[ten].tongTg += duration
        d[ten].tongLm += lm
    else:
        d[ten] = TramDo(f'T0{i}', ten, duration, lm)
        i+=1
    
for key, value in d.items():
    print(value)