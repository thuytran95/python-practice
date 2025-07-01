n, m = map(int, input().split())
arr = list(map(int, input().split()))
d = dict()
for el in arr:
    if el in d: d[el]+=1
    else:d[el] = 1

ansKey = sorted(d, key=lambda x: (-d[x], x))
max1 = d[ansKey[0]]
max2 = 0
key = 0
for i in range(1, len(ansKey)):
    if d[ansKey[i]] <max1:
        max2 = d[ansKey[i]]
        key =ansKey[i]
        break
if max2 != 0: 
    print(key)
else: print('NONE')