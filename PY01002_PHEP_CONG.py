arr =list(map(str, input().strip().split()))

a, b, c = int(arr[0]), int(arr[2]), int(arr[-1])

if a + b == c: print('YES')
else: print("NO")