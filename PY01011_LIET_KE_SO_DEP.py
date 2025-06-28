def isValid(s):
    if len(s) % 2 == 1 or s != s[::-1]: return False # check thuan nghich, so chu so chia 2 du 1
    for c in s:
        if int(c) % 2 == 1: #check co ton tai so le hay khong
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(22, n, 2):
        if(isValid(str(i))): print(i, end=' ')
    print()