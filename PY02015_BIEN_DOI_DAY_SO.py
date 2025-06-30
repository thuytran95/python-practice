while True:
    arr = list(map(int, input().split()))
    if arr.count(0) == len(arr): break
    
    cnt = 0
    while True:
        # truong hop mang da cho 4 so bang nhau => khong can bien doi
        if arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]: break    
        a = []
        for i in range(4):
            a.append(abs(arr[i] - arr[(i + 1) % 4]))
        cnt+=1
        arr = a
    print(cnt)

    