def xoayMang(arr, d):
    return arr[d:] + arr[:d] # noi mang tu d->n va tu 0:d

if __name__ =="__main__":
    t = int(input())
    for _ in range(t):
        n, d = map(int, input().split())
        arr = list(map(int, input().split()))
        d %=n #chia dua de dam bao d < n
        res = xoayMang(arr, d)
        print(' '.join(map(str, res)))
        
        