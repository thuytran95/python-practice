
import re


n = int(input())
d={}
for _ in range(n):
    for s in re.split("[^a-z]", input().lower()):
        if s != '':
            if d.get(s) is None:
                d[s] = 1
            else: d[s] +=1

ans = sorted(d, key=lambda x: (-d[x], x))
for i in ans:
    print(i, d[i])

    