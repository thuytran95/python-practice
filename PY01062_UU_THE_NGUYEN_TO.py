import math

def nguyenTo(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

def checkValid(s):
    if not nguyenTo(len(s)): return False
    cntNgto = 0
    for el in s:
        if el in '2357': cntNgto+=1
    return cntNgto > len(s) - cntNgto

for _ in range(int(input())):
    s = input().strip()
    if checkValid(s): print('YES')
    else: print('NO')