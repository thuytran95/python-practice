import math

def nguyento(n):
    for i in range(2, math.isqrt(n)+ 1):
        if n % i == 0: return False
    return n > 1


n = int(input())
a = list(map(int, input().split()))
d= dict()

arr = []
for el in a:
    if el not in d:
        d[el] = 1
        arr.append(el)

sum = 0
found = False
sum2 = 0
vitri = -1
for i in range(len(arr)):
    sum += arr[i]
    if nguyento(sum):
        found = True
        vitri = i
    if found:
        for j in range(i+ 1, len(arr)):
            sum2 += arr[j]
        if nguyento(sum2):  break
        else: 
            found = False
            vitri = -1

if vitri != -1 : print(vitri)
else: print('NOT FOUND')