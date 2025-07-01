n = int(input())
arr= []
for i in range(n):
    arr.append(list(map(int, input().split())))

tongTren , tongDuoi = 0, 0
for i in range(n):
    for j in range(n):
        # bo qua truong hop bang, do tru di thi truong hop bang triet tieu
        if i < j: tongTren += arr[i][j] 
        elif i > j: tongDuoi +=arr[i][j] 

hieu = abs(tongTren - tongDuoi)
k = int(input())
if hieu > k: print('NO')
else: print('YES')
print(hieu)