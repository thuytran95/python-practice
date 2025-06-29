import math

for _ in range(int(input())):
    s = input().strip()
    if math.gcd(int(s), int(s[::-1])) == 1: print('YES')
    else: print('NO')
