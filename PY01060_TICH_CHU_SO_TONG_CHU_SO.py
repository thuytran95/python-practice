for _ in range(int(input())):
    s = input().strip()
    tich = 1
    tong = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != '0': tich *= int(s[i])
        else: tong += int(s[i])
    print(tich, tong)