for _ in range(int(input())):
    n = int(input())
    tong = 0
    start = 1 if n % 2 != 0 else 2   
    for i in range(start, n + 1 ,2):
        tong += 1/ i       
    print(f'{tong:.6f}')
