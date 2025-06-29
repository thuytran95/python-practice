def  kiemTraChiaHet7(s):
    tong = int(s)
    while tong % 7 != 0:
        tong = tong + int( str(tong)[::-1])
    return tong

for _ in range(int(input())):
    s = input().strip()
    print(kiemTraChiaHet7(s))