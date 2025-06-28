def tinhLai(n, x,m):
    cntYear = 0
    while n < m:
        n = (1 + x * 1/100) * n
        cntYear += 1
    return cntYear

t = int(input())
for _ in range(t):
    n, x, m = map(float, input().split())
    res =  tinhLai(n, x, m)
    print(res)