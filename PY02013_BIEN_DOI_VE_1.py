while True:
    n = int(input())
    if n == 0: break
    if n == 1: print(1)
    else:
        cnt = 1
        m = n
        while m != 1:
            if m % 2 == 0: m = m >> 1
            else: m = 3 * m + 1
            cnt +=1
        print(cnt)
