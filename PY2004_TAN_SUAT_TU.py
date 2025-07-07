n = int(input())
d = dict()
for _ in range(n):
    tu = input().strip().split()
    for el in tu:
        if el in d: d[el] +=1
        else:
            d[el] = 1
resKey = sorted(d,key=lambda x: (-d[x], x))

for el in resKey:
    print(el, d[el])