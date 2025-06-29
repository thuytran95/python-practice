import math

def nguyenTo(n):
    for i in range(2, math.isqrt(n)+ 1):
        if n % i == 0: return False
    return n > 1

def checkValid(s):
    tong = 0
    for i in range(len(s)):
        el = int(s[i])
        #vi tri chan, la so le
        if i % 2 == 0 and el % 2 != 0: return False
        # vi tri le, la so chan
        if i % 2 != 0 and el % 2 == 0: return False 
        tong += el
    return nguyenTo(tong)
    
    
for _ in range(int(input())):
    s = input().strip()
    if checkValid(s): print('YES')
    else: print("NO")