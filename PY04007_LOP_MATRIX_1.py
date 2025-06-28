


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a =[]
        for i in range(n):
            a.append(list(map(int, input().split())))
            
        mt = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(a[j][i]) # dao nguoc a[i][j] thanh a[j][i]
            mt.append(tmp)
                
        for i in range(m):
            for j in range(n):
                print(mt[i][j], end=' ')
            print()