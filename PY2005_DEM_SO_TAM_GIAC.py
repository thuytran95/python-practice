def validTriagle(a, b, c):
    return a + b > c and b + c > a and c + a > b


for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    cnt = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if validTriagle(arr[i], arr[j], arr[k]): cnt +=1
    print(cnt)
    