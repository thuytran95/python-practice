'''
AT[i][j] = A[j][i]
tich[i][j] = Tong xich ma(a[i][k] + b[k][j]
trong do k la hang cua ma tran b (ma tran chuyen vi)
'''


t = int(input())             
ip = []
while True:
    # appen va flatMap trong js
    try: ip.extend(map(int, input().split()))
    except: break

i = 0
for _ in range(t):
    n, m = ip[i], ip[i+1]  
    i+=2
    # m cot , n hang
    arr = [[0 for _ in range(m)] for _ in range(n)]
    while  len(ip) - i < n * m: ip.append(0) # trong truong hop nhap thieu
    for ii in range(n):
        for jj in range(m):
            arr[ii][jj] = ip[i + jj]
        i+=m

    # m hang, n cot
    brr =[[0 for _ in range(n)] for _ in range(m)]
    # hang
    for ii in range(m):
        # cot
        for jj in range(n):
            brr[ii][jj] = arr[jj][ii]
        
    tich = []
    for ii in range(n):
        res = []
        for jj in range(n):
            tong = 0
            for k in range(m):
                tong += arr[ii][k] * brr[k][jj]
            res.append(tong)
        tich.append(res)
    for el in tich:
        print(' '.join(map(str, el)))