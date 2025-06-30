import math

# khoang 1229 so nguyen to 
N = 10 ** 4 + 1
prime = [0] * N
prime[0] = prime[1] = 1
for i in range(2,math.isqrt(N) + 1):
    if prime[i] == 0:
        
        for j in range(i * i, N , i):
            prime[j]= 1

n, x = map(int, input().split())
print(x, end=' ')
while n > 0:
    for i in range(len(prime)):
        if prime[i] == 0:
            x = x + i
            print(x, end=' ')
            n-=1
        if n == 0: break
    