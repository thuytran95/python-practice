def ktraTangGiam(s):
    if len(s) < 3: return False
    arr = list(int(el) for el in s)
    up = True
    for i in range(1, len(arr)):
        # tim vi tri dau tien bat dau giam
        # vd 12342=> i = 4
        if up and arr[i - 1] >= arr[i]: 
            up = False
        # dang down va tang tro lai
        elif not up and arr[i- 1] <= arr[i]:
            return False
    return True


for _ in range(int(input())):
    s = input().strip()
    if ktraTangGiam(s): print('YES')
    else: print('NO')