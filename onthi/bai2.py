for _ in range(int(input())):
    s = input().strip().split()
    for el in s:
        print(el[::-1],end=' ')
    print()