import math
def nguyento(n):
    for i in range(2,math.isqrt(n) + 1): 
        if n % i == 0: return False
    return  n > 1

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(n):
        if math.gcd(i, n) == 1: cnt +=1
    if nguyento(cnt): print('YES')
    else: print('NO')