import math

N = 1001
prime = [0] * N
prime[0] = prime[1] = 1
for i in range(2, math.isqrt(N) + 1):
    if prime[i] == 0:
        for j in range(i * i , N, i):
            prime[j]= 1
            
n, m = map(int, input().split())

for i in range(n):
    tmp = [int(x) for x in input().split()]
    for j in range(m):
        if prime[tmp[j]] == 0: print(1, end=' ')
        else: print(0, end=' ')
    print()

    
        
        