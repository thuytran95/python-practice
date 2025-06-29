import math

def nguyenTo(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1


def checkUuThe(s):
    if not nguyenTo(len(s)): return False
    nguyenToS = '2357'
    cnt = 0
    for el in s:
        if el in nguyenToS:
            cnt+=1
    return cnt > len(s) - cnt

for _ in range(int(input())):
    s = input().strip()
    if checkUuThe(s): print('YES')
    else: print("NO")