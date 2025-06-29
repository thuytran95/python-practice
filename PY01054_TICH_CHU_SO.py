for _ in range(int(input())):
    tich = 1
    s = input().strip()
    for el in s:
        if el != '0':
            tich *= int(el)
    print(tich)