import math



N= 1001
prime = [0] * N
prime[0] = prime[1] = 1
for i in range(2, math.isqrt(N) + 1):
    if prime[i] == 0:
        for j in range(i * i, N, i):
            prime[j] = 1
        


n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if prime[a[i]] == 0:
        for j in range(i + 1, n):
            if prime[a[j]] == 0 and a[j] < a[i]:
                a[i], a[j]= a[j], a[i]

print(' '.join(map(str, a)))
