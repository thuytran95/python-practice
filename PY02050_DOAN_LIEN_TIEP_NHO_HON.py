for  _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    stack = []
    for i in range(n):
        # mang arr[i] o dang tupple (1, 2) ( 1 la gia tri a[i], 2 la vi tri index)
        arr[i] = (arr[i], i) 
        '''
        kiem tra phan tu tren cung cua stack co nho hon phan tu a[i] khong
        neu co thi gan gia tri index cua phan tu tren cung
        va pop phan tu do ra khoi stack
        '''
        while len(stack) > 0 and stack[-1][0] <= arr[i][0]:
            arr[i]= (arr[i][0], stack[-1][1]) 
            stack.pop()
        stack.append(arr[i])
    for i in range(n):
        print(i - arr[i][1]+ 1,end=' ')

    print()