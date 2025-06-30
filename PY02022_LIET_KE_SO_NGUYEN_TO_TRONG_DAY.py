import math

N = int(1e6) + 1
prime = [0] * N
prime[0] = prime[1] = 1
for i in range(2, math.isqrt(N) + 1):
    if prime[i] == 0:
        for j in range(i * i, N, i):
            prime[j] = 1

n = int(input())
arr = list(map(int, input().split()))
d = dict()
for el in arr:
    if el in d: d[el]  +=1
    else:
        if prime[el] == 0: d[el] = 1
for key, value in d.items():
    print(key, value)