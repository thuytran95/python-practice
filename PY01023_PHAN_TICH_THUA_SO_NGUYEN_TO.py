import math
def phanTichNguyenTo(n):
    res = '1'
    for i in range(2, math.isqrt(n) + 1):
        cnt = 0
        while n % i == 0 and n != 0:
            n//= i
            cnt+= 1
        if cnt: res += f' * {i}^{cnt}'
    if n > 1: res += f' * {n}^1'
    return res


for _ in range(int(input())):
    print(phanTichNguyenTo(int(input())))
