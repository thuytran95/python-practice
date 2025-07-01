n = int(input())
arr = []
for i in range(n):
    # cach nhanh nhat dao nguoc lai de xet duong cheo phu
    tmp = list(map(int, input().split()))
    tmp.reverse()
    arr.append(tmp)

tongTren, tongDuoi = 0, 0
for i in range(n):
    for j in range(n):
        if i > j: tongTren +=arr[i][j]
        elif i < j: tongDuoi +=arr[i][j]
hieu = abs(tongTren - tongDuoi)
k =int(input())
if hieu > k: print('NO')
else: print('YES')
print(hieu)
