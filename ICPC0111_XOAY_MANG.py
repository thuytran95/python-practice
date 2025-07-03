if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n , d = map(int, input().split())
        arr = list(map(int, input().split()))
        d %= n
        arr = arr[d:] + arr[:d]
        print(' '.join(map(str, arr)))
        
        


