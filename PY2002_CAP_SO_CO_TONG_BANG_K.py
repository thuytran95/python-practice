for _ in range(int(input())):
    arr = list(map(int, input().split()))
    k = int(input())
    n = len(arr)

    res = []
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                t = f'({arr[i]}, {arr[j]})'
                res.append(t)

    if len(res) == 0: print('NO')
    else:
        print(' '.join(res))
    