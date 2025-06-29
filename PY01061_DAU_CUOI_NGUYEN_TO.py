import math

def nguyenTo(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

for _ in range(int(input())):
    s = input().strip()
    if nguyenTo(int(s[-3:])) and nguyenTo(int(s[:3])): print('YES')
    else: print('NO')