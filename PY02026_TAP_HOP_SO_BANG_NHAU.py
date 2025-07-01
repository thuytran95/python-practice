n, m = map(int,input().split())
A = sorted(list(set(map(int, input().split()))))
B = sorted(list(set(map(int, input().split()))))

if len(A) != len(B): print('NO')
else:
    if A == B: print('YES')
    else: print('NO')
