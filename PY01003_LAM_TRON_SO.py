def round(i): return 1 if i >= 5 else 0

t = int(input())
for _ in range(t):
    a= [int(x) for x in input().strip()]
    for i in range(len(a) - 1, 0, -1):
        a[i - 1] += round(a[i])
        a[i] = 0
    print(''.join(map(str, a)))
        