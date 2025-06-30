n = int(input())
a = input().split()
cnt = 0
for i in range(1, len(a)):
    if a[i] != a[i -1]: cnt +=1
print(cnt)