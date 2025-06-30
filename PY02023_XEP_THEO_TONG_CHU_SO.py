
def tongChuSo(s):
    tong = 0
    for el in s:
        tong +=int(el)
    return tong


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = sorted(arr, key=lambda x: (tongChuSo(str(x)), x))
    print(' '.join(map(str, ans)))