n = int(input())
a = []
for _ in range(n):
    d = {"ma": input(), "ten": input(), "hinhThucThi":input() }
    a.append(d)
    
a.sort(key=lambda x: x["ma"])

for el in a:
    for v in el.values():
        print(v, end=' ')
    print()