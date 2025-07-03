n, m = map(int, input().split())

arr = []
maxThuanNghich = 1
for i in range (n):
    tmp = list(map(int, input().split()))
    for el in tmp:
        s = str(el)
        if el > 10 and s == s[::-1] and el > maxThuanNghich:
            maxThuanNghich = el
    arr.append(tmp)

if maxThuanNghich ==1: print('NOT FOUND')
else:
    for i in range(n):
        for j in range(m):
            if arr[i][j] == maxThuanNghich:
                print(f'Vi tri [{i}][{j}]')