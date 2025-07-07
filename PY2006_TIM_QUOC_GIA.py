n = int(input())
d = dict()

for _ in range(n):
    arr = input().split()
    for i in range(1, len(arr)):
        d[arr[i]] = arr[0]

m = int(input())
for _ in range(m):
    city = input().strip()
    print(city, d[city])