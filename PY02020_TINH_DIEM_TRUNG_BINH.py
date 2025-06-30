n = int(input())
arr = list(map(float, input().split()))
arr.sort()
ans = 0
cnt = 0
for i in range(1, n - 1):
    if arr[i] == arr[0] or arr[i] == arr[n - 1]: continue
    ans += arr[i]
    cnt+=1
print(f'{(ans/cnt):.2f}')