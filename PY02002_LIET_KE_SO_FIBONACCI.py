fibo =100 * [0]
fibo[0] = 1
fibo[1] = 1
for i in range(2 , 94):
    fibo[i] = fibo[i-1] + fibo[i-2]


for _ in range(int(input())):
    a, b  = map(int, input().split())
    for i in range(a - 1, b):
        print(fibo[i], end=' ')
    print()