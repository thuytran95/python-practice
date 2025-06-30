for _ in range(int(input())):
    n = int(input())
    d = dict()
    a = list(map(int, input().split()))
    for val in a:
        if not val in d: d[val] =1
        else: d[val] +=1
    ans = sorted(d,key=lambda x: (-d[x], x))
    if d[ans[0]] > n//2 : print(ans[0])
    else: print('NO')