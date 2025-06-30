a = []
while len(a) < 10:
    a += [int(i) for i in input().split()]

setA = set()
for el in a:
    setA.add(el % 42)
print(len(setA))