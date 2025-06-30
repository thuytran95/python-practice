def tichChuSo(s):
    tich = 1
    for el in s:
        tich *= int(el)
    return tich


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(key=lambda x: (tichChuSo(str(x)), x))
    print(' '.join(map(str, arr)))