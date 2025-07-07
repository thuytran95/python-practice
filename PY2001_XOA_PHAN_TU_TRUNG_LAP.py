d = dict()
for _ in range(int(input())):
    n = int(input())
    if n not in d:
        d[n] = 1

for key, value in d.items():
    print(key, end=' ')