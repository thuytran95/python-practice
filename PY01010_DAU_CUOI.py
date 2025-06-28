t = int(input())
for _ in range(t):
    s = input().strip()
    start, end = s[0:2], s[-2:]
    if start == end: print("YES")
    else: print("NO")
