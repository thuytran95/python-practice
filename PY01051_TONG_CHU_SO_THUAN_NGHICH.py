def checkThuanNghich(n):
    if n < 10: return False
    tongStr = str(n)
    if  tongStr != tongStr[::-1]:return False
    return True

for _ in range(int(input())):
    s = input().strip()
    if(len(s) <= 1): print('NO')
    else:
        tong = 0
        for el in s:
            tong += int(el)
        if checkThuanNghich(tong): print('YES')
        else: print('NO')
    