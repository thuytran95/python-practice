n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n + 1):
    try: arr.index(i) #truy xat index neu xuat hien thi bo qua
    except:
        print(i) #chua xuat hien thi print va break luon
        n = 0
        break
if n != 0: print(n + 1)