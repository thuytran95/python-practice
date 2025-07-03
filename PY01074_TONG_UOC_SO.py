import math

N, M = 1 + 2 * 10** 6, 2 * 10**6
prime = N * [0]

for i in range(2, math.isqrt(M) + 1):
    if prime[i] == 0:
        prime[i]= i
        #chay tu i den (M//i) +1, buoc nhay i
        for j in range(i, M // i + 1):
            # gan lay thua so nguyen to nho nhat
            prime[i * j] = i

# tinh tong cac thua so nguyen to, bao gom lap lai
# cac so prime[0] con lai la so nguyen to
# vi cac so khac > isqrt co the chua duoc gan
'''
vd 10
prime_factor_sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 2: Gán prime_factor_sums[2] = 2 
prime_factor_sums[4] = 2
prime_factor_sums[6] = 2
prime_factor_sums[8] = 2
prime_factor_sums[10] = 2.
i = 3: 
prime_factor_sums[3] = 3
prime_factor_sums[9] = 3.
Kết quả: [0, 0, 2, 3, 2, 0, 2, 0, 2, 3, 2].
'''
for i in range(4, N): prime[i] += prime[i // prime[i]] if prime[i] else i

n = int(input())
sum = 0
for _ in range(n):
    sum += prime[int(input())]
print(sum)
