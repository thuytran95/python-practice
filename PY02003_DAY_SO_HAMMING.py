'''
1 << i : dich trai i bit, moi la dich nham them voi 2
1 << 0: 2^0
1 << 1: 2^1
1 << 2: 2^2
nhanh hon so voi 2**i vi dich bit truc tiep

gioi han 10^18 (1e18) 
so nguyen to < 5: 2,3,5
khoang chan 2 ^ x < 10^18 => x chay tu 0 - 64
khoang chan 3 ^ x < 10^18 => x chay tu 0 - 29
khoang chan 5 ^ x <  10^18 => x chay tu 0 - 27

cac so co the trung nhau nen se su dung set
'''

a = set()
MAX_VAL = int(1e18)
UPPER_LIMIT_2 = 65 # duyet tu 0 - 64 bang range, range khong lay gia tri cuoi => 64 + 1
UPPER_LIMIT_3 = 30
UPPER_LIMIT_5 = 28

for i in range(UPPER_LIMIT_2):
    n2 = 1 << i
    if n2 > MAX_VAL: break
    for j in range(UPPER_LIMIT_3):
        n3 = 3 ** j
        if n2 * n3 > MAX_VAL: break
        for k in range(UPPER_LIMIT_5):
            n5 = 5 ** k
            tich = n2 * n3 * n5
            if tich > MAX_VAL: break
            a.add(tich)

# sort a
a = sorted(a)


#tim kiem bang binary search
def binarySearch(l, r, n):
    if l > r: return "Not in sequence"
    # dich sang phai 1 bit ~ chia cho 2
    mid = (l + r) >> 1
    if a[mid] == n: return mid + 1
    if a[mid] < n: return binarySearch(mid + 1, r, n)
    return binarySearch(l, mid - 1, n)


# solve problem
for _ in range(int(input())):
    n = int(input())
    print(binarySearch(0,len(a), n))
