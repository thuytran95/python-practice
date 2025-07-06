class SinhVien:
    def __init__(self, ma, ten,team):
        self.ma = ma
        self.ten = ten
        self.team = team

    def __str__(self):
        return f'{self.ma} {self.ten} {self.team[1]} {self.team[2]}'
    

team = dict()
n = int(input())
for i in range(n):
    ma = f'Team{(i + 1):02d}'
    team[ma] = (ma, input(), input())
 
arr = []   
for i in range(int(input())):
    ma = f'C{(i + 1):03d}'
    ten = input()
    doi = team[input()]
    sv = SinhVien(ma,ten,doi)
    arr.append(sv)

arr.sort(key=lambda x: x.ten)

for el in arr:
    print(el)




