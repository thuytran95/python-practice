for _ in range(int(input())):
    s = input().strip()
    tong = 0
    for el in s:
        tong+= int(el)
    if tong % 3 == 0: print('YES')
    else: print('NO')