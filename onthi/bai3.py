for _ in range(int(input())):
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    if len(l1) != len(l2): print('INVALID')
    else:
        res = 0
        for i in range(len(l1)):
            res += l1[i] * l2[i]
        print(res)
    