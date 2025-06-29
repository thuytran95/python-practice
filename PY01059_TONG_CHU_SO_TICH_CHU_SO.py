for _ in range(int(input())):
    s = input().strip()
    tong = 0
    tich = 1
    soLe0 = 0
    soChan = 0
    for i in range(len(s)):
        if i % 2 == 0:
            tong+= int(s[i])
            soChan +=1
        else:
            if s[i] != '0':
                tich *= int(s[i])
            else:
                soLe0 += 1
    if soLe0 + soChan == len(s): print(tong, 0)
    else:
        print(tong, tich)

