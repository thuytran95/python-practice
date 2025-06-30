for _ in range(int(input())):
    n = int(input())
    d = dict()
    for i in range(n):
        value = int(input())
        if not value in d: d[value] = 1
        else: d[value] +=1
    ans = sorted(d,key=lambda x: (-d[x], x)) # loc theo key
    print(ans[0])