def isValid(s):
    tongCs = 0
    
    for i in range(1, len(s)):
        n1 = int(s[i-1])
        n2 = int(s[i])
        if abs(n2 - n1) != 2: return False #khoang cach khac 2: invalid
        tongCs += n1
    tongCs += int(s[len(s) - 1]) #lay so cuoi cung do duyet mang den n-1
    return tongCs % 10 == 0

for _ in range(int(input())):
    s = input().strip()
    if isValid(s): print('YES')
    else: print('NO')
        