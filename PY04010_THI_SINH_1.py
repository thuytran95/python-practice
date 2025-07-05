class ThiSinh:
    def __init__(self, ten, ngaySinh, d1, d2, d3):
        self.ten = ten
        self.ngaySinh = ngaySinh
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.tong = d1 + d2 + d3
    
    
    def __str__(self):
        return f'{self.ten} {self.ngaySinh} {self.tong:.1f}'

print(ThiSinh(input().strip(), input().strip(), float(input()), float(input()), float(input())))