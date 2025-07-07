for _ in range(int(input())):
    arr = list(map(int, input().split()))
    k = int(input())
    if k >= len(arr): print('INVALID')
    else:        
        for i in range(0, len(arr), k):
            tmp = arr[i: i+ k]
            print(f'[{", ".join(map(str, tmp))}]', end=" ")
        print()
        