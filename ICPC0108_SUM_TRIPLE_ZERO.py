for _ in range(int(input())):
    n , cnt= int(input()), 0
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n- 2):
        l, r = i + 1, n - 1
        while l < r:
            s = a[i] + a[l] + a[r]
            if s == 0:
                cnt +=1
                l+=1
            elif s < 0: l +=1
            else: r -=1
    print(cnt)
