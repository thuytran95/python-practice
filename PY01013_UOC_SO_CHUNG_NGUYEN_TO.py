import math
def nguyenTo(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    ucln = math.gcd(a, b)
    tongCs= 0
    while ucln > 0:
        tongCs += ucln % 10
        ucln //= 10    
    if nguyenTo(tongCs): print("YES")
    else: print("NO")