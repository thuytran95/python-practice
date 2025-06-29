import math

def nguyenTo(n):
    for i in range(2,math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1


def checkValid(s):
    for i in range(len(s)):
        # i khong la nguyen to, s[i] la nguyen to
        if not nguyenTo(i) and s[i] in '2357': return False
        # i la nguyen to, s[i] khong la nguyen to
        if nguyenTo(i) and not s[i] in '2357': return False
    return True
for _ in range(int(input())):
    s = input().strip()
    if checkValid(s): print('YES')
    else: print('NO')
    
        