class SinhVien:
    def __init__(self, ten, toan, ly, hoa, sinh):
        self.ten = ten
        self.toan= toan
        self.ly = ly
        self.hoa = hoa
        self.sinh = sinh
        self.dtb = (toan + ly + hoa)

a =[]
for _ in range(int(input())):
    ten = input().strip()
    toan, ly, hoa , sinh = map(float, input().split())
    sv = SinhVien(ten, toan, ly, hoa, sinh)
    a.append(sv)

sortA = sorted(a, key=lambda x: (-x.dtb))

for el in sortA:
    print(f'{el.ten} {el.dtb:.2f}')