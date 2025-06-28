import math
class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def distance (self, p):
        return math.sqrt((self.x - p.x)** 2 + (self.y - p.y)**2)
    
    
class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.xy = x.distance(y)
        self.yz = y.distance(z)
        self.xz = x.distance(z)
    
    
    def isValid(self):
        return (self.xy + self.yz > self.xz) and (self.yz+ self.xz> self.xy) and (self.xz + self.xy > self.yz)


    def congThucHero(self):
        tich = (self.xy + self.yz + self.xz)* (self.xy + self.yz - self.xz)*(self.xy - self.yz + self.xz)* (-self.xy + self.yz + self.xz)
        s = 0.25 * math.sqrt(tich)
        return f'{s:.2f}'
    
    
if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        a += [float(i) for i in input().split()]
    
    i = 0
    for _ in range(t):
        p1 = Point(a[i], a[i + 1])
        p2 = Point(a[i+ 2], a[i + 3])
        p3= Point(a[i+ 4], a[i + + 5])
        triangle = Triangle(p1, p2,p3)
        if triangle.isValid():
            print(triangle.congThucHero())
        else:
            print('INVALID')
        i +=6