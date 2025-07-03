import math

def nguyento(n):
    for i  in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2, n - 6 + 1):
        if nguyento(i) and (nguyento(i + 2) or nguyento(i + 4)) and nguyento(i + 6):
            cnt+=1
    print(cnt)