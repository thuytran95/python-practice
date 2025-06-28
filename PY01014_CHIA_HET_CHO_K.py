a, k, n = map(int, input().split())
arr = []
for i in range(0, n + 1, k):
    if i > a: arr.append(i - a)

if len(arr) == 0: print(-1)
else:
    print(' '.join(map(str,arr)))
        
    