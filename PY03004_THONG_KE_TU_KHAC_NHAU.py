
import re
n = int(input())
a = {}
for _ in range(n):
    # phai loc tat ca ca tu khong phai la chu va so
    for w in re.split("[^a-z0-9]", input().lower()):
        if w != '':
            if a.get(w) is None: a[w] = 1
            else:
                a[w] += 1

ans = sorted(a, key=lambda x: (-a[x], x))
for i in ans: print(i, a[i])
