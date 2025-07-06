from datetime import datetime
class CuaRo:
    def __init__(self, ten, donvi, thoigian):
        self.ten = ten
        self.donvi = donvi
        tg = datetime.strptime(thoigian, "%H:%M") - datetime.strptime("06:00", "%H:%M")
        duration = tg.total_seconds() / 3600
        self.vantoc = 120/ duration
    
    def __str__(self):
        ma = ''
        for el in self.donvi.split():
            ma +=el[0]
        for el in self.ten.split():
            ma +=el[0]
        return f'{ma} {self.ten} {self.donvi} {round(self.vantoc)} Km/h' #tinh round khi in ket qua

arr = []
for _ in range(int(input())):
    cr = CuaRo(input(), input(), input())
    arr.append(cr)


arr.sort(key=lambda x: (-x.vantoc)) 

for el in arr:
    print(el)


    
    